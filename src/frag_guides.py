# ---------- SEO guides ----------
GUIDE_DATE = "2026-10-23"

def gtable(head, rows):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="gt"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def gnote(title, text, href="#iletisim", cta="Ücretsiz ön görüşme al"):
    return f'<aside class="gnote"><b>{title}</b><p>{text}</p><a class="btn btn-gold" href="{href}">{cta}</a></aside>'

GUIDES = [
 dict(slug="web-sitesi-yaptirmak.html", kw="web sitesi yaptırmak",
  title="Web Sitesi Yaptırmak 2026: Fiyatlar, Süreç ve Dikkat Edilecekler | Laurus Dijital",
  desc="2026'da web sitesi yaptırmak ne kadar tutar, kaç günde biter, nelere dikkat etmelisin? Site türlerine göre fiyat tablosu, gizli maliyetler ve teklif kontrol listesi.",
  h1="Web sitesi yaptırmak: 2026 fiyatları ve süreç rehberi",
  lead="Web sitesi yaptırmak isteyen işletmelerin en çok sorduğu üç soru: ne kadar tutar, ne kadar sürer, kime yaptırmalıyım? Bu rehberde üçünü de açık rakamlarla anlatıyoruz.",
  photo="tasarim-laptop", read="9 dk",
  related=["web-tasarim.html","seo-hizmeti.html","sosyal-medya-yonetimi-fiyatlari.html"],
  sections=[
   ("ozet","Kısaca: ne kadar tutar?", f"""<p>Fiyatı belirleyen asıl şey sitenin <b>türü</b> ve <b>sayfa sayısı</b>. 2026'da Türkiye'de küçük işletmelerin en sık yaptırdığı üç site türü ve piyasada sık görülen fiyat aralıkları şöyle:</p>
{gtable(["Site türü","Kime uygun","Piyasa aralığı","Laurus fiyatı"],[["Tek sayfa site","Kuaför, kafe, klinik, yeni açılan işletme","8.000 – 25.000 ₺","<b>12.000 ₺</b>"],["Kurumsal site (5 sayfa)","Hizmetlerini ayrı ayrı anlatmak isteyen işletme","25.000 – 75.000 ₺","<b>22.000 ₺</b>"],["Satış (e-ticaret) sitesi","Online ürün satan butik ve mağaza","40.000 – 120.000 ₺","<b>35.000 ₺</b>"],["Site bakımı","Güncelleme, yedek, küçük değişiklik","Aylık 1.000 – 5.000 ₺","<b>1.500 ₺ / ay</b>"]])}
<p>Piyasa aralıkları freelancer ve ajans teklifleri arasındaki farkı gösterir; aynı iş için 3 kat fiyat farkı görmek normaldir. Farkı kapsam, tasarımın özgünlüğü ve teslimden sonra kimin ilgilendiği yaratır.</p>"""),
   ("turler","Hangi site türü sana uygun?", """<h3>Tek sayfa site</h3><p>Ne yaptığını, fiyatlarını, adresini ve iletişim yolunu tek sayfada anlatır. Randevuyla çalışan işletmeler için çoğu zaman yeterlidir: kuaför, güzellik salonu, pet kuaför, kafe, muayenehane. Telefonda hızlı açılır, Google'a tek, güçlü bir sayfa verir.</p>
<h3>Kurumsal site</h3><p>Hizmetlerin birbirinden farklıysa ve her birini ayrı aratmak istiyorsan (örneğin “implant”, “ortodonti”, “diş beyazlatma”) her hizmete ayrı sayfa açmak gerekir. Google her sayfayı ayrı bir aramada gösterebilir; bu yüzden kurumsal site SEO için daha fazla kapı açar.</p>
<h3>Satış sitesi</h3><p>Ürün kataloğu, sepet, online ödeme ve sipariş paneli içerir. Instagram'dan DM ile satış yapan butikler için en büyük kazanç, fiyat ve stok sorularının bitmesi ve ödemenin anında alınmasıdır.</p>"""),
   ("etkenler","Fiyatı belirleyen 6 şey", """<ol class="gl"><li><b>Sayfa sayısı.</b> Her ek sayfa yeni metin, tasarım ve SEO işi demektir.</li><li><b>Hazır tema mı, özgün tasarım mı?</b> Hazır tema ucuzdur ama rakibinle aynı görünebilirsin.</li><li><b>Metinleri kim yazıyor?</b> Metin yazımı çoğu teklifte ayrı ücretlendirilir. Bizde dahil.</li><li><b>Fotoğraf.</b> Telefonla çekilen iyi fotoğraflar çoğu zaman yeter; profesyonel çekim günü ayrı bir kalemdir.</li><li><b>Entegrasyonlar.</b> Online ödeme, randevu sistemi, kargo, pazar yeri bağlantısı fiyatı artırır.</li><li><b>SEO altyapısı.</b> Başlıklar, açıklamalar, hız, Google'ın okuduğu yapısal veri. Ucuz tekliflerde genelde eksik kalır.</li></ol>"""),
   ("gizli","Gizli maliyetler: teklifte sorman gerekenler", f"""<p>Teklif ucuz görünüp sonradan pahalıya patlayan kalemler genelde şunlardır:</p>
{gtable(["Kalem","Yaklaşık maliyet","Not"],[["Alan adı (.com / .com.tr)","Yıllık 500 – 1.200 ₺","Mutlaka <b>senin adına</b> alınmalı"],["Barındırma (hosting)","Yıllık 0 – 3.000 ₺","Basit siteler ücretsiz katmanlarda çalışabilir"],["SSL (https)","Çoğu zaman ücretsiz","Ücret isteniyorsa sor"],["Bakım ve güncelleme","Aylık 1.000 – 5.000 ₺","İstersen kendin de güncelleyebilmelisin"],["Ek düzeltme turları","Saatlik ya da adetle","Teklifte kaç tur olduğu yazmalı"]])}
<p>Laurus'ta alan adının ilk yılı fiyata dahildir, siteyi ücretsiz katmanda yayınlarız ve iki düzeltme turu her işe dahildir.</p>"""),
   ("surec","Süreç: ilk görüşmeden yayına", """<ol class="gl"><li><b>Tanışma (1. gün).</b> İşletmeni, müşterini ve hedefini konuşuruz; varsa mevcut hesaplarına bakarız.</li><li><b>İlk taslak (2–3. gün).</b> Ana sayfanın taslağını görürsün. Beğenmezsen ödeme yapmazsın.</li><li><b>Tamamlama (4–6. gün).</b> Metinler, fotoğraflar, Google İşletme Profili ve iki düzeltme turu.</li><li><b>Yayın (7. gün).</b> Site açılır, Google Search Console'a eklenir, nasıl güncelleyeceğin anlatılır.</li></ol>"""),
   ("kontrol","Teklif alırken kontrol listesi", """<ul class="gc"><li>Alan adı ve tüm hesaplar senin adına mı açılacak?</li><li>Site telefonda nasıl görünecek, örnek gösterebiliyorlar mı?</li><li>Metinleri kim yazıyor, kaç düzeltme turu var?</li><li>SEO altyapısı (başlık, açıklama, site haritası, Search Console) dahil mi?</li><li>Teslimden sonra sorun çıkarsa kime ulaşacaksın?</li><li>Toplam ilk yıl maliyeti (site + alan adı + barındırma + bakım) ne kadar?</li></ul>"""),
  ],
  faq=[("Web sitesi yaptırmak kaç günde biter?","Tek sayfa bir site genelde 7 günde, 5 sayfalık kurumsal site 2–3 haftada, satış sitesi 3–5 haftada yayına girer. Süreyi en çok metin ve fotoğrafların hazır olması belirler."),
       ("Hazır site yapıcı (Wix vb.) mı, yaptırmak mı?","Site yapıcılar ucuz başlar ama aylık ücretleri birikir, tasarım ve hız sınırlıdır ve hesabı bırakırsan site gider. Yaptırdığın site ve alan adı tamamen senin olur."),
       ("Instagram hesabım varken web sitesine ihtiyacım var mı?","Google'da arama yapan biri Instagram profilini değil, siteleri ve haritayı görür. Site, Google'ın seni tanıması ve aramalarda çıkman için gereklidir; Instagram ise vitrin olarak birlikte çalışır."),
       ("Siteyi sonradan kendim güncelleyebilir miyim?","Evet. Fiyat ve saat gibi sık değişen bilgileri nasıl güncelleyeceğini gösteririz. İstersen aylık bakım paketiyle biz yaparız.")]),

 dict(slug="sosyal-medya-yonetimi-fiyatlari.html", kw="sosyal medya yönetimi fiyatları",
  title="Sosyal Medya Yönetimi Fiyatları 2026: Instagram Hesap Yönetimi Ne Kadar? | Laurus Dijital",
  desc="Sosyal medya yönetimi ve Instagram hesap yönetimi 2026 fiyatları: freelancer ve ajans farkı, pakete neler dahil, reklam bütçesi ayrı mı? Açık fiyat tablosu ve kontrol listesi.",
  h1="Sosyal medya yönetimi fiyatları 2026",
  lead="Instagram hesabını birine devretmeden önce bilmen gerekenler: aylık ne kadar ödenir, pakete neler girer, hangi kalemler ayrıdır. Rakamlarla, sade bir dille.",
  photo="telefon-instagram", read="8 dk",
  related=["sosyal-medya.html","reklam-yonetimi.html","web-sitesi-yaptirmak.html"],
  sections=[
   ("ozet","Kısaca: aylık ne kadar?", f"""<p>Sosyal medya yönetimi aylık ücretle çalışır. Fiyatı en çok <b>paylaşım sayısı</b>, <b>video (Reels) üretimi</b> ve <b>mesaj yönetimi</b> belirler. 2026'da Türkiye'de sık görülen aralıklar:</p>
{gtable(["Kim yapıyor","Aylık piyasa aralığı","Not"],[["Yeni başlayan freelancer","5.000 – 12.000 ₺","Genelde sadece tasarım ve paylaşım"],["Deneyimli freelancer","12.000 – 25.000 ₺","Plan ve basit rapor eklenir"],["Butik ajans","20.000 – 45.000 ₺","Strateji, Reels, mesaj yönetimi, rapor"],["Orta ve büyük ajans","40.000 ₺ ve üzeri","Ekip, çekim günleri, çoklu platform"]])}
<p>Laurus'ta iki paket var: <b>Başlangıç 12.000 ₺/ay</b> (Instagram, ayda 8 gönderi ve 8 hikâye, aylık rapor) ve <b>Büyüme 20.000 ₺/ay</b> (Instagram + TikTok ya da Google profili, ayda 12 gönderi ve 4 Reels, yorum ve mesaj yönetimi).</p>"""),
   ("dahil","Pakete neler dahil olmalı?", """<ul class="gc"><li><b>Aylık içerik planı:</b> hangi gün ne paylaşılacağını ayın başında görmelisin.</li><li><b>Tasarım ve metin:</b> gönderi, hikâye ve kapak tasarımları, açıklamalar.</li><li><b>Reels:</b> kısa videolar bugün en çok erişim alan içerik türü; kaç adet olduğu yazmalı.</li><li><b>Yorum ve mesaj yönetimi:</b> gelen soruların yanıtlanması, randevu taleplerinin sana iletilmesi.</li><li><b>Aylık rapor:</b> kaç kişi gördü, kaç mesaj geldi, hangi içerik işe yaradı.</li></ul>"""),
   ("ayri","Fiyata dahil olmayanlar", f"""{gtable(["Kalem","Yaklaşık maliyet","Not"],[["Reklam bütçesi","Aylık 3.000 ₺'den başlar","Google ve Meta'ya doğrudan senin kartından ödenir"],["Reklam yönetimi","Aylık 5.000 – 20.000 ₺ ya da bütçenin %15–25'i","Bizde sosyal medya paketine eklenirse 7.500 ₺/ay"],["Profesyonel çekim günü","8.000 – 25.000 ₺","Çoğu küçük işletmede telefon çekimi yeter"]])}"""),
   ("secim","Freelancer mı, ajans mı?", """<p>Freelancer daha ucuzdur ama tek kişiye bağlı kalırsın; hastalık, tatil ya da iş yükü hesabının boş kalmasına yol açabilir. Ajans daha pahalıdır ama süreklilik ve ekip sağlar. Karar verirken şu soruya bak: <b>hesabım hiçbir hafta boş kalmayacak mı ve sonuçları her ay görebilecek miyim?</b></p>"""),
   ("kontrol","Sözleşmeden önce sor", """<ul class="gc"><li>Instagram şifremi vermem gerekiyor mu? (Gerekmez; Meta İşletme Hesabı üzerinden yetki verilir.)</li><li>Paylaşımları onaylamadan yayınlıyor musunuz?</li><li>Takipçi satın alıyor musunuz? (Almamalı; hesabına zarar verir.)</li><li>Sözleşme kaç ay, erken bırakırsam ne olur?</li><li>Reklam bütçesi ve yönetim ücreti ayrı ayrı yazıyor mu?</li></ul>"""),
  ],
  faq=[("Aylık 10.000 ₺ ile sosyal medya yönetimi olur mu?","Tek platformda, ayda 8 civarı paylaşım ve temel raporla olabilir. Reels ve mesaj yönetimi istiyorsan bütçe genelde 15.000 – 20.000 ₺ bandına çıkar."),
       ("Reklam bütçesi sosyal medya ücretine dahil mi?","Hayır. Reklam bütçesi Meta ve Google'a doğrudan ödenir. Ajans yalnızca yönetim ücreti alır; harcanan her kuruşu reklam panelinde görmelisin."),
       ("Sonuçlar ne zaman görülür?","Düzenli paylaşımın etkisi genelde 2–3 ayda belirginleşir. Reklam eklenirse ilk mesajlar ilk haftada gelebilir. Garanti veren ajanslara dikkat et."),
       ("Kaç ay sözleşme yapmalıyım?","Bizde aylık paketlerde ilk 3 ay sabit, sonra istediğin ay bırakabilirsin. Daha uzun bağlayıcı sözleşmelerde çıkış koşullarını mutlaka oku.")]),

 dict(slug="seo-hizmeti.html", kw="seo hizmeti",
  title="SEO Hizmeti: Küçük İşletmeler İçin Google'da Üst Sıralara Çıkma Rehberi | Laurus Dijital",
  desc="Küçük işletmeler için SEO ve yerel SEO: Google'da ve haritada üst sıralara çıkmak için ne yapılır, ne kadar sürer, ne kadar tutar? Adım adım, sade bir rehber.",
  h1="SEO hizmeti: Google'da üst sıralara nasıl çıkılır?",
  lead="SEO, insanlar seni aradığında Google'ın seni önce göstermesi için yapılan işlerin toplamıdır. Küçük bir işletme için en hızlı sonuç çoğu zaman yerel SEO'dan gelir.",
  photo="google-arama", read="8 dk",
  related=["google-isletme.html","web-sitesi-yaptirmak.html","google-reklam-yonetimi.html"],
  sections=[
   ("nedir","SEO nedir, reklamdan farkı ne?", """<p>Google'da arama sonuçlarında iki tür sonuç görürsün: <b>Sponsorlu</b> yazanlar reklamdır, tıklama başına ödenir ve bütçe bitince kaybolur. Altındakiler ise <b>organik</b> sonuçlardır; oraya SEO ile çıkılır ve tıklama başına ödeme yapılmaz. Reklam hızlı sonuç verir, SEO kalıcı sonuç verir. En iyi sonuç ikisi birlikte kullanıldığında alınır.</p>"""),
   ("yerel","Yerel SEO: haritada ilk üçte çıkmak", """<p>“Yakınımdaki kuaför” ya da “Kadıköy diş kliniği” gibi aramalarda Google önce bir harita ve üç işletme gösterir. Bu üçlüye girmek için:</p><ol class="gl"><li><b>Google İşletme Profili'ni eksiksiz doldur:</b> doğru kategori, saatler, hizmet listesi, gerçek fotoğraflar.</li><li><b>Düzenli yorum topla ve yanıtla:</b> memnun müşteriden yorum istemek için hazır bir bağlantı kullan.</li><li><b>Adres ve telefon her yerde aynı olsun:</b> site, profil, sosyal medya ve rehber sitelerinde tek tip bilgi.</li><li><b>Sitende semtini ve hizmetlerini yaz:</b> Google sitende ne yazdığını profille eşleştirir.</li></ol>"""),
   ("site","Site tarafında yapılanlar", f"""{gtable(["Çalışma","Ne işe yarar"],[["Sayfa başlıkları ve açıklamaları","Aramada görünen başlık ve metin; tıklanma oranını belirler"],["Hizmet başına ayrı sayfa","Her hizmetin ayrı aramada çıkabilmesi"],["Hız ve mobil uyum","Google yavaş ve telefonda bozuk siteleri geri iter"],["Yapısal veri (schema)","Google'a adres, saat, fiyat ve SSS bilgisini düzenli verir"],["Site haritası ve Search Console","Sayfaların Google'a bildirilmesi ve hataların takibi"],["Rehber içerikler","Müşterinin sorduğu sorulara yanıt veren yazılar; yeni aramalara kapı açar"]])}"""),
   ("sure","Ne kadar sürer, ne kadar tutar?", """<p>Yeni bir sitenin aramalarda yerleşmesi genelde <b>3–6 ay</b> sürer; rekabetin yüksek olduğu aramalarda daha uzun. Google İşletme Profili düzenlemesi ise çoğu zaman birkaç hafta içinde haritada fark yaratır. Küçük işletmeler için aylık SEO hizmetleri piyasada genelde 8.000 – 30.000 ₺ arasındadır.</p><p>Laurus'ta site kurulumunda temel SEO altyapısı fiyata dahildir; Google İşletme Profili kurulumu Vitrin paketinde yer alır.</p>"""),
   ("dikkat","Dikkat: SEO'da garanti olmaz", """<p>“Bir ayda Google'da birinci sıra garantisi” veren tekliflerden uzak dur. Sıralamayı Google belirler; dürüst bir ajans ne yapacağını, nasıl ölçeceğini ve her ay neyin değiştiğini gösterir.</p>"""),
  ],
  faq=[("SEO kendim yapabilir miyim?","Google İşletme Profili'ni doldurmak ve yorum toplamak gibi işleri kendin yapabilirsin. Site tarafındaki teknik altyapı ve içerik planı için destek almak zaman kazandırır."),
       ("SEO mu, Google reklamı mı?","Hemen müşteri istiyorsan reklam, kalıcı görünürlük istiyorsan SEO. Yeni açılan bir işletmeye ilk aylarda ikisini birlikte öneriyoruz."),
       ("Yorum satın almak işe yarar mı?","Hayır. Sahte yorumlar Google kurallarına aykırıdır ve profilin askıya alınabilir. Gerçek müşteriden yorum istemenin kolay yollarını kurarız.")]),

 dict(slug="google-reklam-yonetimi.html", kw="google reklam yönetimi",
  title="Google Reklam Yönetimi 2026: Bütçe, Ücret ve Doğru Kurulum | Laurus Dijital",
  desc="Google Ads reklam yönetimi 2026: küçük işletme için ne kadar bütçe gerekir, ajans ücreti ne kadar, reklam nasıl kurulmalı? Semte özel arama reklamları için sade rehber.",
  h1="Google reklam yönetimi: bütçe ve ücretler 2026",
  lead="Google reklamı, seni arayan kişinin karşısına aynı gün çıkmanın en hızlı yolu. Doğru kurulmazsa da bütçeyi en hızlı eriten yol. İkisini ayıran şeyleri anlatıyoruz.",
  photo="google-arama", read="7 dk",
  related=["reklam-yonetimi.html","seo-hizmeti.html","sosyal-medya-yonetimi-fiyatlari.html"],
  sections=[
   ("nasil","Google reklamı nasıl çalışır?", """<p>Belirlediğin aramalarda (“kuşadası termal otel”, “ataşehir diş kliniği”) sonuçların en üstünde <b>Sponsorlu</b> etiketiyle görünürsün. Yalnızca biri reklama tıkladığında ödeme yaparsın. Kimin göreceğini semt, saat ve cihaza göre sınırlayabilirsin.</p>"""),
   ("butce","Ne kadar bütçe gerekir?", f"""{gtable(["İşletme tipi","Başlangıç için aylık reklam bütçesi","Not"],[["Mahalle işletmesi (kuaför, kafe)","3.000 – 8.000 ₺","3–5 km çevreyle sınırlı"],["Klinik, avukat, emlak","8.000 – 25.000 ₺","Tıklama maliyeti daha yüksek"],["Otel ve turizm","15.000 ₺ ve üzeri","Sezona göre artırılır"]])}
<p>Bu bütçe Google'a doğrudan senin kartından ödenir. Ajans ücreti ayrıdır; piyasada genelde aylık 5.000 – 20.000 ₺ ya da bütçenin %15–25'i kadardır. Laurus'ta reklam yönetimi <b>9.000 ₺/ay</b>, sosyal medya paketine eklenirse <b>7.500 ₺/ay</b>.</p>"""),
   ("kurulum","Doğru kurulum için 5 şart", """<ol class="gl"><li><b>Doğru anahtar kelimeler:</b> satın alma niyeti taşıyan aramalar (“fiyat”, “randevu”, semt adı).</li><li><b>Negatif kelimeler:</b> “iş ilanı”, “ücretsiz” gibi seni ilgilendirmeyen aramaları dışarıda bırakmak.</li><li><b>Doğru sayfaya yönlendirme:</b> reklam, aranan hizmeti anlatan sayfaya gitmeli.</li><li><b>Dönüşüm takibi:</b> arama, WhatsApp ve form tıklamalarını saymak; neyin işe yaradığını görmek.</li><li><b>Haftalık kontrol:</b> boşa giden aramaları ayıklamak, bütçeyi işe yarayan gruplara kaydırmak.</li></ol>"""),
  ],
  faq=[("Google reklamında en az ne kadar harcamalıyım?","Mahalle ölçeğinde bir işletme aylık 3.000 ₺ civarıyla başlayıp sonuçlara göre artırabilir. Çok düşük bütçede veri birikmez ve sonuç değerlendirilemez."),
       ("Reklam bütçesini ajansa mı ödüyorum?","Hayır, bütçe Google'a doğrudan senin kartından ödenir. Ajansa yalnızca yönetim ücreti ödenir."),
       ("Reklam ne zaman sonuç verir?","Doğru kurulmuş bir arama reklamında ilk aramalar ve mesajlar genelde ilk hafta içinde gelir. İlk ay, en iyi çalışan kelimeleri bulma ayıdır.")]),
]
GMAP = {g["slug"]: g for g in GUIDES}

def guide_page(g):
    toc = "".join(f'<li><a href="#{sid}">{t}</a></li>' for sid,t,_ in g["sections"])
    secs = "".join(f'<section id="{sid}" class="gsec"><h2>{t}</h2>{body}</section>' for sid,t,body in g["sections"])
    rel = "".join(f'<a class="grel" href="{r}">{(GMAP[r]["h1"] if r in GMAP else dict((h,t) for h,_,t,_ in SERVICES).get(r, r))}</a>' for r in g["related"])
    faqs = faq_list(g["faq"])
    mid = gnote("Laurus ile açık fiyat", "Fiyatlarımız sitede yazıyor, teklif beklemene gerek yok. İşletmene bakıp sana uygun paketi aynı gün söyleyelim.")
    body = f'''
<section class="phero ghero" aria-labelledby="h-page"><div class="wrap">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / <a href="rehber.html">Rehber</a> / {g["kw"].capitalize()}</nav>
<h1 id="h-page">{g["h1"]}</h1><p class="lead">{g["lead"]}</p>
<p class="gmeta">Güncelleme: 23 Ekim 2026 · Okuma: {g["read"]} · Laurus Dijital</p></div>
<div class="ph">{img(g["photo"], g["h1"], eager=True)}</div>
</div></section>
<section class="light gbody"><div class="wrap ggrid">
<aside class="gtoc"><b>Bu rehberde</b><ol>{toc}</ol><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme</a></aside>
<article class="gart">{secs}{mid}
<section id="sss" class="gsec"><h2>Sık sorulan sorular</h2>{faqs}</section>
<div class="grels"><b>İlgili sayfalar</b>{rel}</div></article>
</div></section>
{contact()}
'''
    return (g["title"], g["desc"], body)

def page_rehber():
    cards = "".join(f'<a class="rcard" href="{g["slug"]}" data-rv style="--d:{i*80}ms"><div class="ph">{img(g["photo"],"")}</div><div><small>{g["read"]} okuma</small><h3>{g["h1"]}</h3><p>{g["desc"]}</p></div></a>' for i,g in enumerate(GUIDES))
    body = f'''
<section class="phero" aria-labelledby="h-page" style="padding-bottom:40px"><div class="wrap" style="grid-template-columns:1fr">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / Rehber</nav>
<h1 id="h-page">İşletmeler için dijital rehber.</h1>
<p class="lead">Web sitesi, sosyal medya, Google reklamı ve SEO hakkında en çok sorulan sorulara açık rakamlarla yanıt veriyoruz.</p></div></div></section>
<section class="light ksec"><div class="wrap"><div class="rgrid">{cards}</div></div></section>
{contact()}
'''
    return ("Rehber: Web Sitesi, Sosyal Medya, Google Reklam ve SEO | Laurus Dijital","Web sitesi yaptırmak, sosyal medya yönetimi fiyatları, Google reklam bütçesi ve SEO hakkında 2026 rehberleri. Açık fiyatlar ve kontrol listeleri.", body)
