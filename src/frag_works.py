# ---------- works: real + sample designs ----------
HOTEL_NAME = "Ege Termal Otel"   # örnek; müşteri onayıyla gerçek adla değişir

BRANDS = [
  dict(id="moda", name="Moda Salon", sector="Kuaför ve güzellik", cat="guzellik", city="Kadıköy, Moda",
       logo='<span class="lg-moda">Moda<em>Salon</em></span>',
       pal=[("#2E1A24","Mürdüm"),("#F4E4DC","Pudra"),("#B8875F","Bakır"),("#FFFDFB","Krem")],
       fonts="Başlık: klasik serif. Metin: sade sans.",
       h="Saçın için sakin bir saat.", p="Kesim, renk ve bakım. Salı–Pazar 10:00–20:00, Moda iskelesine 5 dakika.",
       hero="salon-fon", nav=["Hizmetler","Fiyatlar","Galeri","İletişim"], cta="Randevu al",
       items=[("Kesim + fön","45 dk","650 ₺"),("Dip boya","90 dk","1.400 ₺"),("Keratin bakım","120 dk","2.200 ₺")],
       handle="modasalon.kadikoy", bio="Kuaför · Moda, Kadıköy<br>Randevu için WhatsApp ↓",
       grid=["salon-yikama",("Gelin saçı<br>sezonu açıldı","#2E1A24","#F4E4DC"),"salon-ic",("Hafta içi<br>%15 dip boya","#B8875F","#FFFDFB"),"salon-fon","nail",("Önce / sonra<br>Keratin","#F4E4DC","#2E1A24"),"salon-yikama","salon-ic"],
       svcs=["Web sitesi","Instagram","Google profili"],
       did=["Tek sayfa site ve WhatsApp randevu düğmesi","Google profili: fotoğraf, saat, hizmet listesi","Instagram için renk ve yazı düzeni"],
       case="Randevular telefondan ve DM'den karışık geliyor; Google profilinde fotoğraf yok, saatler eski."),
  dict(id="kose", name="Köşe Kahve", sector="Kafe ve restoran", cat="yemek", city="Bostancı",
       logo='<span class="lg-kose">köşe<i>kahve</i></span>',
       pal=[("#2A1B12","Espresso"),("#EADBC4","Krema"),("#6E7B3B","Zeytin"),("#C8692F","Tarçın")],
       fonts="Başlık: sıcak serif. Metin: sade sans.",
       h="Sahile iki dakika, kahveye bir adım.", p="Taze kavrulmuş çekirdek, ev yapımı tatlılar ve hafta sonu kahvaltısı.",
       hero="kafe-latte", nav=["Menü","Kahvaltı","Saatler","Yol tarifi"], cta="Yol tarifi",
       items=[("Filtre kahve","","95 ₺"),("Flat white","","120 ₺"),("Serpme kahvaltı","2 kişilik","890 ₺")],
       handle="kosekahve.bostanci", bio="Kafe · Bostancı<br>Her gün 08:00–22:00",
       grid=["kafe-masa",("Hafta sonu<br>kahvaltısı","#2A1B12","#EADBC4"),"kafe-latte","kafe-kupa",("Yeni çekirdek:<br>Etiyopya","#6E7B3B","#FFFFFF"),"kafe-masa",("Sahile<br>2 dakika","#EADBC4","#2A1B12"),"kafe-kupa","kafe-latte"],
       svcs=["Web sitesi","Instagram","Google reklamı"],
       did=["3 km çevreye Google arama reklamı","Menü ve fotoğraflarla harita profili","Kolay güncellenen menü sayfası"],
       case="Sahile yakın ama ara sokakta; yoldan geçenler ve semte yeni gelenler kafeyi bilmiyor."),
  dict(id="dis", name="Gülümse Diş", sector="Sağlık ve klinik", cat="saglik", city="Ataşehir",
       logo='<span class="lg-dis">gülümse<b>diş</b></span>',
       pal=[("#0E6B6B","Petrol"),("#E8F1EE","Nane"),("#F2A65A","Kayısı"),("#FFFFFF","Beyaz")],
       fonts="Başlık: yuvarlak, sakin sans. Metin: okunaklı sans.",
       h="Rahat bir koltuk, net bir plan.", p="İmplant, ortodonti ve estetik diş hekimliği. Muayene randevusu aynı hafta içinde.",
       hero="dis-klinik", nav=["Tedaviler","Hekimlerimiz","Ulaşım","Sık sorulanlar"], cta="Muayene randevusu",
       items=[("Muayene ve plan","","Ücretsiz"),("Diş taşı temizliği","30 dk","Randevuyla"),("Şeffaf plak","","Ön görüşme")],
       handle="gulumse.dis", bio="Diş kliniği · Ataşehir<br>Randevu için mesaj atın",
       grid=["dis-hekim",("İmplant<br>nasıl yapılır?","#0E6B6B","#FFFFFF"),"dis-klinik",("Çocuklar için<br>ilk muayene","#F2A65A","#FFFFFF"),"dis-hekim",("Şeffaf plak<br>sorular","#E8F1EE","#0E6B6B"),"dis-klinik","dis-hekim",("Hafta içi<br>akşam randevu","#0E6B6B","#E8F1EE")],
       svcs=["Web sitesi","SEO","Instagram"],
       did=["Tedavi sayfaları ve sık sorulanlar","“Ataşehir diş kliniği” aramaları için SEO","Bilgilendiren, sade Instagram içerikleri"],
       case="Hastalar kliniği tavsiyeyle buluyor ama Google'da “Ataşehir diş kliniği” aramasında görünmüyor."),
  dict(id="hukuk", name="Aydın Hukuk", sector="Avukat ve danışmanlık", cat="hizmet", city="Şişli",
       logo='<span class="lg-hukuk">AYDIN<small>Hukuk Bürosu</small></span>',
       pal=[("#1D2B3A","Lacivert"),("#C9B48A","Pirinç"),("#F5F2EC","Fildişi"),("#6B7686","Arduvaz")],
       fonts="Başlık: ağır serif. Metin: sade sans.",
       h="Hukuki süreçte yanınızda, açık ve anlaşılır.", p="Aile, iş ve ticaret hukuku. İlk görüşmede süreci ve maliyeti açıkça konuşuruz.",
       hero="hukuk-kutuphane", nav=["Çalışma alanları","Ekibimiz","Makaleler","İletişim"], cta="Görüşme talep et",
       items=[("Aile hukuku","Boşanma, velayet",""),("İş hukuku","Tazminat, işe iade",""),("Ticaret hukuku","Sözleşme, şirket","")],
       handle="aydinhukuk", bio="Hukuk bürosu · Şişli<br>Bilgilendirme içerikleri",
       grid=[("Kıdem tazminatı<br>nasıl hesaplanır?","#1D2B3A","#C9B48A"),"hukuk-kutuphane",("Kira artışında<br>yeni dönem","#F5F2EC","#1D2B3A"),"hukuk-ofis",("Velayet<br>süreci","#C9B48A","#1D2B3A"),"hukuk-kutuphane",("Sözleşme<br>kontrol listesi","#1D2B3A","#F5F2EC"),"hukuk-ofis",("Sık sorulan<br>5 soru","#6B7686","#FFFFFF")],
       svcs=["Web sitesi","SEO","İçerik"],
       did=["Çalışma alanı sayfaları ve makale bölümü","Hukuki sorulara yanıt veren SEO içerikleri","LinkedIn ve Instagram için bilgilendirme kartları"],
       case="Sitesi eski ve telefonda bozuk açılıyor; insanlar hukuki sorularını Google'a yazıyor ama büroya ulaşmıyor."),
  dict(id="emlak", name="Kuzey Gayrimenkul", sector="Emlak", cat="hizmet", city="Beykoz",
       logo='<span class="lg-emlak">kuzey<small>gayrimenkul</small></span>',
       pal=[("#14321F","Orman"),("#E7E2D6","Kum"),("#B5562E","Kiremit"),("#FFFFFF","Beyaz")],
       fonts="Başlık: geniş sans. Metin: sade sans.",
       h="Boğaz'a yakın, size uygun ev.", p="Beykoz ve çevresinde satılık ve kiralık portföy. Her ilan için video tur ve net bilgi.",
       hero="emlak-salon", nav=["Satılık","Kiralık","Değerleme","İletişim"], cta="Portföyü gör",
       items=[("3+1 bahçeli","Kavacık","Satılık"),("2+1 deniz manzaralı","Paşabahçe","Kiralık"),("Değerleme","Ücretsiz","Ön görüşme")],
       handle="kuzey.gayrimenkul", bio="Emlak · Beykoz<br>Her ilanın video turu var",
       grid=["emlak-salon",("Yeni ilan<br>3+1 bahçeli","#14321F","#E7E2D6"),"emlak-oda",("Video tur<br>izleyin","#B5562E","#FFFFFF"),"emlak-salon","emlak-oda",("Evinizin değeri<br>ne kadar?","#E7E2D6","#14321F"),"emlak-oda","emlak-salon"],
       svcs=["Web sitesi","Meta reklamı","Instagram"],
       did=["İlan sayfaları ve video tur alanı","Semte özel Instagram ve Meta reklamları","Değerleme talebi toplayan form"],
       case="İlanlar yalnızca ilan sitelerinde; kendi markası yok, gelen talepler komisyonlu platformlara bağlı."),
  dict(id="butik", name="Lina Butik", sector="Butik ve e-ticaret", cat="perakende", city="Nişantaşı",
       logo='<span class="lg-butik">LINA</span>',
       pal=[("#141414","Siyah"),("#F3E9E2","Ten"),("#D4A3A0","Gül kurusu"),("#FFFFFF","Beyaz")],
       fonts="Başlık: ince, geniş aralıklı serif. Metin: sade sans.",
       h="Sonbahar seçkisi geldi.", p="Doğal kumaşlar, sınırlı adet. Mağazadan ya da siteden sipariş, aynı gün kargo.",
       hero="butik-aski", nav=["Yeni gelenler","Triko","Elbise","Mağaza"], cta="Alışverişe başla",
       items=[("Yün triko","Krem","1.850 ₺"),("Keten gömlek","Taş","1.290 ₺"),("Örgü hırka","Kahve","2.150 ₺")],
       handle="linabutik", bio="Butik · Nişantaşı<br>Sipariş için siteye ↓",
       grid=["butik-aski",("Sonbahar<br>seçkisi","#141414","#F3E9E2"),"butik-magaza","butik-aski",("Aynı gün<br>kargo","#D4A3A0","#141414"),"butik-alisveris","butik-magaza",("Sınırlı<br>adet","#F3E9E2","#141414"),"butik-aski"],
       svcs=["Satış sitesi","Instagram","Meta reklamı"],
       did=["Ürün kataloğu ve online ödeme","Yeni sezon için Instagram çekim planı","Ürün odaklı Meta reklamları"],
       case="Satışlar sadece DM'den; stok ve fiyat soruları her gün tekrar ediyor, ödeme havaleyle zor ilerliyor."),
]
BMAP = {b["id"]: b for b in BRANDS}

WORKS = [
  dict(id="nil", name="Nil Pet Kuaför", sector="Pet kuaför", cat="pet", kind="real", city="Kadıköy",
       svcs=["Web sitesi","Instagram","Google profili"], url="https://nilpetkuafor.com",
       note="Kadıköy'de pet kuaför. Sitesini, Instagram tasarımlarını ve Google profilini biz hazırladık.",
       did=["Tek sayfa site: hizmetler, öncesi-sonrası galeri, randevu formu","Fiyat listesi ve vizyon gönderileri dahil Instagram tasarımları","WhatsApp, arama ve yol tarifi düğmeleri"]),
  dict(id="otel", name=HOTEL_NAME, sector="Otel ve turizm", cat="turizm", kind="ornek", city="Kuşadası",
       svcs=["Google reklamı","SEO","Dönüşüm takibi"],
       note="Kuşadası'nda termal otel için Google arama reklamı ve SEO kurgusu.",
       did=["“kuşadası termal otel” gibi aramalar için reklam grupları","Oda, havuz ve paket sayfaları için SEO","Rezervasyon ve arama tıklamalarının takibi"],
       case="Rezervasyonların çoğu komisyonlu sitelerden geliyor; otelin kendi sitesi aramalarda arka sıralarda."),
] + [dict(id=b["id"], name=b["name"], sector=b["sector"], cat=b["cat"], kind="ornek", city=b["city"], svcs=b["svcs"], did=b["did"], case=b["case"]) for b in BRANDS]
WMAP = {w["id"]: w for w in WORKS}
CATS = [("hepsi","Tümü"),("guzellik","Güzellik"),("pet","Pet"),("yemek","Yeme-içme"),("saglik","Sağlık"),("hizmet","Hukuk ve emlak"),("perakende","Perakende"),("turizm","Turizm")]

def b_site(b):
    nav = "".join(f"<span>{x}</span>" for x in b["nav"])
    items = "".join(f'<div><b>{a}</b><small>{d}</small><span>{p}</span></div>' for a,d,p in b["items"])
    return f'''<div class="bsite b-{b["id"]}" data-fit="1000"><div class="bs-nav">{b["logo"]}<nav>{nav}</nav><span class="bs-cta">{b["cta"]}</span></div>
<div class="bs-hero"><div class="bs-tx"><small>{b["city"]}</small><h3>{b["h"]}</h3><p>{b["p"]}</p><div class="bs-btns"><span class="b1">WhatsApp'tan yaz</span><span class="b2">{b["nav"][0]}</span></div></div><div class="bs-im">{img(b["hero"],"")}</div></div>
<div class="bs-list">{items}</div></div>'''

def b_ig(b):
    g = ""
    for x in b["grid"]:
        if isinstance(x, tuple):
            t,bg,fg = x; g += f'<i class="tx" style="background:{bg};color:{fg}"><span>{t}</span></i>'
        else:
            g += f'<i>{img(x,"")}</i>'
    return f'''<div class="big b-{b["id"]}" data-fit="380"><div class="ig-top"><b>{b["handle"]}</b></div>
<div class="ig-h"><span class="ig-av">{b["logo"]}</span><div class="ig-n"><div><b>Örnek</b>hesap</div><div><b>{b["sector"].split(" ")[0]}</b>sektör</div></div></div>
<div class="ig-bio"><b>{b["name"]}</b><br>{b["bio"]}</div>
<div class="ig-bt"><span class="p">Mesaj gönder</span><span>{b["cta"]}</span></div>
<div class="ig-g">{g}</div></div>'''

def serp():
    n = HOTEL_NAME
    return f'''<div class="serp" data-fit="1000"><div class="sp-top"><span class="sp-g"><b style="color:#4285F4">G</b><b style="color:#EA4335">o</b><b style="color:#FBBC05">o</b><b style="color:#4285F4">g</b><b style="color:#34A853">l</b><b style="color:#EA4335">e</b></span><div class="sp-q">kuşadası termal otel her şey dahil</div></div>
<div class="sp-tabs"><span class="on">Tümü</span><span>Haritalar</span><span>Görseller</span><span>Oteller</span></div>
<div class="sp-body"><div class="sp-res">
<div class="sp-ad"><small><b>Sponsorlu</b></small><div class="sp-url"><i></i>{n.lower().replace(" ","")}.com.tr</div><h4>{n} | Kuşadası'nda Termal Havuzlu Her Şey Dahil</h4><p>Açık ve kapalı termal havuz, spa ve aile odaları. Resmi sitede en uygun fiyat, ücretsiz iptal seçeneği.</p><div class="sp-sl"><span>Odalar</span><span>Termal & Spa</span><span>Erken rezervasyon</span><span>İletişim</span></div></div>
<div class="sp-org"><div class="sp-url"><i></i>{n.lower().replace(" ","")}.com.tr › termal-havuz</div><h4>Termal Havuz ve Spa | {n} Kuşadası</h4><p>Güzelçamlı'da, Milli Park'a yakın. 38 °C termal su, kapalı havuz ve masaj hizmetleri. Fotoğraflar, saatler ve paket fiyatları.</p></div>
<div class="sp-org dim"><div class="sp-url"><i></i>rezervasyon-sitesi.com › kusadasi</div><h4>Kuşadası Termal Otelleri 2026</h4><p>Karşılaştırma ve fiyatlar...</p></div>
</div><div class="sp-side"><div class="sp-card">{img("otel-havuz","")}<div><b>{n}</b><small>Otel · Güzelçamlı, Kuşadası</small><div class="sp-btns"><span>Web sitesi</span><span>Yol tarifi</span><span>Ara</span></div></div></div></div></div></div>'''

def otel_mobile():
    n = HOTEL_NAME
    return f'''<div class="omob" data-fit="380"><div class="om-im">{img("otel-termal","")}<span>{n}</span></div>
<div class="om-tx"><small>Kuşadası, Güzelçamlı</small><h5>Termal havuz, deniz ve her şey dahil.</h5><p>Resmi sitede en uygun fiyat ve ücretsiz iptal.</p><span class="om-b">Fiyatları gör</span><span class="om-b2">WhatsApp'tan sor</span></div>
<div class="om-l"><div>{img("otel-havuz","")}<b>Açık havuz</b></div><div>{img("otel-teras","")}<b>Deniz terası</b></div></div></div>'''

def w_stage(w, cls=""):
    if w["id"] == "nil":
        lap = f'<img class="shot" src="img/real/nil-site.webp" alt="Nil Pet Kuaför web sitesi ana sayfası" loading="lazy">'
        ph = f'<img class="shot" src="img/real/nil-ig.webp" alt="Nil Pet Kuaför Instagram profili" loading="lazy">'
    elif w["id"] == "otel":
        lap, ph = serp(), otel_mobile()
    else:
        b = BMAP[w["id"]]; lap, ph = b_site(b), b_ig(b)
    return f'''<div class="stage {cls}"><div class="laptop"><div class="lid"><div class="scr">{lap}</div></div><div class="base"></div></div>
<div class="phone"><div class="pscr">{ph}</div></div></div>'''

def kind_tag(w):
    return '<span class="wtag real">Gerçek iş</span>' if w["kind"]=="real" else '<span class="wtag">Örnek tasarım</span>'

def hero_showcase():
    sets = "".join(f'<div class="show-set{" on" if i==0 else ""}" data-show="{w["id"]}"{"" if i==0 else " aria-hidden=\"true\""}>{w_stage(w)}</div>' for i,w in enumerate(WORKS))
    caps = "".join(f'<div class="show-cap{" on" if i==0 else ""}" data-cap="{w["id"]}">{kind_tag(w)}<b>{w["name"]}</b><small>{w["sector"]}, {w["city"]} · {", ".join(w["svcs"])}</small></div>' for i,w in enumerate(WORKS))
    segs = "".join(f'<button type="button" data-show-btn="{w["id"]}" aria-label="{w["name"]}" aria-pressed="{"true" if i==0 else "false"}"><i></i></button>' for i,w in enumerate(WORKS))
    return f'''<div class="showcase" data-showcase><div class="show-stage">{sets}</div>
<div class="show-bar"><div class="show-caps" aria-live="polite">{caps}</div><div class="show-ctl"><button type="button" class="show-nav" data-show-prev aria-label="Önceki iş">‹</button><div class="show-segs" role="group" aria-label="İş seç">{segs}</div><button type="button" class="show-nav" data-show-next aria-label="Sonraki iş">›</button></div></div></div>'''

def work_card(w, featured=False):
    chips = "".join(f"<span>{s}</span>" for s in w["svcs"])
    href = f'calismalar.html#{w["id"]}'
    if featured:
        return f'''<article class="wfeat" data-cat="{w["cat"]}"><div class="wf-vis">{w_stage(w)}</div>
<div class="wf-tx">{kind_tag(w)}<h3>{w["name"]}</h3><p class="muted">{w["sector"]}, {w["city"]}</p><p>{w["note"]}</p>{checks(w["did"])}<div class="chips">{chips}</div>
<div class="wf-act"><a class="btn btn-gold" href="{w["url"]}" target="_blank" rel="noopener">Siteyi ziyaret et</a><a class="btn btn-line" href="{href}">Detaylar</a></div></div></article>'''
    if w["id"] == "otel": prev = serp()
    else: prev = b_site(BMAP[w["id"]])
    return f'''<a class="wcard" href="{href}" data-cat="{w["cat"]}"><div class="wc-scr"><div class="wc-in">{prev}</div></div>
<div class="wc-tx">{kind_tag(w)}<h3>{w["name"]}</h3><p>{w["sector"]}, {w["city"]}</p><div class="chips">{chips}</div></div></a>'''

def works_block():
    chips = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k=="hepsi" else "false"}">{t}</button>' for k,t in CATS)
    feat = work_card(WMAP["nil"], featured=True)
    cards = "".join(work_card(w) for w in WORKS if w["id"] != "nil")
    return f'''<div class="works" data-works><div class="filters" role="group" aria-label="Sektöre göre süz">{chips}</div>{feat}<div class="wgrid">{cards}</div><p class="knote wempty" hidden>Bu sektörde henüz yayınlanmış bir çalışma yok. Senin işin ilk olsun: aşağıdan yaz.</p></div>'''

def brand_case(w):
    stage = w_stage(w, "in-case")
    chips = "".join(f"<span>{s}</span>" for s in w["svcs"])
    extra = ""
    if w["id"] in BMAP:
        b = BMAP[w["id"]]
        sw = "".join(f'<span><i style="background:{c}"></i>{n}</span>' for c,n in b["pal"])
        extra = f'<h3>Marka dili</h3><div class="swatches">{sw}</div><p class="fonts">{b["fonts"]}</p>'
    durum = w.get("case") or w.get("note")
    link = f'<a class="btn btn-line" href="{w["url"]}" target="_blank" rel="noopener">Siteyi ziyaret et</a>' if w.get("url") else ""
    sub = "Gerçek müşteri çalışması" if w["kind"]=="real" else "Örnek çalışma"
    return f'''<div class="bcase">
<div class="bcase-vis bg-{w["id"]}">{stage}</div>
<div class="bcase-tx">
<div class="bcase-id"><div><b>{w["name"]}</b><small>{sub}, {w["sector"].lower()}</small></div></div>
<div class="chips">{chips}</div>
<h3>{"Ne yaptık" if w["kind"]=="real" else "Durum"}</h3><p>{durum}</p>
<h3>{"Neler var" if w["kind"]=="real" else "Ne yaparız"}</h3>{checks(w["did"])}
{extra}
<div class="wf-act"><a class="btn btn-gold" href="#iletisim">Benim için de hazırla</a>{link}</div>
</div></div>'''

