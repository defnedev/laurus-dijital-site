# ===== v20: multi-page cinematic structure =====
PT_NAMES = {"index":"Laurus","hizmetler":"Hizmetler","calismalar":"Çalışmalar","mobil-uygulama":"Uygulamalar","surec":"Süreç","fiyatlar":"Fiyatlar","hakkimizda":"Hakkımızda","iletisim":"İletişim","rehber":"Rehber","web-tasarim":"Web Tasarım","sosyal-medya":"Sosyal Medya","reklam-yonetimi":"Reklam","google-isletme":"Google ve SEO"}

def _words(t):
    out = []; k = 0
    for line in t.split("|"):
        ws = []
        for w in line.split(" "):
            if not w: continue
            ws.append(f'<span class="w"><span style="--k:{k}">{w}</span></span>'); k += 1
        out.append(" ".join(ws))
    return "<br>".join(out)

def cine_hero(crumb, eyebrow, title, lead, imgs, actions="", size="", meta=""):
    n = len(imgs)
    sl = "".join(f'<div class="ch-s" style="--i:{i};animation-name:chf{n};animation-delay:{i*6 - 0.01}s"><img src="img/{s}.webp" alt="" {"" if i==0 else "loading=\"lazy\" "}decoding="async" style="--kx:{(-1)**i*2}%"></div>' for i,s in enumerate(imgs))
    cr = f'<nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / {crumb}</nav>' if crumb else ""
    act = f'<div class="actions ch-act">{actions}</div>' if actions else ""
    dim = " dim" if sum(1 for s in imgs if s.startswith(("app/","real/"))) >= 2 else ""
    lng = " long" if len(title) > 44 else ""
    return f'''<section class="chero {size}{dim}{lng}" aria-labelledby="h-page" style="--n:{n}">
<div class="ch-media" aria-hidden="true">{sl}</div><div class="ch-shade" aria-hidden="true"></div><div class="ch-grain" aria-hidden="true"></div>
<div class="wrap ch-in">{cr}<span class="eyebrow ch-ey">{eyebrow}</span>
<h1 id="h-page" class="ch-h">{_words(title)}</h1>
<p class="lead ch-lead">{lead}</p>{act}{meta}</div>
<a class="h3-scroll ch-scroll" href="#ic" aria-label="Aşağı kaydır"><i></i></a>
</section><span id="ic"></span>'''

def cta_band(title="Sıradaki işletme|seninki olsun.", sub="İlk görüşme ücretsiz. İşletmeni anlat, aynı gün taslağını konuşalım.", photo="is-sahibi"):
    return f'''<section class="ctab" aria-label="Ücretsiz ön görüşme"><div class="ctab-bg" aria-hidden="true"><img src="img/{photo}.webp" alt="" loading="lazy" decoding="async"></div>
<div class="wrap ctab-in" data-rv><span class="eyebrow">Ücretsiz ön görüşme</span><h2>{_words(title)}</h2><p class="lead">{sub}</p>
<div class="actions"><a class="btn btn-gold" href="iletisim.html">Teklif al</a><a class="btn btn-line js-wa" href="https://wa.me/905434309702">WhatsApp'tan yaz</a></div></div></section>'''

def stats_strip():
    st = [("8+","yıllık deneyim"),("5","kendi uygulamamız"),("19 bin+","takipçi: Little Paws"),("7 gün","ilk taslaktan yayına")]
    return '<section class="stats" aria-label="Rakamlarla Laurus"><div class="wrap stats-in">' + "".join(f'<div data-rv style="--d:{i*90}ms"><b>{a}</b><span>{b}</span></div>' for i,(a,b) in enumerate(st)) + '</div></section>'

POS={"app/os-world":"50% 38%",'real/nil-galeri':'50% 75%'}
def explore():
    T = [("hizmetler.html","tasarim-laptop","Hizmetler","Web sitesi, sosyal medya, reklam, SEO ve uygulama.","xbig"),
         ("calismalar.html","real/nil-galeri","Çalışmalar","Gerçek müşteriler, gerçek işler.","xbig"),
         ("mobil-uygulama.html","app/os-world","Uygulamalar","Kendi tasarlayıp kodladığımız beş ürün.",""),
         ("surec.html","planlama","Süreç","İlk görüşmeden yayına yedi gün.",""),
         ("fiyatlar.html","is-sahibi","Fiyatlar","Açık fiyat, sürpriz yok.",""),
         ("hakkimizda.html","cekim","Hakkımızda","8 yılı aşkın deneyim, tek ekip.","")]
    tiles = "".join(f'<a class="xt {c}" href="{h}" data-pt="{t}" data-tilt data-rv style="--d:{i*80}ms"><img src="img/{p}.webp" alt="" loading="lazy" decoding="async"{(" style=\"object-position:"+POS[p]+"\"") if p in POS else ""}><span class="xt-sh" aria-hidden="true"></span><span class="xt-gl" aria-hidden="true"></span><span class="xt-tx"><b>{t}</b><small>{d}</small></span><span class="xt-ar" aria-hidden="true">{I["arrow"]}</span></a>' for i,(h,p,t,d,c) in enumerate(T))
    return f'''<section class="xpl" id="kesfet" aria-labelledby="h-xpl"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Keşfet</span><h2 id="h-xpl">Laurus'u yakından tanı.</h2></div><p>Her kapı ayrı bir sayfaya açılıyor. Birini seç, içeri gir.</p></div>
<div class="xgrid">{tiles}</div></div></section>'''

_H3D = [("real/nil-site","d"),("app/lp-m","p"),("app/seven-d","d"),("app/sb-home","p"),("app/feronya-d","d"),("app/os-world","p"),("app/sorbi-d","d"),("real/nil-ig","p"),("app/ohsame-d","d"),("app/nf-main","p"),("app/lp-d","d"),("app/cn-home","p"),("real/nil-galeri","d"),("app/sk-sekiz","p")]
H3D_DATA = '<script>window.__H3D_IMGS=' + json.dumps([{"src":"/img/"+p+".webp","k":k,"href":"/calismalar"} for p,k in _H3D]) + '</script>'
def page_index():
    slides = "".join(slide(w, i) for i, w in enumerate(WORKS))
    words = "".join(f'<span>{w}</span> ' for w in MANIFESTO.split(" "))
    body = f'''
<section class="hero3" aria-labelledby="h-hero">
{reel()}
<div class="h3d" aria-hidden="true"></div>
{H3D_DATA}
<div class="h3-shade" aria-hidden="true"></div>
<div class="wrap h3-in">
<h1 id="h-hero"><span class="ln"><span>İşletmeni</span></span> <span class="ln"><span>internete</span></span> <span class="ln"><span>taşıyoruz.</span></span></h1>
<p class="lead">İstanbul merkezli dijital ajans: web tasarım, mobil uygulama, sosyal medya yönetimi, Google reklamı ve SEO. Kuaförden otele, kliniğe kadar her işletme için tek ekip.</p>
<div class="actions"><a class="btn btn-gold" href="iletisim.html">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="calismalar.html">İşlerimizi gör</a></div>
</div>
<a class="h3-scroll" href="#kesfet" aria-label="Aşağı kaydır"><i></i></a>
</section>
{explore()}
{cta_band()}
'''
    return ("Laurus Dijital | Web Tasarım, Sosyal Medya Yönetimi ve SEO Ajansı · İstanbul",
            "Web sitesi yaptırmak, mobil uygulama, Instagram ve sosyal medya yönetimi, Google reklamı ve SEO için İstanbul merkezli dijital ajans. Fiyatlar açık, ilk site 7 günde yayında.", body)

SVC_CH = [
  ("web-tasarim.html","Web sitesi","Telefonda hızlı açılan,|randevu getiren siteler.","Ziyaretçilerin çoğu telefondan gelir. Siten bir saniyede açılır, tek dokunuşla WhatsApp'a, aramaya ve yol tarifine götürür.",["Tek sayfadan kurumsal siteye, ihtiyacın kadar","WhatsApp, arama ve yol tarifi düğmeleri","Google İşletme Profili kurulumu ve temel SEO"],"12.000 ₺'den","app/seven-d","Seven For Life Thermal Hotel web sitesi"),
  ("sosyal-medya.html","Sosyal medya","Hesabın hep canlı,|hep tutarlı.","Aylık içerik planı, tasarım, Reels ve mesaj yönetimi. Little Paws'ın hesabını bu düzenle 19 binden fazla takipçiye taşıdık.",["Aylık plan ve markana özel tasarım dili","Reels, hikâye ve gönderi üretimi","Yorum ve mesaj yönetimi, aylık rapor"],"Aylık 12.000 ₺'den","app/lp-d","Little Paws Pet Shop Instagram profili"),
  ("reklam-yonetimi.html","Google ve Meta reklamı","Seni arayanın karşısına|ilk sen çık.","Google aramasında, haritada ve Instagram'da doğru kişiye, doğru anda görünürsün. Bütçe senin kartından, yönetim bizden.",["Google arama ve harita reklamları","Instagram ve Facebook reklamları","Hedefleme, görseller ve aylık rapor"],"Aylık 9.000 ₺","google-arama","Google arama sonuçları"),
  ("google-isletme.html","Google profili ve SEO","Haritada bulun,|yorumla güven ver.","Google İşletme Profilin, fotoğrafların, yorumların ve sitenin arama ayarları birlikte çalışır; semtinde arayan seni bulur.",["Google İşletme Profili kurulumu ve düzeni","Yerel SEO ve arama ayarları","Yorum toplama akışı"],"Vitrin paketine dahil","harita","Harita üzerinde işletme konumu"),
  ("mobil-uygulama.html","Mobil uygulama","Fikrinden|App Store'a.","iOS, Android ve web'de çalışan uygulamalar. oh same., Sorbi, Sekiz8, Çınar ve Nefes'i kendi ekibimiz tasarladı ve kodladı.",["iOS, Android ve web uygulaması","Üyelik, abonelik ve canlı veri","Mağaza yayını ve bakım"],"Ön görüşmede sabit fiyat","app/ohsame-d","oh same. uygulaması"),
]

def page_services():
    ch = ""
    for i,(h,ey,t,d,lst,pr,ph,alt) in enumerate(SVC_CH):
        li = "".join(f'<li>{I["check"]}<span>{x}</span></li>' for x in lst)
        ch += f'''<article class="chap{" rev" if i%2 else ""}"><div class="chap-vis" data-rv><img src="img/{ph}.webp" alt="{alt}" loading="lazy" decoding="async"></div>
<div class="chap-tx"><span class="eyebrow" data-rv>{ey}</span><h2 data-rv>{_words(t)}</h2><p class="lead" data-rv>{d}</p><ul class="chap-l" data-rv>{li}</ul>
<div class="chap-f" data-rv><span class="chap-pr">{pr}</span><a class="btn btn-line" href="{h}" data-pt="{ey}">Ayrıntılar</a></div></div></article>'''
    body = f'''
{cine_hero("Hizmetler","Hizmetler","Dijitalde ihtiyacın olan|her şey, tek ekipte.","Web sitesi, sosyal medya, reklam, SEO ve mobil uygulama. İstersen birini al, istersen hepsini birlikte; sitendeki mesaj, Instagram'daki görsel dil ve Google'daki reklam birbirini tamamlasın.",["tasarim-laptop","telefon-instagram","google-arama","harita"],'<a class="btn btn-gold" href="iletisim.html">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="fiyatlar.html">Fiyatları gör</a>')}
<section class="chaps" aria-label="Hizmet ayrıntıları"><div class="wrap">{ch}</div></section>
{cta_band("Hangisiyle|başlayalım?","Emin değilsen sorun değil. İşletmeni anlat, en hızlı sonuç verecek adımı birlikte seçelim.","kadin-telefon")}
'''
    return ("Hizmetler: Web Tasarım, Sosyal Medya, Reklam, SEO ve Uygulama | Laurus Dijital","Web sitesi, sosyal medya yönetimi, Google ve Meta reklamları, Google İşletme Profili ve SEO, mobil uygulama. Her hizmetin kendi sayfası, fiyatı ve örnek işleri.", body)

def page_process():
    steps = [("1. gün","Tanışma","15 dakikalık görüşmede işletmeni, müşterini ve hedefini dinleriz. Neye ihtiyacın olduğunu birlikte netleştiririz."),
             ("2–3. gün","İlk taslak","Taslağı telefonunda görürsün. Beğenmezsen ödeme yok; beğenirsen ödemenin yarısıyla devam ederiz."),
             ("4–6. gün","Tamamlama","Metinler, fotoğraflar, Google profili ve Instagram düzeni. İki düzeltme turu dahil."),
             ("7. gün","Yayında","Siten açılır, hesapların hazır olur. Sonrasında her ay kısa bir raporla ne işe yaradığını görürsün.")]
    st = "".join(f'<li data-rv style="--d:{i*120}ms"><span class="n">{i+1}</span><small>{d}</small><h3>{t}</h3><p>{x}</p></li>' for i,(d,t,x) in enumerate(steps))
    need = [("Logon ve fotoğrafların","Yoksa sorun değil; logo tasarımı ve çekim de yapıyoruz."),("Hizmetlerin ve fiyatların","Kabaca bir liste yeter, metinleri biz düzenleriz."),("Hesap erişimleri","Alan adı, Instagram ve Google hesapları her zaman senin adına açılır."),("Haftada 15 dakikan","Taslağa bakıp onay vermen yeterli; gerisi bizde.")]
    nd = "".join(f'<div class="ab-v" data-rv style="--d:{i*80}ms"><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(need))
    body = f'''
{cine_hero("Süreç","Nasıl çalışıyoruz","İlk görüşmeden|yayına yedi gün.","Önce taslağı görürsün, sonra karar verirsin. Ödemenin yarısı taslağı beğendiğinde, kalanı yayında.",["planlama","cekim","tasarim-laptop"],'<a class="btn btn-gold" href="iletisim.html">Hemen başlayalım</a>')}
<section class="light ksec" aria-labelledby="h-proc"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Yedi gün</span><h2 id="h-proc">Gün gün ne oluyor?</h2></div><p>Her adımda ne göreceğini ve ne zaman göreceğini bilirsin.</p></div>
<ol class="proc3" data-line><span class="pl" aria-hidden="true"><i></i></span>{st}</ol>
</div></section>
<section class="ksec" aria-labelledby="h-need"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Senden istediklerimiz</span><h2 id="h-need">Az şey, çok sonuç.</h2></div></div>
<div class="ab-vals">{nd}</div></div></section>
<section id="sss" class="light ksec" aria-labelledby="h-sss"><div class="wrap kfaq">
<div data-rv><span class="eyebrow">Sık sorulanlar</span><h2 id="h-sss">Aklındaki sorular.</h2><p class="muted">Burada yoksa WhatsApp'tan yaz, aynı gün dönelim.</p></div>
{faq_list(HOME_FAQ)}
</div></section>
{cta_band()}
'''
    return ("Nasıl Çalışıyoruz: 7 Günde Yayında | Laurus Dijital","İlk görüşmeden yayına 7 gün: tanışma, ücretsiz taslak, tamamlama ve yayın. Beğenmezsen ödeme yok; ödemenin yarısı taslağı beğendiğinde.", body)

def page_contact():
    nx = [("Mesajın gelir","Formu gönderdiğinde mesajın WhatsApp'ta hazır açılır; tek dokunuşla bize ulaşır."),("Aynı gün döneriz","İşletmeni inceleriz ve sana neler yapabileceğimizi kısaca anlatırız."),("Taslağını görürsün","Beğenirsen devam ederiz. Beğenmezsen hiçbir ödeme yapmazsın.")]
    steps = "".join(f'<div class="ab-v" data-rv style="--d:{i*80}ms"><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(nx))
    body = f'''
{cine_hero("İletişim","İletişim","İşletmeni anlat,|taslağını gör.","İlk görüşme ücretsiz. WhatsApp'tan yaz ya da formu doldur; aynı gün dönelim.",["kadin-telefon","is-sahibi","kafe-masa"],'<a class="btn btn-gold" href="#iletisim">Formu doldur</a><a class="btn btn-line js-wa" href="https://wa.me/905434309702">WhatsApp\'tan yaz</a>',"sm")}
{contact(title="Üç alanı doldur, yeter.")}
<section class="ksec" aria-labelledby="h-next"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Sonra ne olur</span><h2 id="h-next">Üç kısa adım.</h2></div></div>
<div class="ab-vals three">{steps}</div></div></section>
'''
    return ("İletişim ve Ücretsiz Ön Görüşme | Laurus Dijital","Laurus Dijital ile iletişime geç: WhatsApp 0543 430 97 02, merhaba@laurusdijital.com. İlk görüşme ücretsiz, aynı gün dönüş.", body)

CH_IMGS = {"web-tasarim.html":["tasarim-laptop","app/seven-d","app/feronya-d"],"sosyal-medya.html":["telefon-instagram","app/lp-d","cekim"],"reklam-yonetimi.html":["google-arama","kadin-telefon","is-sahibi"],"google-isletme.html":["harita","google-arama","kafe-masa"],"mobil-uygulama.html":["app/ohsame-d","app/sorbi-d","app/feronya-d"],"calismalar.html":["app/seven-d","app/lp-d","app/feronya-d","app/sorbi-d"],"fiyatlar.html":["is-sahibi","butik-sahibi","kafe-masa"],"hakkimizda.html":["planlama","cekim","kadin-telefon"]}

def phero_to_cine(body, slug, eyebrow):
    m = re.search(r'<section class="phero"[^>]*>.*?</section>', body, re.S)
    if not m: return body
    blk = m.group(0)
    h1 = re.search(r'<h1 id="h-page">(.*?)</h1>', blk, re.S).group(1)
    lead = re.search(r'<p class="lead">(.*?)</p>', blk, re.S)
    act = re.search(r'<div class="actions">(.*?)</div>', blk, re.S)
    cr = re.search(r'<nav class="crumbs"[^>]*>(.*?)</nav>', blk, re.S)
    crumb = re.sub(r'^<a href="index.html">Ana sayfa</a> / ', '', cr.group(1)) if cr else ""
    t = re.sub(r"<[^>]+>", "", h1).strip()
    # split title into two lines near the middle for drama
    ws = t.split(" ")
    if len(ws) > 3:
        cut = (len(ws)+1)//2; t = " ".join(ws[:cut]) + "|" + " ".join(ws[cut:])
    new = cine_hero(crumb, eyebrow, t, lead.group(1) if lead else "", CH_IMGS.get(slug, ["planlama","cekim"]), act.group(1) if act else "")
    return body.replace(blk, new, 1)

def v20_post(slug, body):
    if slug in CH_IMGS:
        body = phero_to_cine(body, slug, PT_NAMES.get(slug.replace(".html",""), "Laurus"))
    if slug != "iletisim.html":
        body = re.sub(r'<section id="iletisim" class="contact".*?</section>', lambda m: cta_band(), body, flags=re.S)
        body = body.replace('href="#iletisim"','href="iletisim.html"')
    body = body.replace('href="index.html#hizmetler"','href="hizmetler.html"').replace('href="index.html#sss"','href="surec.html#sss"').replace('href="index.html#iletisim"','href="iletisim.html"')
    return body
