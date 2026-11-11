// Laurus Kariyer: CV analysis that runs entirely in the browser. The file never leaves the device.
// PDF text comes from pdf.js (loaded only when a file is chosen); .docx is unzipped with DecompressionStream.
const root = document.getElementById('cvscan');
if (root) init();

function init() {
  const $ = (s) => root.querySelector(s);
  const drop = $('.cva-drop'), input = $('#cva-file'), job = $('#cva-job');
  const stage = $('.cva-stage'), out = $('.cva-out'), err = $('.cva-err');
  const WA = 'https://wa.me/905434309702?text=';
  const V = root.dataset.v || '1';

  ['dragenter', 'dragover'].forEach((e) => drop.addEventListener(e, (ev) => { ev.preventDefault(); drop.classList.add('over'); }));
  ['dragleave', 'drop'].forEach((e) => drop.addEventListener(e, (ev) => { ev.preventDefault(); drop.classList.remove('over'); }));
  drop.addEventListener('drop', (ev) => { const f = ev.dataTransfer.files[0]; if (f) run(f); });
  input.addEventListener('change', () => { if (input.files[0]) run(input.files[0]); });
  root.addEventListener('click', (e) => { if (e.target.closest('.cva-again')) { reset(); input.click(); } });

  function reset() { input.value = ''; out.hidden = true; out.innerHTML = ''; stage.hidden = true; err.hidden = true; root.classList.remove('done', 'busy'); }
  function fail(msg) { root.classList.remove('busy'); stage.hidden = true; err.hidden = false; err.textContent = msg; }

  async function run(file) {
    reset();
    const name = file.name.toLowerCase();
    const isPdf = name.endsWith('.pdf') || file.type === 'application/pdf';
    const isDocx = name.endsWith('.docx');
    if (!isPdf && !isDocx) return fail('Yalnızca PDF ya da Word (.docx) dosyası yükleyebilirsin. Eski .doc dosyasını Word\'de açıp "Farklı Kaydet" ile .docx ya da PDF yap.');
    if (file.size > 12 * 1024 * 1024) return fail('Dosya 12 MB\'tan büyük. CV dosyaları genelde 1 MB\'ın altındadır; görselleri küçültüp tekrar dene.');
    root.classList.add('busy'); stage.hidden = false;
    stage.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center' });
    $('.cva-fn').textContent = file.name;
    const canvas = $('.cva-page'); canvas.width = canvas.width;
    const t0 = performance.now();
    let doc;
    try { doc = isPdf ? await readPdf(file, canvas) : await readDocx(file, canvas); }
    catch (e) { return fail('Dosya okunamadı. Dosya şifreli ya da bozuk olabilir; PDF olarak yeniden kaydedip tekrar dene.'); }
    const res = analyze(doc, file, job.value || '');
    const wait = Math.max(0, 2600 - (performance.now() - t0));
    setTimeout(() => { root.classList.remove('busy'); root.classList.add('done'); render(res, file); }, wait);
  }

  // ---------- readers ----------
  async function readPdf(file, canvas) {
    const pdfjs = await import('/assets/pdf-41038.min.mjs');
    pdfjs.GlobalWorkerOptions.workerSrc = '/assets/pdf-41038.worker.min.mjs';
    const pdf = await pdfjs.getDocument({ data: await file.arrayBuffer() }).promise;
    const lines = []; let images = 0, colPages = 0; const starts = [];
    const fonts = new Set();
    for (let n = 1; n <= Math.min(pdf.numPages, 6); n++) {
      const page = await pdf.getPage(n);
      const vp = page.getViewport({ scale: 1 });
      if (n === 1) {
        const s = Math.min(2, 520 / vp.width), v2 = page.getViewport({ scale: s });
        canvas.width = v2.width; canvas.height = v2.height;
        try { await page.render({ canvasContext: canvas.getContext('2d'), viewport: v2 }).promise; } catch (e) {}
      }
      const tc = await page.getTextContent();
      const rows = new Map(); let itemN = 0; const midX = new Map();
      tc.items.forEach((it) => {
        if (!it.str || !it.str.trim()) return;
        if (it.fontName) fonts.add(it.fontName);
        const y = Math.round(it.transform[5] / 3) * 3, x = it.transform[4];
        if (!rows.has(y)) rows.set(y, []);
        rows.get(y).push({ x, s: it.str, w: it.width || 0 });
        itemN++; if (it.str.trim().length > 12 && x > vp.width * 0.27 && x < vp.width * 0.72) { const kx = Math.round(x / vp.width * 50); midX.set(kx, (midX.get(kx) || 0) + 1); }
      });
      // column check: rows that have a wide horizontal gap between two text runs
      let gapRows = 0, total = 0; const gutters = new Map();
      [...rows.entries()].sort((a, b) => b[0] - a[0]).forEach(([, arr]) => {
        arr.sort((a, b) => a.x - b.x); total++; if (arr.map((a) => a.s).join('').trim().length > 12) starts.push(arr[0].x / vp.width);
        let gap = false;
        for (let i = 1; i < arr.length; i++) { const g = arr[i].x - (arr[i - 1].x + arr[i - 1].w); if (g > vp.width * 0.09 && arr[i].x > vp.width * 0.3 && arr[i - 1].s.trim().length > 2 && arr[i].s.trim().length > 6) gap = true; }
        if (gap) gapRows++;
        let bg = 0, bx = 0; for (let i = 1; i < arr.length; i++) { const g2 = arr[i].x - (arr[i - 1].x + arr[i - 1].w); if (g2 > bg) { bg = g2; bx = arr[i].x; } }
        if (bg > vp.width * 0.03 && bx > vp.width * 0.25 && bx < vp.width * 0.75) { const kx = Math.round(bx / vp.width * 40); gutters.set(kx, (gutters.get(kx) || 0) + 1); }
        lines.push(arr.map((a) => a.s).join(' ').replace(/\s+/g, ' ').trim());
      });
      const gmax = Math.max(0, ...gutters.values());
      const mmax = Math.max(0, ...midX.values()); if (mmax >= 6 && mmax / itemN > 0.22) colPages++;
      if (total > 10 && (gapRows / total > 0.3 || gmax / total > 0.3)) colPages++;
      try { const ops = await page.getOperatorList(); ops.fnArray.forEach((f) => { if (f === pdfjs.OPS.paintImageXObject || f === pdfjs.OPS.paintInlineImageXObject) images++; }); } catch (e) {}
    }
    const leftN = starts.filter((x) => x < 0.22).length, rightN = starts.filter((x) => x > 0.3 && x < 0.75).length;
    const twoCol = starts.length > 14 && leftN / starts.length > 0.2 && rightN / starts.length > 0.3;
    return { kind: 'pdf', pages: pdf.numPages, lines, text: lines.join('\n'), images, columns: colPages > 0 || twoCol, fonts: fonts.size, tables: false };
  }

  async function readDocx(file, canvas) {
    const buf = new Uint8Array(await file.arrayBuffer());
    const xml = await unzipEntry(buf, 'word/document.xml');
    if (!xml) throw new Error('docx');
    const paras = xml.split(/<\/w:p>/).map((p) => (p.match(/<w:t[^>]*>[^<]*<\/w:t>|<w:tab\/>|<w:br\/>/g) || []).map((t) => t.startsWith('<w:t') ? t.replace(/<[^>]+>/g, '') : ' ').join('')
      .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&apos;/g, "'").trim()).filter(Boolean);
    const text = paras.join('\n');
    const words = text.split(/\s+/).filter(Boolean).length;
    drawDocPreview(canvas, paras);
    return { kind: 'docx', pages: Math.max(1, Math.round(words / 420)), lines: paras, text, images: (xml.match(/<w:drawing|<w:pict/g) || []).length,
      columns: /<w:cols[^>]*w:num="[2-9]"/.test(xml), fonts: 0, tables: (xml.match(/<w:tbl>/g) || []).length > 0, textbox: /<w:txbxContent/.test(xml) };
  }

  async function unzipEntry(u8, target) {
    const dv = new DataView(u8.buffer, u8.byteOffset, u8.byteLength);
    let e = u8.length - 22; while (e >= 0 && dv.getUint32(e, true) !== 0x06054b50) e--;
    if (e < 0) return null;
    const n = dv.getUint16(e + 10, true); let p = dv.getUint32(e + 16, true);
    const td = new TextDecoder();
    for (let i = 0; i < n; i++) {
      if (dv.getUint32(p, true) !== 0x02014b50) break;
      const method = dv.getUint16(p + 10, true), csize = dv.getUint32(p + 20, true), nl = dv.getUint16(p + 28, true), el = dv.getUint16(p + 30, true), cl = dv.getUint16(p + 32, true), off = dv.getUint32(p + 42, true);
      const name = td.decode(u8.subarray(p + 46, p + 46 + nl));
      if (name === target) {
        const lnl = dv.getUint16(off + 26, true), lel = dv.getUint16(off + 28, true), start = off + 30 + lnl + lel;
        const data = u8.subarray(start, start + csize);
        if (method === 0) return td.decode(data);
        const ds = new DecompressionStream('deflate-raw');
        const ab = await new Response(new Blob([data]).stream().pipeThrough(ds)).arrayBuffer();
        return td.decode(ab);
      }
      p += 46 + nl + el + cl;
    }
    return null;
  }

  function drawDocPreview(c, paras) {
    c.width = 520; c.height = 735; const g = c.getContext('2d');
    g.fillStyle = '#FBFAF5'; g.fillRect(0, 0, c.width, c.height); g.fillStyle = '#1b231e';
    let y = 54; paras.slice(0, 40).forEach((p, i) => {
      if (y > c.height - 30) return;
      const head = p.length < 34 && i > 0; g.font = (i === 0 ? '700 24px' : head ? '700 13px' : '400 11px') + ' "Instrument Sans", Arial, sans-serif';
      g.fillStyle = head ? '#8a6c22' : '#1b231e';
      const words = p.split(' '); let line = '';
      const lh = i === 0 ? 32 : head ? 24 : 16; if (head) y += 8;
      words.forEach((w) => { if (g.measureText(line + w).width > c.width - 88) { g.fillText(line, 44, y); y += lh; line = ''; } line += w + ' '; });
      g.fillText(line, 44, y); y += lh + (i === 0 ? 6 : 2);
    });
  }

  // ---------- analysis ----------
  const tr = (s) => s.toLocaleLowerCase('tr-TR');
  const SECTIONS = [
    { k: 'deneyim', n: 'Deneyim', re: /(iş\s*deneyim|deneyim|tecrübe|experience|employment|work history|çalışma geçmişi)/, need: true },
    { k: 'egitim', n: 'Eğitim', re: /(eğitim|öğrenim|education|academic)/, need: true },
    { k: 'yetenek', n: 'Yetenekler', re: /(yetenek|beceri|yetkinlik|skills|competenc|teknik bilgi|bilgisayar bilgisi)/, need: true },
    { k: 'profil', n: 'Profil özeti', re: /(profil|özet|hakkımda|kariyer hedefi|summary|profile|objective|about me)/, need: true },
    { k: 'dil', n: 'Diller', re: /(yabancı dil|diller|languages)/ },
    { k: 'sertifika', n: 'Sertifika ve kurslar', re: /(sertifika|kurs|certificat|courses|eğitimler ve)/ },
  ];
  const VERBS = ['yönettim', 'geliştirdim', 'artırdım', 'arttırdım', 'azalttım', 'kurdum', 'tasarladım', 'yürüttüm', 'hazırladım', 'sundum', 'tamamladım', 'koordine ettim', 'analiz ettim', 'uyguladım', 'oluşturdum', 'sağladım', 'düşürdüm', 'kazandırdım', 'eğittim', 'raporladım', 'planladım', 'optimize ettim', 'başlattım', 'liderlik ettim', 'iyileştirdim',
    'managed', 'led', 'built', 'developed', 'increased', 'reduced', 'designed', 'launched', 'delivered', 'improved', 'created', 'implemented', 'achieved', 'grew', 'drove', 'analyzed', 'coordinated', 'trained'];
  const CLICHES = ['takım oyuncusu', 'takım çalışmasına yatkın', 'öğrenmeye açık', 'sonuç odaklı', 'dinamik', 'yenilikçi', 'çözüm odaklı', 'kendimi geliştirebileceğim', 'detaycı', 'sorumluluk sahibi', 'iletişimi güçlü', 'hard working', 'team player', 'detail oriented', 'results driven', 'fast learner'];
  const STOP = new Set(('ve veya ile için bir bu şu o da de mi mı mu mü gibi daha çok en ya ki ne olan olarak ait göre kadar her tüm ise veya ancak ama fakat hem ayrıca üzere tercihen aranan aranıyor aranmaktadır bilen adaylar adayların tercihen uzmanı elemanı personeli sahip olmak olması gereken iyi derecede konusunda alanında bilgi bilgisi deneyim deneyimi deneyimli tecrübe yıl yıllık en az iş pozisyon pozisyonu firma şirket şirketimiz ekip ekibimiz arkadaşı arkadaşları çalışma çalışacak görev görevi tanımı nitelikler genel başvuru aday adaylar mezun mezunu bölümü bölümlerinden üniversite üniversitelerin tercih sebebi olan yapabilecek edebilecek olabilecek the and for with our you your are will have has that this from who all can able years experience work team role job strong good knowledge skills required preferred including such other must should').split(' '));

  function analyze(doc, file, jobText) {
    const text = doc.text, low = tr(text), words = text.split(/\s+/).filter(Boolean), wc = words.length;
    const F = []; const add = (cat, st, t, d) => F.push({ cat, st, t, d });
    const cats = {};

    // 1. machine readability (30)
    let r = 30;
    const imageOnly = wc < 30;
    if (imageOnly) { r = 2; add('okuma', 'bad', 'Metin okunamıyor', 'Dosyandan neredeyse hiç metin çıkmadı. CV büyük olasılıkla resim olarak kaydedilmiş (taranmış ya da tasarım aracından görsel olarak dışa aktarılmış). Başvuru yazılımları bu dosyayı boş görür. Word ya da Google Dokümanlar\'da yazıp "PDF olarak kaydet" ile yeniden oluştur.'); }
    else {
      add('okuma', 'ok', 'Metin katmanı okunuyor', `Dosyandan ${wc.toLocaleString('tr-TR')} kelime çıkarıldı; yazılımlar içeriği metin olarak görebilir.`);
      if (doc.columns) { r -= 9; add('okuma', 'warn', 'Çok sütunlu düzen', 'Sayfada yan yana iki metin sütunu algılandı. Bazı başvuru yazılımları sütunları soldan sağa tek satır gibi okuyup bilgileri karıştırır. Tek sütunlu düzene geç.'); }
      else add('okuma', 'ok', 'Tek sütunlu akış', 'Metin yukarıdan aşağı tek akışta ilerliyor; yazılımların en rahat okuduğu düzen.');
      if (doc.tables) { r -= 6; add('okuma', 'warn', 'Tablo kullanılmış', 'Belgede tablo var. Tablo içindeki bilgi bazı sistemlerde atlanır ya da sırası bozulur. Deneyim ve eğitimi düz paragraf ve madde işaretiyle yaz.'); }
      if (doc.textbox) { r -= 6; add('okuma', 'warn', 'Metin kutusu kullanılmış', 'Metin kutularının içindeki yazı birçok sistemde okunmaz. İçeriği normal paragrafa taşı.'); }
      if (doc.images > 3) { r -= 4; add('okuma', 'warn', 'Çok sayıda görsel öğe', `${doc.images} görsel öğe bulundu. Simge, çubuk grafik ve yıldızlı beceri göstergeleri yazılımlar için anlamsızdır; beceriyi kelimeyle yaz.`); }
      const odd = (text.match(/[�-]/g) || []).length;
      if (odd > 8) { r -= 6; add('okuma', 'warn', 'Okunamayan karakterler', 'Metinde tanınmayan karakterler var; özel simge yazı tipleri ya da ikonlar metne karışmış. Standart bir yazı tipi (Arial, Calibri, Helvetica) kullan.'); }
      if (doc.kind === 'pdf' && doc.fonts > 6) { r -= 2; add('okuma', 'warn', 'Çok fazla yazı tipi', `${doc.fonts} farklı yazı tipi algılandı. Bir ya da iki yazı tipiyle sınırla.`); }
    }
    cats.okuma = Math.max(0, r);

    // 2. sections (20)
    const heads = doc.lines.filter((l) => l.length < 42).map(tr);
    let s = 0; const missing = [];
    SECTIONS.forEach((sec) => {
      const inHead = heads.some((h) => sec.re.test(h)), inText = sec.re.test(low);
      if (inHead) { s += sec.need ? 4.5 : 1; }
      else if (inText) { s += sec.need ? 2.5 : 0.5; if (sec.need) add('bolum', 'warn', `"${sec.n}" başlığı net değil`, `İçerikte geçiyor ama ayrı bir başlık olarak algılanmadı. Başlığı tek başına bir satıra, standart adıyla yaz ("${sec.n}").`); }
      else if (sec.need) { missing.push(sec.n); }
    });
    if (missing.length && !imageOnly) add('bolum', 'bad', 'Eksik bölüm: ' + missing.join(', '), 'Yazılımlar ve işe alımcılar bu bölümleri standart başlıklarla arar. Eksik olanları ekle.');
    else if (!imageOnly) add('bolum', 'ok', 'Temel bölümler yerinde', 'Profil, deneyim, eğitim ve yetenek bölümleri bulundu.');
    cats.bolum = imageOnly ? 0 : Math.min(20, Math.round(s));

    // 3. contact (15)
    let c = 0;
    const email = text.match(/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/);
    const phone = text.match(/(\+?90|0)?\s*\(?5\d{2}\)?[\s.-]?\d{3}[\s.-]?\d{2}[\s.-]?\d{2}|\+\d{1,3}[\s.-]?\d{2,4}[\s.-]?\d{3}[\s.-]?\d{2,4}/);
    const linkedin = /linkedin\.com\/|linkedin/i.test(text);
    if (email) { c += 6; if (/(hotmail|yahoo|mynet|windowslive)/i.test(email[0]) || /\d{4,}|prenses|kral|tatli|crazy|cool|baby/i.test(email[0].split('@')[0])) add('iletisim', 'warn', 'E-posta adresini gözden geçir', 'Adın ve soyadından oluşan sade bir adres (ad.soyad@...) daha profesyonel durur.'); else add('iletisim', 'ok', 'E-posta adresi var', 'İletişim e-postan okunuyor.'); }
    else if (!imageOnly) add('iletisim', 'bad', 'E-posta adresi bulunamadı', 'E-postanı üst bölüme, düz metin olarak yaz. Üst bilgi/alt bilgi alanına ya da görsele yazılan iletişim bilgisi okunmayabilir.');
    if (phone) { c += 5; if (!imageOnly) add('iletisim', 'ok', 'Telefon numarası var', 'Telefon numaran okunuyor.'); } else if (!imageOnly) add('iletisim', 'bad', 'Telefon numarası bulunamadı', 'Cep telefonunu üst bölüme düz metin olarak ekle.');
    if (linkedin) { c += 4; } else if (!imageOnly) add('iletisim', 'warn', 'LinkedIn bağlantısı yok', 'Güncel bir LinkedIn profilin varsa adresini ekle; işe alımcıların çoğu bakar.');
    if (/\b[1-9]\d{10}\b/.test(text.replace(/[\s.-]/g, ' ')) && /(t\.?c\.?|kimlik)/i.test(text)) { c -= 3; add('iletisim', 'bad', 'Kimlik numarası yazılmış', 'T.C. kimlik numaranı CV\'den çıkar. Başvuruda gerekmez ve kişisel veri riski oluşturur.'); }
    if (/(medeni (hal|durum)|doğum yeri|kan grubu|askerlik durumu|uyruk|din[iİ]? )/i.test(text)) add('iletisim', 'warn', 'Gereksiz kişisel bilgiler', 'Medeni durum, doğum yeri, kan grubu gibi bilgiler değerlendirmeye katkı sağlamaz. İlan özellikle istemiyorsa çıkar.');
    cats.iletisim = Math.max(0, Math.min(15, c + (c > 0 ? 0 : 0)));

    // 4. content strength (25)
    let g = 0;
    const metrics = (text.match(/(%\s?\d+|\d+\s?%|yüzde\s+\d+|\d[\d.,]*\s?(tl|₺|usd|\$|€|eur|bin|milyon|kişi|müşteri|proje|kişilik|adet|saat|gün|ay)\b)/gi) || []).length;
    const verbs = VERBS.filter((v) => low.includes(v)).length;
    const bullets = doc.lines.filter((l) => /^[•●▪■◦\-–*·]/.test(l.trim())).length;
    const dates = (text.match(/\b(19|20)\d{2}\b/g) || []).length;
    const cl = CLICHES.filter((x) => low.includes(x));
    if (!imageOnly) {
      if (metrics >= 5) { g += 9; add('icerik', 'ok', 'Rakamla desteklenmiş başarılar', `${metrics} sayısal ifade bulundu. Sonuçlarını rakamla göstermen güçlü bir işaret.`); }
      else if (metrics >= 2) { g += 5; add('icerik', 'warn', 'Daha fazla rakam ekle', `Yalnızca ${metrics} sayısal ifade bulundu. Her görev için en az bir sonucu rakamla yaz: kaç müşteri, yüzde kaç artış, kaç kişilik ekip, ne kadar süre.`); }
      else { add('icerik', 'bad', 'Başarılar rakamsız', 'CV\'de ölçülebilir sonuç neredeyse yok. "Satışları artırdım" yerine "Satışları bir yılda yüzde 18 artırdım" yaz; fark burada oluşur.'); }
      if (verbs >= 6) { g += 7; add('icerik', 'ok', 'Güçlü eylem fiilleri', `${verbs} farklı eylem fiili kullanılmış (yönettim, geliştirdim gibi).`); }
      else if (verbs >= 3) { g += 4; add('icerik', 'warn', 'Eylem fiillerini çeşitlendir', 'Maddeleri "sorumluydum" yerine yaptığın işi anlatan fiillerle başlat: yönettim, kurdum, azalttım, hazırladım.'); }
      else add('icerik', 'bad', 'Görev tanımı gibi yazılmış', 'Maddeler ne yaptığını değil, görev tanımını anlatıyor. Her maddeyi bir eylem fiiliyle başlat ve sonucu ekle.');
      if (bullets >= 6 || (verbs >= 5 && doc.lines.length >= 14)) g += 4; else if (bullets >= 3 || verbs >= 3) g += 2; else add('icerik', 'warn', 'Madde işareti az', 'Deneyimlerini uzun paragraf yerine 3-5 kısa maddeyle yaz; hem yazılım hem insan daha rahat okur.');
      if (dates >= 4) g += 5; else if (dates >= 2) { g += 3; } else add('icerik', 'bad', 'Tarihler eksik', 'İş ve eğitim kayıtlarında başlangıç ve bitiş tarihleri bulunamadı. "Eki 2022 – Bugün" biçiminde ay ve yıl yaz.');
      if (cl.length >= 3) { g -= 3; add('icerik', 'warn', 'Kanıtsız sıfatlar', `Şu ifadeler tek başına bir şey kanıtlamaz: ${cl.slice(0, 4).join(', ')}. Yerine bunu gösteren somut bir örnek yaz.`); }
    }
    cats.icerik = Math.max(0, Math.min(25, g));

    // 5. length (10)
    let l = 0;
    if (!imageOnly) {
      if (wc >= 250 && wc <= 850) { l += 6; add('uzunluk', 'ok', 'Uzunluk dengeli', `${wc.toLocaleString('tr-TR')} kelime; okunabilir bir uzunluk.`); }
      else if (wc < 250) { l += 2; add('uzunluk', 'warn', 'CV çok kısa', `${wc} kelime var. Deneyim ve projelerini biraz daha açarak 300-700 kelime aralığına getir.`); }
      else { l += 3; add('uzunluk', 'warn', 'CV çok uzun', `${wc.toLocaleString('tr-TR')} kelime var. İşe alımcı ilk bakışta saniyeler ayırır; son 10 yıla ve ilanla ilgili işlere odaklan.`); }
      if (doc.pages <= 2) l += 4; else { l += 1; add('uzunluk', 'warn', `${doc.pages} sayfa`, 'İki sayfayı geçmemeye çalış. Yeni mezunsan tek sayfa yeter.'); }
      if (file.size > 2 * 1024 * 1024) add('uzunluk', 'warn', 'Dosya boyutu büyük', `${(file.size / 1048576).toFixed(1)} MB. Bazı başvuru formları 2 MB üstünü kabul etmez; görselleri çıkar ya da küçült.`);
    }
    cats.uzunluk = l;

    // job match (optional, reported separately)
    let match = null;
    const jt = jobText.trim();
    if (jt.length > 80 && !imageOnly) {
      const freq = new Map();
      tr(jt).replace(/[^a-zçğıöşü0-9+#.\s-]/g, ' ').split(/\s+/).forEach((w) => { w = w.replace(/^[.-]+|[.-]+$/g, ''); if (w.length < 3 || STOP.has(w) || /^\d+$/.test(w)) return; freq.set(w, (freq.get(w) || 0) + 1); });
      const stem = (w) => w.length > 6 ? w.slice(0, Math.max(5, w.length - 3)) : w.length > 4 ? w.slice(0, 4) : w;
      const seen = new Set(); const keys = [];
      [...freq.entries()].sort((a, b) => b[1] - a[1] || b[0].length - a[0].length).forEach(([w]) => { const st = stem(w); if (seen.has(st) || keys.length >= 16) return; seen.add(st); keys.push(w); });
      const found = keys.filter((k) => low.includes(stem(k))), miss = keys.filter((k) => !low.includes(stem(k)));
      match = { pct: keys.length ? Math.round(found.length / keys.length * 100) : 0, found, miss };
    }

    if (!imageOnly && wc < 120) { cats.uzunluk = 0; cats.icerik = Math.min(cats.icerik, 8); cats.bolum = Math.min(cats.bolum, 12); }
    const total = Math.round(cats.okuma + cats.bolum + cats.iletisim + cats.icerik + cats.uzunluk);
    return { total, cats, F, match, wc, pages: doc.pages, kind: doc.kind, imageOnly };
  }

  // ---------- render ----------
  const CATS = [['okuma', 'Yazılım okunabilirliği', 30], ['bolum', 'Bölümler ve başlıklar', 20], ['iletisim', 'İletişim bilgileri', 15], ['icerik', 'İçerik gücü', 25], ['uzunluk', 'Uzunluk ve dosya', 10]];
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const ICON = { ok: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>', warn: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7v6M12 17h.01"/></svg>', bad: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 7l10 10M17 7L7 17"/></svg>' };

  function render(res, file) {
    const t = res.total;
    const lvl = t >= 85 ? ['good', 'Güçlü', 'CV\'n yazılımlar tarafından rahat okunuyor ve içeriği sağlam. Küçük dokunuşlarla daha da iyi olur.']
      : t >= 65 ? ['mid', 'İyi, ama geliştirilebilir', 'Temel yapı yerinde. Aşağıdaki maddeleri düzeltirsen geri dönüş alma ihtimalin artar.']
      : t >= 40 ? ['low', 'Riskli', 'CV\'n bazı sistemlerde eksik okunabilir ve içerik işe alımcıyı ikna etmekte zorlanabilir.']
      : ['bad', 'Büyük ihtimalle eleniyor', 'Bu haliyle CV\'n başvuru yazılımlarında ciddi sorun yaşar. Önce aşağıdaki kırmızı maddeleri çöz.'];
    const order = { bad: 0, warn: 1, ok: 2 };
    const todo = res.F.filter((f) => f.st !== 'ok').sort((a, b) => order[a.st] - order[b.st]);
    const good = res.F.filter((f) => f.st === 'ok');
    const bars = CATS.map(([k, n, max]) => { const v = res.cats[k], p = Math.round(v / max * 100); return `<li><span>${n}</span><b>${Math.round(v)}<i>/${max}</i></b><em class="${p >= 80 ? 'good' : p >= 55 ? 'mid' : 'low'}"><u style="--w:${p}%"></u></em></li>`; }).join('');
    const item = (f) => `<li class="${f.st}"><span class="ic">${ICON[f.st]}</span><div><b>${esc(f.t)}</b><p>${esc(f.d)}</p></div></li>`;
    const m = res.match;
    const matchHtml = m ? `<div class="cva-match"><div class="cva-mh"><div><span class="eyebrow">İlan uyumu</span><h3>İlandaki anahtar kelimelerin ne kadarı CV'nde geçiyor?</h3></div><b class="${m.pct >= 70 ? 'good' : m.pct >= 45 ? 'mid' : 'low'}">%${m.pct}</b></div>
      ${m.miss.length ? `<p>CV'nde bulunmayan kelimeler. Gerçekten sahip olduğun beceri ve deneyimleri ilandaki kelimeyle yaz:</p><ul class="cva-kw miss">${m.miss.map((k) => `<li>${esc(k)}</li>`).join('')}</ul>` : ''}
      ${m.found.length ? `<p>Bulunanlar:</p><ul class="cva-kw">${m.found.map((k) => `<li>${esc(k)}</li>`).join('')}</ul>` : ''}</div>` : '';
    const msg = encodeURIComponent(`Merhaba, sitenizde CV analizi yaptım, puanım ${t}/100 çıktı. CV'mi düzeltmek için yardım almak istiyorum.`);
    out.innerHTML = `
      <div class="cva-top ${lvl[0]}">
        <div class="cva-ring" style="--p:0" data-p="${t}"><svg viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="60" r="52"/><circle class="v" cx="60" cy="60" r="52"/></svg><b>0</b><i>/ 100</i></div>
        <div class="cva-sum"><span class="eyebrow">CV analiz raporu</span><h3>${lvl[1]}</h3><p>${lvl[2]}</p>
          <p class="cva-meta">${esc(file.name)} · ${res.kind === 'pdf' ? 'PDF' : 'Word'} · ${res.pages} sayfa · ${res.wc.toLocaleString('tr-TR')} kelime</p></div>
        <ul class="cva-bars">${bars}</ul>
      </div>
      ${matchHtml}
      <div class="cva-cols">
        <div><h4>Düzeltilecekler <small>${todo.length}</small></h4><ul class="cva-list">${todo.length ? todo.map(item).join('') : '<li class="ok"><span class="ic">' + ICON.ok + '</span><div><b>Düzeltilecek önemli bir şey bulunamadı</b><p>Otomatik kontrolde sorun çıkmadı.</p></div></li>'}</ul></div>
        <div><h4>İyi olanlar <small>${good.length}</small></h4><ul class="cva-list">${good.map(item).join('')}</ul></div>
      </div>
      <div class="cva-cta"><div><h3>${t >= 85 ? 'Son rötuşu birlikte yapalım mı?' : 'Bu maddeleri senin yerine biz düzeltelim.'}</h3><p>Raporu WhatsApp'tan gönder; CV'ni yazılımların okuyacağı düzene çevirelim, başarılarını rakamla yazalım. CV Oluşturma 250 ₺, tek seferlik.</p></div>
        <div class="cva-btns"><a class="btn btn-gold js-wa" href="${WA}${msg}" target="_blank" rel="noopener">Raporumu gönder, destek al</a><a class="btn btn-line" href="cv-hazirlama.html#paketler">Paketleri gör</a><button type="button" class="btn btn-ghost cva-again">Başka bir CV tara</button></div></div>
      <p class="cva-note">Bu rapor otomatik bir ön kontroldür: dosyanın yapısına ve metnine bakar, belirli bir şirketin başvuru sistemini birebir taklit etmez. Dosyan tarayıcında incelendi; hiçbir sunucuya gönderilmedi ve saklanmadı.</p>`;
    out.hidden = false;
    const ring = out.querySelector('.cva-ring'), num = ring.querySelector('b'), start = performance.now();
    const rm = matchMedia('(prefers-reduced-motion: reduce)').matches;
    (function tick(now) { const k = rm ? 1 : Math.min(1, (now - start) / 1400), e = 1 - Math.pow(1 - k, 3), v = Math.round(t * e); ring.style.setProperty('--p', v); num.textContent = v; if (k < 1) requestAnimationFrame(tick); })(start);
    requestAnimationFrame(() => out.classList.add('in'));
    out.scrollIntoView({ behavior: rm ? 'auto' : 'smooth', block: 'start' });
  }
}
