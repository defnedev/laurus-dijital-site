
# ---------- own apps ----------
APPS = [
  dict(id="ohsame", name="oh same.", kind="Mobil + web uygulaması", status="Web'de yayında · iOS sürümü yolda",
       url="https://ohsame.app", cta="oh same.'i aç", lap="ohsame-d", ph="ohsame-app",
       desc="Nasıl hissettiğini seçiyorsun; dünyada aynı anda aynı şeyi hisseden insanları canlı bir küre üzerinde görüyorsun. “Ah, benim gibi biri daha var” dedirten bir uygulama.",
       did=["Canlı dünya küresi ve anlık sayaçlar","Apple, Google ve e-posta ile giriş; isteyen anonim kullanır","Türkçe ve İngilizce, iOS ve web aynı üründe"],
       tech=["iOS","Web uygulaması","Canlı veri","Üyelik sistemi"]),
  dict(id="sorbi", name="Sorbi", kind="Web platformu", status="sorbiapp.com'da yayında",
       url="https://sorbiapp.com", cta="Sorbi'yi aç", lap="sorbi-d", ph="sorbi-m",
       desc="Doğum tarihini yazıyorsun, doğduğun anın gökyüzünü ve haritanın kaç kişide bir görüldüğünü saniyeler içinde görüyorsun. Arkasında 1,3 milyondan fazla gök anını sayan kendi hesap motorumuz var.",
       did=["Swiss Ephemeris ile test edilmiş hesap motoru","Üyelik: Google ve e-posta ile giriş","Paylaşılabilir kartlar, günlük gökyüzü ve dersler"],
       tech=["Web platformu","Hesap motoru","Üyelik","SEO"]),
  dict(id="sekiz", name="Sekiz", kind="Mobil uygulama", status="iOS ve Android için",
       url=None, cta=None, lap=None, ph="sekiz-m",
       desc="Aklındaki soruyu tut, telefonu salla, cevabın ekranda belirsin. Tek ekran, tek hareket; sade ama özenli bir mobil deneyim.",
       did=["Telefonu sallamayı algılayan hareket sensörü","Titreşimli geri bildirim ve akıcı animasyonlar","Türkçe ve İngilizce"],
       tech=["iOS","Android","React Native"]),
]
AMAP = {a["id"]: a for a in APPS}

def app_stage(a, cls=""):
    ph = f'<div class="phone"><div class="pscr"><img class="shot" src="img/app/{a["ph"]}.webp" alt="{a["name"]} telefon ekranı" loading="lazy"></div></div>'
    if not a["lap"]:
        return f'<div class="stage solo {cls}">{ph}</div>'
    lap = f'<div class="laptop"><div class="lid"><div class="scr"><img class="shot" src="img/app/{a["lap"]}.webp" alt="{a["name"]} bilgisayar görünümü" loading="lazy"></div></div><div class="base"></div></div>'
    return f'<div class="stage {cls}">{lap}{ph}</div>'

def app_card(a, i=0, big=False):
    chips = "".join(f"<span>{t}</span>" for t in a["tech"])
    act = f'<a class="btn btn-gold" href="{a["url"]}" target="_blank" rel="noopener">{a["cta"]}</a>' if a["url"] else '<a class="btn btn-gold" href="#iletisim">Benzerini konuşalım</a>'
    return (f'<article class="appc{" appc-big" if big else ""}" id="app-{a["id"]}" data-rv style="--d:{i*90}ms"><div class="app-vis bg-{a["id"]}">{app_stage(a)}</div>'
            f'<div class="app-tx"><span class="app-kind">{a["kind"]}</span><h3>{a["name"]}</h3><p>{a["desc"]}</p>{checks(a["did"])}<div class="chips">{chips}</div>'
            f'<div class="app-foot"><span class="app-st"><i></i>{a["status"]}</span>{act}</div></div></article>')

def apps_block():
    return '<div class="apps">' + app_card(APPS[0], 0, True) + app_card(APPS[1], 1) + app_card(APPS[2], 2) + '</div>'

def app_case(a):
    chips = "".join(f"<span>{t}</span>" for t in a["tech"])
    link = f'<a class="btn btn-line" href="{a["url"]}" target="_blank" rel="noopener">{a["cta"]}</a>' if a["url"] else ""
    return (f'<div class="bcase"><div class="bcase-vis bg-{a["id"]}">{app_stage(a, "in-case")}</div><div class="bcase-tx">'
            f'<div class="bcase-id"><div><b>{a["name"]}</b><small>Kendi ürünümüz, {a["kind"].lower()}</small></div></div>'
            f'<div class="chips">{chips}</div><h3>Ne yaptık</h3><p>{a["desc"]}</p><h3>Neler var</h3>{checks(a["did"])}'
            f'<p class="app-st"><i></i>{a["status"]}</p>'
            f'<div class="wf-act"><a class="btn btn-gold" href="#iletisim">Uygulamamı konuşalım</a>{link}</div></div></div>')

def page_apps():
    does = [("phone","iOS ve Android","Tek kod tabanıyla iki platformda çalışan, mağaza kurallarına uygun uygulamalar."),
            ("web","Web uygulaması","Tarayıcıda uygulama gibi çalışan, telefona eklenebilen web uygulamaları."),
            ("lock","Üyelik ve giriş","Apple, Google ve e-posta ile giriş; anonim kullanım ve güvenli veri saklama."),
            ("star","Abonelik ve ödeme","Uygulama içi satın alma, abonelik ve ücretli katmanlar."),
            ("bolt","Mağaza yayını","App Store ve Google Play hesapları, ekran görüntüleri, açıklamalar ve inceleme süreci."),
            ("chart","Ölçüm ve bakım","Kullanım verisi, hata takibi ve sürüm güncellemeleri.")]
    dg = "".join(f'<div class="do"><span class="ic">{I[ic]}</span><h3>{t}</h3><p>{d}</p></div>' for ic,t,d in does)
    steps = [("1. hafta","Kapsam","Uygulamanın tek cümlelik vaadini ve ilk sürümde olacakları birlikte netleştiririz."),
             ("2. hafta","Tıklanabilir taslak","Ekranları telefonunda deneyebileceğin bir taslak olarak görürsün."),
             ("3–6. hafta","Geliştirme","Haftalık sürümlerle ilerleriz; her hafta yeni hali elinde olur."),
             ("Yayın","Mağaza ve web","App Store, Google Play ve web sürümü yayına alınır; sonrası bakım.")]
    month = '<div class="month">' + "".join(f"<div><b>{w}</b><h4>{t}</h4><p>{d}</p></div>" for w,t,d in steps) + '</div>'
    faq = [("Uygulama yaptırmak ne kadar tutar?","Kapsama göre değişir: tek ekranlı bir uygulamayla üyelik, ödeme ve canlı veri içeren bir ürün aynı fiyatta olmaz. Ücretsiz ön görüşmede kapsamı çıkarır, sabit fiyat ve teslim tarihi veririz."),
           ("Önce web sitesiyle mi başlamalıyım?","Çoğu fikir için evet. Önce web uygulaması olarak deneyip kullanıcı geldikçe mobil uygulamaya geçmek hem daha hızlı hem daha ucuzdur. oh same.'i de bu yolla büyüttük."),
           ("Uygulama mağazaya kimin adına yüklenir?","Senin adına. App Store ve Google Play geliştirici hesapları senin olur; kaynak kod da teslim edilir."),
           ("Yayından sonra ne oluyor?","Aylık bakım paketiyle güncellemeleri, mağaza değişikliklerini ve küçük geliştirmeleri biz yaparız.")]
    body = f'''
<section class="phero" aria-labelledby="h-page"><div class="wrap">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / <a href="index.html#hizmetler">Hizmetler</a> / Mobil uygulama</nav>
<h1 id="h-page">Mobil uygulama ve web uygulaması geliştirme.</h1>
<p class="lead">Fikrini iOS, Android ve web'de çalışan bir ürüne çeviriyoruz. Aşağıdaki uygulamaları kendi ekibimiz tasarladı ve kodladı.</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="#uygulamalar">Uygulamalarımızı gör</a></div></div>
<div class="ph app-ph">{img("app/ohsame-d","oh same. uygulamasının web sitesi ve telefon ekranı", eager=True)}</div>
</div></section>
<section id="uygulamalar" class="ksec apps-sec" aria-labelledby="h-apps"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Kendi ürünlerimiz</span><h2 id="h-apps">Yaptığımız uygulamalar.</h2></div><p>Tasarımı, yazılımı ve yayını tamamen bizde olan üç ürün.</p></div>
{apps_block()}
</div></section>
<section class="light ksec" aria-labelledby="h-do"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Neler yapıyoruz</span><h2 id="h-do">Fikirden mağazaya, tek ekip.</h2></div></div>
<div class="do-grid">{dg}</div>
<h3 class="kh3" style="margin:48px 0 18px">Süreç nasıl işliyor</h3>{month}
</div></section>
<section class="light ksec" aria-labelledby="h-afaq" style="padding-top:0"><div class="wrap kfaq">
<div data-rv><span class="eyebrow">Sık sorulanlar</span><h2 id="h-afaq">Uygulama hakkında sorular.</h2></div>
{faq_list(faq)}
</div></section>
{contact(title="Uygulama fikrini anlat, taslağını gör.", need="Mobil uygulama")}
'''
    return ("Mobil Uygulama Geliştirme ve Web Uygulaması · İstanbul | Laurus Dijital",
            "iOS, Android ve web uygulaması geliştirme: üyelik, abonelik, canlı veri ve mağaza yayını dahil. oh same., Sorbi ve Sekiz uygulamalarını kendi ekibimiz geliştirdi.", body)

