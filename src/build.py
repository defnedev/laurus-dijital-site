#!/usr/bin/env python3
"""Laurus Dijital static site builder.

Add a page: write a function returning (title, description, body_html) and register it in PAGES.
Add a service: append to SERVICES and create its page function. Run: python3 build.py
Output goes to ../laurus-site (Cloudflare Pages upload folder).
"""
import os, shutil, html

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(SRC), "laurus-site")
BASE = "https://laurusdijital.com"
PHONE_TXT = "0543 430 97 02"
PHONE_TEL = "+905434309702"
EMAIL = "merhaba@laurusdijital.com"

# ---------- icons ----------
I = {
 "web": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 8h18M8 21h8"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
 "ads": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 19V5M4 19h16M8 15l4-4 3 3 5-6"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-6.1-7-11a7 7 0 0 1 14 0c0 4.9-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 "search": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>',
 "video": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="6" y="2" width="12" height="20" rx="3"/><path d="M10.5 9.5v5l4-2.5z" fill="currentColor"/></svg>',
 "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 5h16v11H8l-4 4z"/></svg>',
 "cal": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
 "bolt": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
 "star": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg>',
 "pen": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 20h4L19 9l-4-4L4 16z"/></svg>',
 "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
 "target": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="currentColor"/></svg>',
 "lock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
 "app": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="6.5" y="2.5" width="11" height="19" rx="2.6"/><path d="M10.5 18.5h3"/><path d="M9.5 7.5h2v2h-2zM12.5 7.5h2v2h-2zM9.5 10.5h2v2h-2zM12.5 10.5h2v2h-2z" stroke-width="1.2"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M5 3h4l2 5-3 2a11 11 0 0 0 6 6l2-3 5 2v4a2 2 0 0 1-2 2A17 17 0 0 1 3 5a2 2 0 0 1 2-2z"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="m5 12 5 5 9-10"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "down": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 "wa": '<svg viewBox="0 0 24 24"><use href="#wa"/></svg>',
}
def checks(items, cls="checks"):
    return f'<ul class="{cls}">' + "".join(f"<li>{I['check']}<span>{x}</span></li>" for x in items) + "</ul>"

SERVICES = [
  ("web-tasarim.html", "web", "Web tasarım", "Telefonda hızlı açılan, randevuya götüren siteler"),
  ("sosyal-medya.html", "ig", "Sosyal medya ve içerik", "Instagram, TikTok, Reels ve aylık plan"),
  ("reklam-yonetimi.html", "ads", "Google ve Meta reklamları", "Semtindeki doğru kişilere görün"),
  ("google-isletme.html", "pin", "Google İşletme ve yerel SEO", "Haritalarda bul, yorum topla"),
  ("mobil-uygulama.html", "app", "Mobil uygulama ve yazılım", "iOS, Android ve web uygulamaları"),
]

# ---------- layout ----------
SYMBOLS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="logo" viewBox="0 0 40 40"><rect width="40" height="40" rx="11" fill="#D9B24C"/><path fill="#0D1611" d="M11 8h5.6v18.4H29V32H11z"/><path fill="#0D1611" d="M20.5 21.5c.2-6.4 3.6-11 9.5-13 .4 6.3-3.1 11.2-9.5 13z"/><path fill="#D9B24C" d="M21.6 20.4c1.6-3.4 3.8-6.2 6.9-8.6-.2.4-3.6 4.8-6.9 8.6z"/></symbol>
<symbol id="wa" viewBox="0 0 24 24"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7c.1.2 1.9 2.9 4.6 4 1.7.7 2.4.8 3.2.7.5-.1 1.5-.6 1.8-1.2.2-.6.2-1.1.1-1.2l-.4-.2z"/></symbol>
</svg>'''

def header(active):
    dd = "".join(f'<a href="{h}"><span class="ic">{I[ic]}</span><span><b>{t}</b><small>{d}</small></span></a>' for h,ic,t,d in SERVICES)
    def cur(k): return ' aria-current="page"' if active == k else ""
    return f'''<a class="skip" href="#main">İçeriğe geç</a>
<header class="nav"><div class="wrap">
<a class="brand" href="index.html" aria-label="Laurus Dijital ana sayfa"><svg viewBox="0 0 40 40" aria-hidden="true"><use href="#logo"/></svg><span><b>Laurus</b><small>DİJİTAL AJANS</small></span></a>
<nav class="menu" id="menu" aria-label="Ana menü">
<div class="dd"><button type="button" aria-expanded="false" aria-controls="dd-svc">Hizmetler {I['down']}</button><div class="dd-panel" id="dd-svc" hidden>{dd}</div></div>
<a href="calismalar.html"{cur("calismalar")}>Çalışmalar</a>
<a href="fiyatlar.html"{cur("fiyatlar")}>Fiyatlar</a>
<a href="hakkimizda.html"{cur("hakkimizda")}>Hakkımızda</a>
<a href="rehber.html"{cur("rehber")}>Rehber</a>
<a class="btn btn-gold" href="#iletisim">Teklif al</a>
</nav>
<button class="burger" id="burger" aria-label="Menüyü aç" aria-expanded="false" aria-controls="menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>'''

def contact(title="İşletmeni anlat, taslağını gör.", need="Web sitesi"):
    needs = ["Web sitesi","Sosyal medya yönetimi","Google / Meta reklamı","SEO ve Google profili","Mobil uygulama","Hepsi","Emin değilim, öneri istiyorum"]
    opts = "".join(f'<option{" selected" if n==need else ""}>{n}</option>' for n in needs)
    return f'''<section id="iletisim" class="contact" aria-labelledby="h-contact"><div class="wrap cbox">
<div><span class="eyebrow">İletişim</span><h2 id="h-contact">{title}</h2>
<p class="lead">Formu doldur ya da doğrudan yaz. İşletmeni inceleyip sana ne yapabileceğimizi aynı gün gösterelim. İlk görüşme ücretsiz.</p>
<div class="direct">
<a class="js-wa" href="https://wa.me/905434309702"><span class="ic">{I['wa']}</span><span><small>WhatsApp</small><b>{PHONE_TXT}</b></span></a>
<a href="mailto:{EMAIL}"><span class="ic">{I['mail']}</span><span><small>E-posta</small><b>{EMAIL}</b></span></a>
</div></div>
<form class="quick" id="quick" novalidate>
<h3>Ücretsiz ön görüşme</h3><p>Üç alanı doldur, mesajın WhatsApp'ta hazır açılsın.</p>
<label for="f-name">Adın<input id="f-name" name="fname" autocomplete="name" required></label>
<label for="f-biz">İşletmenin adı ve sektörü<input id="f-biz" name="biz" placeholder="İşletmenin adı ve sektörü" required></label>
<label for="f-need">İhtiyacın<select id="f-need" name="need">{opts}</select></label>
<input type="hidden" id="f-note" name="note" value="">
<div class="err" id="f-err" aria-live="polite"></div>
<button class="btn btn-wa" type="submit">{I['wa']}WhatsApp'tan gönder</button>
<p class="fine">Form bilgilerini sitede saklamıyoruz; mesaj doğrudan senin WhatsApp'ından gider.</p>
</form></div></section>'''

def footer():
    FSHORT = {"Sosyal medya ve içerik":"Sosyal medya","Google ve Meta reklamları":"Google ve Meta reklamı","Google İşletme ve yerel SEO":"Google profili ve SEO","Mobil uygulama ve yazılım":"Mobil uygulama","Güzellik salonu ve nail bar":"Güzellik ve nail bar","Avukat ve danışmanlık":"Avukat ve danışman"}
    svc = "".join(f'<li><a href="{h}">{FSHORT.get(t,t)}</a></li>' for h,_,t,_ in SERVICES)
    sec = "".join(f'<li><a href="{x["slug"]}">{FSHORT.get(x["short"],x["short"])}</a></li>' for x in SECTORS)
    pin = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>'
    up = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>'
    return f'''<footer><div class="wrap">
<div class="ftop">
<div class="fbrand"><a class="brand" href="index.html" aria-label="Laurus Dijital"><svg viewBox="0 0 40 40" aria-hidden="true"><use href="#logo"/></svg><span><b>Laurus</b><small>DİJİTAL AJANS</small></span></a>
<p class="about">İstanbul merkezli dijital ajans. Web tasarım, mobil uygulama, sosyal medya yönetimi, Google Ads ve SEO; Türkiye geneline online hizmet.</p></div>
<div class="fcontact" aria-label="İletişim">
<a class="fc fc-wa js-wa" href="https://wa.me/905434309702"><span class="fc-ic">{I['wa']}</span><span class="fc-tx"><small>WhatsApp</small><b>{PHONE_TXT}</b></span><span class="fc-go" aria-hidden="true">→</span></a>
<a class="fc" href="mailto:{EMAIL}"><span class="fc-ic">{I['mail']}</span><span class="fc-tx"><small>E-posta</small><b>{EMAIL}</b></span><span class="fc-go" aria-hidden="true">→</span></a>
<div class="fc fc-static"><span class="fc-ic">{pin}</span><span class="fc-tx"><small>Konum</small><b>İstanbul · Türkiye geneli online</b></span></div>
</div></div>
<div class="flinks">
<div><h4>Hizmetler</h4><ul>{svc}</ul></div>
<div><h4>Sektörler</h4><ul>{sec}</ul></div>
<div><h4>Laurus</h4><ul><li><a href="hakkimizda.html">Hakkımızda</a></li><li><a href="calismalar.html">Çalışmalar</a></li><li><a href="fiyatlar.html">Fiyatlar</a></li><li><a href="index.html#sss">Sık sorulanlar</a></li><li><a href="rehber.html">Rehber</a></li><li><a href="web-sitesi-yaptirmak.html">Web sitesi yaptırmak</a></li><li><a href="sosyal-medya-yonetimi-fiyatlari.html">Sosyal medya fiyatları</a></li></ul></div>
</div>
<div class="fbot"><span>© 2026 Laurus Dijital · Tüm hakları saklıdır.</span><span class="fbot-r"><span>Bu site çerez kullanmaz.</span><a class="ftop-btn" href="#main" aria-label="Sayfanın başına dön">{up}<span>Başa dön</span></a></span></div>
</div></footer>
<a class="wa-float js-wa" href="https://wa.me/905434309702" aria-label="WhatsApp'tan yaz">{I['wa']}</a>'''

import json, re
def _strip(t): return re.sub(r"<[^>]+>","",t)
PAGE_META = {}  # slug -> dict(crumb=..., service=(name, price, desc))
def schemas(slug, url, title, desc):
    org = {"@type":["ProfessionalService","LocalBusiness"],"@id":BASE+"/#org","name":"Laurus Dijital","url":BASE,"logo":BASE+"/favicon.svg","image":BASE+"/og.png",
           "email":EMAIL,"telephone":PHONE_TEL,"priceRange":"₺₺","address":{"@type":"PostalAddress","addressLocality":"İstanbul","addressRegion":"İstanbul","addressCountry":"TR"},
           "areaServed":[{"@type":"City","name":"İstanbul"},{"@type":"Country","name":"Türkiye"}],
           "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"19:00"}],
           "knowsAbout":["web tasarım","web sitesi yapımı","kurumsal web sitesi","e-ticaret sitesi","sosyal medya yönetimi","Instagram hesap yönetimi","Google Ads","Meta reklamları","SEO","yerel SEO","Google İşletme Profili","mobil uygulama geliştirme","iOS uygulama","web uygulaması","yazılım geliştirme"],"description":"İstanbul merkezli dijital ajans: web tasarım, mobil uygulama, sosyal medya yönetimi, Google Ads ve SEO hizmetleri.","slogan":"İşletmeni internete taşıyoruz.","url":BASE,
           "hasOfferCatalog":{"@type":"OfferCatalog","name":"Hizmetler","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":t,"url":BASE+"/"+h.replace(".html","")}} for h,_,t,_ in SERVICES]}}
    graph=[org,{"@type":"WebSite","@id":BASE+"/#site","url":BASE,"name":"Laurus Dijital","inLanguage":"tr-TR","publisher":{"@id":BASE+"/#org"}},
           {"@type":("AboutPage" if slug=="hakkimizda.html" else "WebPage"),"@id":url+"#page","url":url,"name":title,"description":desc,"inLanguage":"tr-TR","isPartOf":{"@id":BASE+"/#site"}}]
    m = PAGE_META.get(slug,{})
    if m.get("crumb"):
        graph.append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":BASE+"/"}]+[{"@type":"ListItem","position":i+2,"name":n,"item":BASE+u} for i,(n,u) in enumerate(m["crumb"])]})
    if m.get("service"):
        n,price,d = m["service"]
        sv={"@type":"Service","name":n,"description":d,"provider":{"@id":BASE+"/#org"},"areaServed":"TR","url":url}
        if price: sv["offers"]={"@type":"Offer","price":price,"priceCurrency":"TRY","url":url+"#fiyat"}
        graph.append(sv)
    if slug in globals().get("GMAP", {}):
        g = GMAP[slug]
        graph.append({"@type":"Article","headline":g["h1"],"description":g["desc"],"inLanguage":"tr-TR","datePublished":GUIDE_DATE,"dateModified":GUIDE_DATE,
                      "author":{"@id":BASE+"/#org"},"publisher":{"@id":BASE+"/#org"},"mainEntityOfPage":url,"image":BASE+"/img/"+g["photo"]+".webp","about":g["kw"]})
    if FAQ_SINK:
        graph.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":_strip(q),"acceptedAnswer":{"@type":"Answer","text":_strip(a)}} for q,a in FAQ_SINK]})
    return json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)


META_FIX = {
 "index.html": ("Laurus Dijital | Web Tasarım, Sosyal Medya ve SEO Ajansı","Web sitesi, mobil uygulama, Instagram yönetimi, Google reklamı ve SEO. İstanbul merkezli dijital ajans; açık fiyatlar, ilk site 7 günde yayında."),
 "mobil-uygulama.html": ("Mobil Uygulama Geliştirme · İstanbul | Laurus Dijital","iOS, Android ve web uygulaması geliştirme; üyelik, abonelik ve mağaza yayını dahil. oh same., Sorbi, Sekiz8, Çınar ve Nefes'i kendi ekibimiz geliştiriyor."),
 "calismalar.html": ("Çalışmalarımız: Web, Sosyal Medya, Uygulama | Laurus Dijital","Seven For Life, Feronya, Nil Pet Kuaför, Little Paws ve @astrodefnee işlerimiz; oh same., Sorbi, Sekiz8, Çınar ve Nefes uygulamalarımız."),
 "rehber.html": ("Rehber: Web Sitesi, Sosyal Medya, Reklam, SEO | Laurus Dijital","Web sitesi yaptırmak, sosyal medya fiyatları, Google reklam bütçesi ve SEO hakkında 2026 rehberleri; açık fiyatlar ve kontrol listeleri."),
 "hakkimizda.html": ("Hakkımızda | Laurus Dijital, İstanbul Dijital Ajans","8 yılı aşkın yazılım ve dijital deneyimle web tasarım, mobil uygulama, sosyal medya, Google Ads ve SEO hizmeti veren İstanbul merkezli ajans."),
 "web-sitesi-yaptirmak.html": ("Web Sitesi Yaptırmak 2026: Fiyatlar ve Süreç | Laurus Dijital","Web sitesi yaptırmak ne kadar tutar, kaç günde biter? Site türlerine göre 2026 fiyat tablosu, gizli maliyetler ve teklif kontrol listesi."),
 "sosyal-medya-yonetimi-fiyatlari.html": ("Sosyal Medya Yönetimi Fiyatları 2026 | Laurus Dijital","Instagram hesap yönetimi 2026 fiyatları: freelancer ve ajans farkı, pakete neler dahil, reklam bütçesi ayrı mı? Açık fiyat tablosu."),
 "seo-hizmeti.html": ("SEO Hizmeti: Google'da Üst Sıralara Çıkma | Laurus Dijital","Küçük işletmeler için SEO ve yerel SEO: Google'da ve haritada öne çıkmak için ne yapılır, ne kadar sürer, ne kadar tutar?"),
 "google-reklam-yonetimi.html": ("Google Reklam Yönetimi 2026: Bütçe ve Ücret | Laurus Dijital","Google Ads 2026: küçük işletme için ne kadar bütçe gerekir, ajans ücreti ne kadar, reklam nasıl kurulur? Semte özel reklam rehberi."),
 "kuafor-dijital-pazarlama.html": ("Kuaför ve Berber için Web Sitesi ve Instagram | Laurus","Kuaför ve berberler için web sitesi, Instagram yönetimi, Google profili ve yerel reklam. WhatsApp'tan randevu, açık fiyatlar."),
 "guzellik-salonu-dijital-pazarlama.html": ("Güzellik Salonu için Sosyal Medya ve Reklam | Laurus","Güzellik salonu ve nail bar için Instagram yönetimi, web sitesi, Google profili ve Meta reklamları. Açık fiyatlar."),
 "kafe-restoran-dijital-pazarlama.html": ("Kafe ve Restoran için Web Sitesi ve Reklam | Laurus","Kafe ve restoranlar için web sitesi, menü sayfası, Instagram yönetimi, Google profili ve yerel reklam. Açık fiyatlar."),
 "klinik-dijital-pazarlama.html": ("Klinik için Web Sitesi, SEO ve Google Profili | Laurus","Klinik ve muayenehaneler için güven veren web sitesi, SEO ve Google İşletme Profili; sağlık tanıtım kurallarına uygun dil."),
 "avukat-dijital-pazarlama.html": ("Avukat için Web Sitesi ve SEO | Laurus Dijital","Avukat ve danışmanlık firmaları için web sitesi, SEO ve bilgilendirici içerik; mesleki kurallara uygun sade dil. Açık fiyatlar."),
 "emlak-dijital-pazarlama.html": ("Emlak Ofisi için Web Sitesi ve Reklam | Laurus Dijital","Emlak ofisleri için ilan sitesi, Instagram yönetimi, Google profili ve Meta reklamları; kendi markanla müşteri topla."),
 "butik-e-ticaret-dijital-pazarlama.html": ("Butik için E-ticaret Sitesi ve Instagram | Laurus","Butik ve mağazalar için satış sitesi, online ödeme, Instagram yönetimi ve Meta reklamları. Açık fiyatlar."),
 "otel-turizm-dijital-pazarlama.html": ("Otel için Google Reklamı ve SEO | Laurus Dijital","Oteller ve turizm işletmeleri için Google reklamı ve SEO; rezervasyonu kendi sitene çeken arama reklamları. Reklamlar ilk hafta yayında."),
}
def layout(slug, title, desc, body, active=""):
    title, desc = META_FIX.get(slug, (title, desc))
    url = BASE + ("/" if slug == "index.html" else "/" + slug.replace(".html",""))
    sch = schemas(slug, url, title, desc); FAQ_SINK.clear()
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/og.png">
<meta name="theme-color" content="#0D1611">
<link rel="canonical" href="{url}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/site.css">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:locale" content="tr_TR">
<meta property="og:site_name" content="Laurus Dijital">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="tr-TR" href="{url}">
<link rel="preload" href="fonts/bricolage-grotesque-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<script type="application/ld+json">{sch}</script>
</head>
<body class="pg-{slug.replace('.html','')}">
<script>try{{if("scrollRestoration" in history)history.scrollRestoration="manual";var _n=performance.getEntriesByType&&performance.getEntriesByType("navigation")[0];if(_n&&_n.type==="reload"){{if(location.hash)history.replaceState(null,"",location.pathname+location.search);window.scrollTo(0,0);addEventListener("load",function(){{window.scrollTo(0,0)}})}}}}catch(e){{}}document.documentElement.classList.add("js");try{{if(!matchMedia("(prefers-reduced-motion: reduce)").matches&&!sessionStorage.getItem("li")){{document.documentElement.classList.add("intro");sessionStorage.setItem("li","1")}}}}catch(e){{}}</script>
<div id="intro"><div class="cur c1" aria-hidden="true"></div><div class="cur c2" aria-hidden="true"></div>
<div class="in-mark" aria-hidden="true"><svg viewBox="0 0 40 40"><path class="in-l" d="M13.8 8v21.2H29"/><path class="in-leaf" d="M20.5 21.5c.2-6.4 3.6-11 9.5-13 .4 6.3-3.1 11.2-9.5 13z"/></svg><span>Laurus</span></div>
<div class="cuts" aria-hidden="true"><div class="cut" style="--i:0"><img src="img/salon-fon.webp" alt=""><b>Kuaför</b></div><div class="cut" style="--i:1"><img src="img/kafe-latte.webp" alt=""><b>Kafe</b></div><div class="cut" style="--i:2"><img src="img/dis-klinik.webp" alt=""><b>Klinik</b></div><div class="cut" style="--i:3"><img src="img/otel-havuz.webp" alt=""><b>Otel</b></div><div class="cut" style="--i:4"><img src="img/hukuk-kutuphane.webp" alt=""><b>Avukat</b></div><div class="cut" style="--i:5"><img src="img/butik-aski.webp" alt=""><b>Butik</b></div><div class="cut" style="--i:6"><img src="img/emlak-salon.webp" alt=""><b>Emlak</b></div><div class="cut" style="--i:7"><img src="img/pet-beyaz.webp" alt=""><b>Pet kuaför</b></div></div>
<div class="in-end" aria-hidden="true"><span>Senin işin için.</span><i></i></div>
<button type="button" class="in-skip" id="in-skip">Geç</button></div>
{SYMBOLS}
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/site.js"></script>
</body>
</html>
'''

def img(name, alt, eager=False, cls=""):
    return f'<img src="img/{name}.webp" alt="{alt}"{"" if eager else " loading=\"lazy\""}{f" class=\"{cls}\"" if cls else ""} decoding="async">'

# ---------- shared blocks ----------
def plans_block():
    return f'''<div class="plans">
<div class="plan"><h3>Vitrin</h3><p class="for">İnternette hiç olmayan ya da yeni açılan işletmeler için.</p><div class="price">12.000 ₺ <small>tek sefer</small></div>
{checks(["Tek sayfa web sitesi","Google İşletme Profili kurulumu","WhatsApp randevu düğmesi","İlk 8 Instagram paylaşımı","7 günde yayında"])}
<a class="btn" data-plan="Vitrin paketi" href="#iletisim">Bu paketle başla</a></div>
<div class="plan hot"><h3>Büyüme</h3><p class="for">Düzenli müşteri akışı isteyen işletmeler için aylık yönetim.</p><div class="price">20.000 ₺ <small>/ ay</small></div>
{checks(["Instagram + TikTok ya da Google profili","Ayda 12 paylaşım ve 4 Reels","Yorum ve mesajlara yanıt","Aylık içerik takvimi ve rapor","Reklam yönetimi eklenirse +7.500 ₺ / ay"])}
<a class="btn btn-gold" data-plan="Büyüme paketi" href="#iletisim">Bu paketle başla</a></div>
<div class="plan"><h3>Reklam</h3><p class="for">Hemen görünür olmak ve yeni müşteri çekmek isteyenler için.</p><div class="price">9.000 ₺ <small>/ ay</small></div>
{checks(["Google Ads ve/veya Meta reklamları","Kurulum ve hedefleme dahil","Reklam görselleri dahil","Aylık sonuç raporu","Bütçe doğrudan senin kartından"])}
<a class="btn" data-plan="Reklam paketi" href="#iletisim">Bu paketle başla</a></div>
</div>'''

def terms_block():
    return f'''<div class="terms"><span>{I['check']}Aylık paketlerde ilk 3 ay sabit, sonra istediğin ay bırakırsın</span><span>{I['check']}İki düzeltme turu her işe dahil</span><span>{I['check']}Fatura ayrıntıları ilk görüşmede netleşir</span></div>'''

FAQ_SINK = []
def faq_block(items, title="Aklındaki sorular.", sid="sss"):
    FAQ_SINK.extend(items)
    d = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items)
    return f'''<section id="{sid}" class="light" aria-labelledby="h-{sid}"><div class="wrap faq-grid">
<div><span class="eyebrow">Sık sorulanlar</span><h2 class="h2" id="h-{sid}">{title}</h2><p class="muted" style="margin-top:18px;font-size:18px">Burada olmayan bir şey mi var? WhatsApp'tan yaz, aynı gün dönelim.</p></div>
<div>{d}</div></div></section>'''

def igphone(handle, sub, av, grid, posts="Örnek", fol="tasarım", fl="—"):
    g = "".join(img(x, "") if not x.startswith("#") else f'<i style="background:{x}"></i>' for x in grid)
    return f'''<div class="igp" aria-hidden="true"><div class="s">
<div class="ig-head"><div class="ig-av">{img(av,"")}</div><div class="ig-stats"><div><b>{posts}</b>gönderi</div><div><b>{fol}</b>takipçi</div><div><b>{fl}</b>takip</div></div></div>
<div class="ig-name"><b>{handle}</b>{sub}</div>
<div class="ig-btns"><span>Takip et</span><span>Mesaj</span><span>Randevu</span></div>
<div class="ig-grid">{g}</div></div></div>'''

def site_mock(url, small, title, text, cta, photo, items):
    lst = "".join(f"<div><b>{a}</b>{b}</div>" for a,b in items)
    return f'''<div class="browser" aria-hidden="true"><div class="bar"><i></i><i></i><i></i><span class="url">{url}</span></div>
<div class="site"><div class="t"><small>{small}</small><h5>{title}</h5><p>{text}</p><span>{cta}</span></div><div class="im">{img(photo,"")}</div>
<div class="list">{lst}</div></div></div>'''

HOME_FAQ = [
 ("Fotoğrafları kim çekiyor?","Telefonla çektiğin fotoğraflar çoğu zaman yeter; nasıl çekeceğini kısa bir listeyle anlatırız. Seçmeyi, düzenlemeyi ve yerleştirmeyi biz yaparız. İstersen çekim günü de planlarız."),
 ("Reklam bütçesi fiyata dahil mi?","Hayır. Reklam bütçesi Google ve Meta'ya doğrudan senin kartından ödenir; biz yalnızca yönetim ücreti alırız. Harcanan her kuruşu kendin görürsün."),
 ("Zaten bir sitem var, ne yaparsınız?","Önce ücretsiz bakarız. Düzeltmek yetiyorsa düzeltiriz, yeniden yapmak gerekiyorsa nedenini anlatırız."),
 ("Sözleşme ne kadar sürüyor?","Tek seferlik işlerde sözleşme işin kendisidir. Aylık paketlerde ilk 3 ay sabittir, sonra her ay devam edip etmemeye sen karar verirsin."),
 ("Hesaplar ve site kimin üzerine açılıyor?","Hepsi senin adına: alan adı, Instagram, Google İşletme Profili ve reklam hesapları. Bizimle çalışmayı bıraksan da hepsi sende kalır."),
 ("Sonuç ne zaman görülür?","Site yayına girdiği gün Google'a bildirilir; Google profilinin doğrulanması birkaç gün sürebilir. Reklamlarda ilk mesajlar genelde ilk haftada gelir; sosyal medyada düzenli büyüme 2–3 ayda belirginleşir. Garanti vermeyiz, her ay rakamları birlikte görürüz."),
 ("İstanbul dışındayım, çalışabilir miyiz?","Evet. Bütün süreç WhatsApp ve görüntülü görüşmeyle ilerliyor; Türkiye'nin her yerinden çalışıyoruz."),
]

# ---------- works: real + sample designs ----------
HOTEL_NAME = "Seven For Life Thermal Hotel"

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
       svcs=["Web sitesi","Instagram yönetimi"], url="https://nilpetkuafor.com",
       note="Kadıköy'de pet kuaför. Web sitesinin tamamını biz yaptık; Instagram hesabını da içerik planından tasarıma biz yönetiyoruz.",
       did=["Web sitesinin tamamı: hizmetler, öncesi-sonrası galeri, randevu formu","Instagram yönetimi: fiyat listesi, vizyon gönderileri ve düzenli paylaşım","WhatsApp, arama ve yol tarifi düğmeleri"]),
  dict(id="lp", name="Little Paws Pet Shop", sector="Pet shop", cat="pet", kind="real", city="Çorlu, Tekirdağ",
       svcs=["Logo tasarımı","Instagram yönetimi","Görsel tasarım","Reklam kampanyaları"], url="https://www.instagram.com/corlulittlepawspetshop/", cta="Profili gör",
       note="Çorlu'daki Little Paws Pet Shop'un logosunu biz tasarladık; Instagram hesabının tamamını, tüm görselleri ve reklam kampanyalarını biz yürütüyoruz. Hesap 19 bini aşkın takipçiye ulaştı.",
       did=["Logo ve marka kimliği tasarımı","Instagram yönetimi: Reels, bilgilendirme ve tanıtım görselleri","Meta reklam kampanyaları ile mağaza ve showroom ziyaretleri"]),
  dict(id="astro", name="Astrolog Defne", sector="Astroloji içerik hesabı", cat="icerik", kind="real", city="Instagram · @astrodefnee",
       svcs=["Instagram yönetimi","İçerik tasarımı","Hesap düzeni"], url="https://www.instagram.com/astrodefnee/", cta="Profili gör",
       note="@astrodefnee Instagram hesabı: haftalık burç yorumu serisi, “Astro İnceleme” ünlü harita serisi ve tutarlı bir görsel dil. İçerik planı, tasarım ve hesap yönetimi bizde.",
       did=["Haftalık burç yorumu şablon serisi","“Astro İnceleme” ve tema gönderileri","Profil düzeni, öne çıkanlar ve düzenli paylaşım takvimi"]),
  dict(id="otel", name="Seven For Life Thermal Hotel", sector="Termal otel", cat="turizm", kind="real", city="Kuşadası",
       svcs=["Web sitesi","Google reklamı","SEO","Instagram"], url="https://sevenforlife.com",
       note="Kuşadası'nın termal oteli için web sitesi, Google reklamları, SEO ve Instagram yönetimi. Amaç: rezervasyonu komisyonlu sitelerden otelin kendi sitesine ve WhatsApp hattına çekmek.",
       did=["Rezervasyon ve bilgi talebi odaklı web sitesi","“Kuşadası termal otel” gibi aramalar için Google reklamları ve SEO","Instagram içerik planı ve hesap yönetimi"]),
  dict(id="feronya", name="Feronya Restaurant", sector="Restoran", cat="yemek", kind="real", city="Kuşadası",
       svcs=["Web sitesi","Google reklamı","SEO","Instagram"], url="https://feronyarestaurant.com",
       note="Kuşadası'nda deniz ürünleri ve Ege mutfağı sunan Feronya için web sitesi, menü sayfası, Google reklamları, SEO ve Instagram yönetimi.",
       did=["Menü, hakkımızda ve iletişim sayfalarıyla web sitesi","Restoran aramaları için Google reklamları ve yerel SEO","Instagram içerik planı ve hesap yönetimi"]),
]
WMAP = {w["id"]: w for w in WORKS}
CATS = [("hepsi","Tümü"),("pet","Pet"),("icerik","İçerik ve kişisel marka"),("yemek","Yeme-içme"),("saglik","Sağlık"),("hizmet","Hukuk ve emlak"),("perakende","Perakende"),("turizm","Turizm")]

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
    elif w["id"] in ("otel","feronya"):
        k = "seven" if w["id"]=="otel" else "feronya"
        lap = f'<img class="shot" src="img/app/{k}-d.webp" alt="{w["name"]} web sitesi" loading="lazy">'
        ph = f'<img class="shot" src="img/app/{k}-m.webp" alt="{w["name"]} mobil site" loading="lazy">'
    elif w["id"] == "lp":
        lap = '<img class="shot" src="img/app/lp-d.webp" alt="Little Paws Pet Shop Instagram profili, bilgisayar görünümü" loading="lazy">'
        ph = '<img class="shot" src="img/app/lp-m.webp" alt="Little Paws Pet Shop Instagram profili, telefon görünümü" loading="lazy">'
    elif w["id"] == "astro":
        lap = '<img class="shot" src="img/app/astro-d.webp" alt="@astrodefnee Instagram profili, bilgisayar görünümü" loading="lazy">'
        ph = '<img class="shot" src="img/app/astro-m.webp" alt="@astrodefnee Instagram profili, telefon görünümü" loading="lazy">'
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
        return f'''<article class="wfeat{' rev' if w['id']=='otel' else ''}" data-cat="{w["cat"]}"><div class="wf-vis">{w_stage(w)}</div>
<div class="wf-tx">{kind_tag(w)}<h3>{w["name"]}</h3><p class="muted">{w["sector"]}, {w["city"]}</p><p>{w.get("note") or w.get("case")}</p>{checks(w["did"])}<div class="chips">{chips}</div>
<div class="wf-act">{f'<a class="btn btn-gold" href="{w["url"]}" target="_blank" rel="noopener">{w.get("cta","Siteyi ziyaret et")}</a>' if w.get("url") else '<a class="btn btn-gold" href="#iletisim">Benim için de kur</a>'}<a class="btn btn-line" href="{href}">Detaylar</a></div></div></article>'''
    if w["id"] in ("otel","feronya"): prev = f'<img src="img/app/{"seven" if w["id"]=="otel" else "feronya"}-d.webp" alt="" loading="lazy">'
    else: prev = b_site(BMAP[w["id"]])
    return f'''<a class="wcard" href="{href}" data-cat="{w["cat"]}"><div class="wc-scr"><div class="wc-in">{prev}</div></div>
<div class="wc-tx">{kind_tag(w)}<h3>{w["name"]}</h3><p>{w["sector"]}, {w["city"]}</p><div class="chips">{chips}</div></div></a>'''

def works_block():
    chips = "".join(f'<button type="button" data-filter="{k}" aria-pressed="{"true" if k=="hepsi" else "false"}">{t}</button>' for k,t in CATS)
    feat = work_card(WMAP["nil"], featured=True)
    feat2 = work_card(WMAP["otel"], featured=True)
    cards = "".join(work_card(w) for w in WORKS if w["id"] not in ("nil","otel") and w["id"] in BMAP)
    return f'''<div class="works" data-works><div class="filters" role="group" aria-label="Sektöre göre süz">{chips}</div>{feat}{feat2}<div class="wgrid">{cards}</div><p class="knote wempty" hidden>Bu sektörde henüz yayınlanmış bir çalışma yok. Senin işin ilk olsun: aşağıdan yaz.</p></div>'''

def brand_case(w):
    stage = w_stage(w, "in-case")
    chips = "".join(f"<span>{s}</span>" for s in w["svcs"])
    extra = ""
    if w["id"] in BMAP:
        b = BMAP[w["id"]]
        sw = "".join(f'<span><i style="background:{c}"></i>{n}</span>' for c,n in b["pal"])
        extra = f'<h3>Marka dili</h3><div class="swatches">{sw}</div><p class="fonts">{b["fonts"]}</p>'
    durum = w.get("case") or w.get("note")
    link = f'<a class="btn btn-line" href="{w["url"]}" target="_blank" rel="noopener">{w.get("cta","Siteyi ziyaret et")}</a>' if w.get("url") else ""
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


# ---------- own apps ----------
APPS = [
  dict(id="ohsame", name="oh same.", kind="Mobil + web uygulaması", status="Web'de yayında · iOS sürümü yolda",
       url="https://ohsame.app", cta="oh same.'i aç", lap="ohsame-d", ph="os-world",
       desc="Nasıl hissettiğini seçiyorsun; dünyada aynı anda aynı şeyi hisseden insanları canlı bir küre üzerinde görüyorsun. “Ah, benim gibi biri daha var” dedirten bir uygulama.",
       did=["Canlı dünya küresi ve anlık sayaçlar","Apple, Google ve e-posta ile giriş; isteyen anonim kullanır","Türkçe ve İngilizce, iOS ve web aynı üründe"],
       tech=["iOS","Web uygulaması","Canlı veri","Üyelik sistemi"]),
  dict(id="sorbi", name="Sorbi", kind="Web platformu", status="sorbiapp.com'da yayında",
       url="https://sorbiapp.com", cta="Sorbi'yi aç", lap="sorbi-d", ph="sb-chart",
       desc="Doğum tarihini yazıyorsun, doğduğun anın gökyüzünü ve haritanın kaç kişide bir görüldüğünü saniyeler içinde görüyorsun. Arkasında 1,3 milyondan fazla gök anını sayan kendi hesap motorumuz var.",
       did=["Swiss Ephemeris ile test edilmiş hesap motoru","Üyelik: Google ve e-posta ile giriş","Paylaşılabilir kartlar, günlük gökyüzü ve dersler"],
       tech=["Web platformu","Hesap motoru","Üyelik","SEO"]),
  dict(id="sekiz", name="Sekiz8", kind="iOS uygulaması", status="App Store'da yayında",
       url="https://apps.apple.com/tr/app/sekiz8/id6758377312", cta="App Store'da gör", lap=None, ph="sekiz-m", ph2="sekiz-sec",
       desc="Karar veremediğinde salla. Aklındaki soruyu tut, telefonu salla ya da dokun; cevap topun içinde belirsin. Evet/hayır, kendi seçeneklerin arasından seçim ya da rastgele sayı için de aynı hareket.",
       did=["Dört mod: Sekiz, Evet/Hayır, Seç ve Sayı","Telefonu sallamayı algılayan hareket sensörü ve titreşim","Kendi seçeneklerini yazıp aralarından seçtirme, temalar"],
       tech=["iOS","App Store","React Native"]),
  dict(id="cinar", name="Çınar", kind="iOS uygulaması · yakında", status="TestFlight'ta test ediliyor", beta=True,
       url=None, cta="", lap=None, ph="cn-home", ph2="cn-agac", ph2alt="soy ağacı ekranı",
       desc="Ailenin hikâyesi, kuşaktan kuşağa. Soy ağacını kuruyorsun; büyüklerinin sesi, fotoğraflar ve anılar ailenin kendi çınarında birikiyor. Her gün biri suladıkça ağaç canlı kalıyor.",
       did=["Canlı soy ağacı ve kişi sayfaları","Büyüklerin sesinden kayıtlar ve masallar","Önemli tarihler takvimi, aile bülteni ve telefon eşleme"],
       tech=["iOS","3D ağaç","Ses kaydı","Aile hesabı"]),
  dict(id="nefes", name="Nefes", kind="iOS uygulaması · yakında", status="TestFlight'ta test ediliyor", beta=True,
       url=None, cta="", lap=None, ph="nf-main", ph2="nf-dinle", ph2alt="dua dinleme ekranı",
       desc="Sevdiğin sesten, her gün bir dua. Bulunduğun şehre göre namaz vakitleri, izin verdiğinde ezan hatırlatmaları, Kur'an okuyucu, dualar ve zikirmatik tek uygulamada; duaları sevdiklerinin sesinden dinleyebiliyorsun.",
       did=["Konuma göre namaz vakitleri ve Hicri takvim","Kur'an okuyucu, günün duası, zikirmatik ve virdler","Duaları anne, baba ya da kendi sesinden dinleme"],
       tech=["iOS","Konum","Bildirim","Abonelik"]),
]
AMAP = {a["id"]: a for a in APPS}

def app_stage(a, cls=""):
    ph = f'<div class="phone"><div class="pscr"><img class="shot" src="img/app/{a["ph"]}.webp" alt="{a["name"]} telefon ekranı" loading="lazy"></div></div>'
    if not a["lap"]:
        if a.get("ph2"):
            ph += f'<div class="phone p2"><div class="pscr"><img class="shot" src="img/app/{a["ph2"]}.webp" alt="{a["name"]} {a.get("ph2alt","seçim modu ekranı")}" loading="lazy"></div></div>'
        return f'<div class="stage solo{" duo" if a.get("ph2") else ""} {cls}">{ph}</div>'
    lap = f'<div class="laptop"><div class="lid"><div class="scr"><img class="shot" src="img/app/{a["lap"]}.webp" alt="{a["name"]} bilgisayar görünümü" loading="lazy"></div></div><div class="base"></div></div>'
    return f'<div class="stage {cls}">{lap}{ph}</div>'

def app_card(a, i=0, big=False):
    chips = "".join(f"<span>{t}</span>" for t in a["tech"])
    act = f'<a class="btn btn-gold" href="{a["url"]}" target="_blank" rel="noopener">{a["cta"]}</a>' if a["url"] else '<a class="btn btn-gold" href="#iletisim">Erken erişim iste</a>'
    return (f'<article class="appc{" appc-big" if big else ""}" id="app-{a["id"]}" data-rv style="--d:{i*90}ms"><div class="app-vis bg-{a["id"]}">{app_stage(a)}</div>'
            f'<div class="app-tx"><span class="app-kind">{a["kind"]}</span><h3>{a["name"]}</h3><p>{a["desc"]}</p>{checks(a["did"])}<div class="chips">{chips}</div>'
            f'<div class="app-foot"><span class="app-st{" beta" if a.get("beta") else ""}"><i></i>{a["status"]}</span>{act}</div></div></article>')

def apps_block():
    return '<div class="apps">' + app_card(APPS[0], 0, True) + ''.join(app_card(a, i) for i,a in enumerate(APPS[1:],1)) + '</div>'

def app_case(a):
    chips = "".join(f"<span>{t}</span>" for t in a["tech"])
    link = f'<a class="btn btn-line" href="{a["url"]}" target="_blank" rel="noopener">{a["cta"]}</a>' if a["url"] else ""
    return (f'<div class="bcase"><div class="bcase-vis bg-{a["id"]}">{app_stage(a, "in-case")}</div><div class="bcase-tx">'
            f'<div class="bcase-id"><div><b>{a["name"]}</b><small>Kendi ürünümüz, {a["kind"] if a["kind"].startswith("iOS") else a["kind"].lower()}</small></div></div>'
            f'<div class="chips">{chips}</div><h3>Ne yaptık</h3><p>{a["desc"]}</p><h3>Neler var</h3>{checks(a["did"])}'
            f'<p class="app-st{" beta" if a.get("beta") else ""}"><i></i>{a["status"]}</p>'
            f'<div class="wf-act"><a class="btn btn-gold" href="#iletisim">Uygulamamı konuşalım</a>{link}</div></div></div>')

def page_apps():
    does = [("app","iOS ve Android","Tek kod tabanıyla iki platformda çalışan, mağaza kurallarına uygun uygulamalar."),
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
{app_show(h2="Yaptığımız <br>uygulamalar.", eyebrow="Kendi ürünlerimiz")}
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
            "iOS, Android ve web uygulaması geliştirme: üyelik, abonelik, canlı veri ve mağaza yayını dahil. oh same., Sorbi, Sekiz8, Çınar ve Nefes uygulamalarını kendi ekibimiz geliştirdi.", body)



# ---------- cinematic app showcase (v10) ----------
SB_ICONS = '<svg viewBox="0 0 64 14" aria-hidden="true"><g fill="currentColor"><rect x="0" y="9" width="3" height="5" rx="1"/><rect x="5" y="6" width="3" height="8" rx="1"/><rect x="10" y="3" width="3" height="11" rx="1"/><rect x="15" y="0" width="3" height="14" rx="1"/><path d="M30 13.5l-2.6-3.2a4.2 4.2 0 0 1 5.2 0zM24.6 7a8.6 8.6 0 0 1 10.8 0l-1.5 1.8a6.2 6.2 0 0 0-7.8 0zM21.8 3.6a13 13 0 0 1 16.4 0l-1.5 1.9a10.6 10.6 0 0 0-13.4 0z"/><rect x="44" y="1.5" width="17" height="11" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><rect x="46" y="3.5" width="12" height="7" rx="1.6"/><rect x="62" y="5" width="1.6" height="4" rx=".8"/></g></svg>'

def iph(src, alt, cls="", live=""):
    return (f'<div class="iph {cls}"{f' data-live="{live}"' if live else ''}><div class="iph-scr"><div class="iph-sb"><b>9:41</b>{SB_ICONS}</div>'
            f'<img src="img/app/{src}.webp" alt="{alt}" loading="lazy" decoding="async"></div>'
            f'<span class="iph-isl" aria-hidden="true"></span><span class="iph-gl" aria-hidden="true"></span></div>')

def bwin(src, url, alt, cls=""):
    return (f'<div class="bwin {cls}"><div class="bw-bar"><i></i><i></i><i></i><span>{url}</span></div>'
            f'<img src="img/app/{src}.webp" alt="{alt}" loading="lazy" decoding="async"></div>')

SHOW = [
  dict(id="ohsame", name="oh same.", kind="Mobil + web uygulaması", tag="Farklı hayatlar. Aynı an.",
       desc="Nasıl hissettiğini seçiyorsun; dünyada aynı anda aynı şeyi hisseden insanları canlı bir küre üzerinde görüyorsun.",
       feats=["Canlı dünya küresi","Apple, Google, e-posta ile giriş","iOS ve web, TR ve EN"],
       status="Web'de yayında · iOS sürümü yolda", url="https://ohsame.app", cta="oh same.'i aç",
       icon='<img src="img/app/os-icon.webp" alt="" width="56" height="56">',
       dev=lambda: (iph("os-start","oh same. giriş ekranı","b1") + iph("os-world","oh same. dünya ekranı: şu an nasılsın?","m","globe") +
                    '<div class="fl fl-pills" aria-hidden="true"><span><i style="background:#F28A3C"></i>heyecanlı</span><span><i style="background:#E8457A"></i>mutlu</span><span><i style="background:#A44CF0"></i>sakin</span></div>'
                    '<div class="fl fl-count" aria-hidden="true"><b>340 kişi</b><span>senin gibi heyecanlı.</span><small>12\'si İstanbul\'da · 41 şehirde</small></div>')),
  dict(id="sorbi", name="Sorbi", kind="Web platformu", tag="Doğduğun an kaç kişide bir?",
       desc="Doğum tarihini yazıyorsun; doğduğun anın gökyüzünü ve haritanın kaç kişide bir görüldüğünü saniyeler içinde görüyorsun.",
       feats=["Kendi hesap motorumuz","Üyelik ve giriş sistemi","Paylaşılabilir kartlar"],
       status="sorbiapp.com'da yayında", url="https://sorbiapp.com", cta="Sorbi'yi aç",
       icon='<span class="as-ico-sorbi" aria-hidden="true">✦</span>',
       dev=lambda: (bwin("sorbi-d","sorbiapp.com","Sorbi ana sayfası, bilgisayar görünümü","bw") + iph("sb-chart","Sorbi doğum haritası ekranı","m","chart") +
                    '<div class="fl fl-img"><img src="img/app/sb-cards.webp" alt="Sorbi Güneş, Ay ve yükselen kartları" loading="lazy"></div>'
                    '<div class="fl fl-stat" aria-hidden="true"><b>1.367.496</b><span>gök anı sayıldı</span></div>')),
  dict(id="sekiz", name="Sekiz8", kind="iOS uygulaması", tag="Karar veremediğinde salla.",
       desc="Aklındaki soruyu tut, telefonu salla; cevap topun içinde belirsin. Evet/hayır, kendi seçeneklerin ya da rastgele sayı için de aynı hareket.",
       feats=["Dört mod: Sekiz, Evet/Hayır, Seç, Sayı","Sallama sensörü ve titreşim","Temalar"],
       status="App Store'da yayında", url="https://apps.apple.com/tr/app/sekiz8/id6758377312", cta="App Store'da indir",
       icon='<img src="img/app/sk-icon.webp" alt="" width="56" height="56">',
       dev=lambda: (iph("sk-sec","Sekiz8 seçim modu","l") + iph("sk-evet","Sekiz8 evet/hayır modu","r") + iph("sk-sekiz","Sekiz8 ana ekranı","m","eight") +
                    '<img class="fl fl-icon" src="img/app/sk-icon.webp" alt="" loading="lazy">')),
  dict(id="cinar", name="Çınar", kind="iOS uygulaması · TestFlight", tag="Ailenin hikâyesi, kuşaktan kuşağa.",
       desc="Soy ağacını kuruyorsun; büyüklerinin sesi, fotoğraflar ve anılar ailenin kendi çınarında birikiyor. Her gün biri suladıkça ağaç canlı kalıyor.",
       feats=["Canlı 3D soy ağacı","Büyüklerin sesinden masallar","Önemli tarihler takvimi"],
       status="TestFlight'ta test ediliyor · yakında App Store'da", beta=True, url="#iletisim", cta="Erken erişim iste",
       icon='<img src="img/app/cn-icon.webp" alt="" width="56" height="56">',
       dev=lambda: (iph("cn-agac","Çınar soy ağacı ekranı","l") + iph("cn-takvim","Çınar önemli tarihler takvimi","r") + iph("cn-home","Çınar ana ekranı: ailenin çınarı","m","tree") +
                    '<div class="fl fl-note" aria-hidden="true"><small>Anneanneyle kurabiye</small><b>▶ Dinle · 1:04</b></div>'
                    '<img class="fl fl-icon" src="img/app/cn-icon.webp" alt="" loading="lazy">')),
  dict(id="nefes", name="Nefes", kind="iOS uygulaması · TestFlight", tag="Sevdiğin sesten, her gün bir dua.",
       desc="Bulunduğun şehre göre namaz vakitleri, izin verdiğinde ezan hatırlatmaları, Kur'an okuyucu ve zikirmatik tek yerde. Duaları sevdiklerinin sesinden dinleyebiliyorsun.",
       feats=["Konuma göre vakitler","Kur'an okuyucu ve dualar","Sevdiğin sesten dua"],
       status="TestFlight'ta test ediliyor · yakında App Store'da", beta=True, url="#iletisim", cta="Erken erişim iste",
       icon='<img src="img/app/nf-icon.webp" alt="" width="56" height="56">',
       dev=lambda: (iph("nf-dinle","Nefes: duaları sevdiklerinin sesinden dinle","l") + iph("nf-kuran","Nefes Kur'an okuyucu","r") + iph("nf-main","Nefes ana ekranı: namaz vakitleri","m","nefes") +
                    '<div class="fl fl-note gold" aria-hidden="true"><small>Sıradaki vakit · İkindi</small><b>15:46</b></div>'
                    '<img class="fl fl-icon" src="img/app/nf-icon.webp" alt="" loading="lazy">')),
]

def app_show(h2="Sadece site değil. <br>Uygulama da yapıyoruz.", eyebrow="Uygulamalarımız", sid="uygulamalar"):
    tabs = "".join(f'<button type="button" role="tab" data-as-tab="{i}" aria-selected="{"true" if i==0 else "false"}"><span>0{i+1}</span>{a["name"]}</button>' for i,a in enumerate(SHOW))
    scenes = ""
    for i,a in enumerate(SHOW):
        feats = "".join(f"<li>{f}</li>" for f in a["feats"])
        scenes += (f'<article class="as-scene as-{a["id"]}{" on" if i==0 else ""}" data-i="{i}" aria-label="{a["name"]}">'
                   f'<div class="as-sbg" aria-hidden="true"><i class="g1"></i><i class="g2"></i><i class="g3"></i></div>'
                   f'<div class="wrap as-grid"><div class="as-tx">'
                   f'<div class="as-id"><span class="as-ico">{a["icon"]}</span><span class="as-kind">{a["kind"]}</span></div>'
                   f'<h3 class="as-name">{a["name"]}</h3><p class="as-tag">{a["tag"]}</p><p class="as-desc">{a["desc"]}</p>'
                   f'<ul class="as-feats">{feats}</ul>'
                   f'<div class="as-foot">{f'<a class="btn as-cta" href="{a["url"]}">{a["cta"]}</a>' if a.get("beta") else f'<a class="btn as-cta" href="{a["url"]}" target="_blank" rel="noopener">{a["cta"]} <span aria-hidden="true">↗</span></a>'}<span class="as-st{" beta" if a.get("beta") else ""}"><i></i>{a["status"]}</span></div>'
                   f'</div><div class="as-dev"><div class="as-dv-in">{a["dev"]()}</div></div></div></article>')
    return (f'<section id="{sid}" class="appshow" data-appshow aria-labelledby="h-{sid}"><div class="as-pin">'
            f'{scenes}'
            f'<div class="wrap as-head"><div><span class="eyebrow">{eyebrow}</span><h2 id="h-{sid}">{h2}</h2></div>'
            f'<div class="as-tabs" role="tablist" aria-label="Uygulamalar">{tabs}<i class="as-bar" aria-hidden="true"><b data-as-bar></b></i></div></div>'
            f'</div></section>')

# ---------- pages ----------
def tabs(items, label):
    btns = "".join(f'<button type="button" role="tab" id="t-{i}" aria-controls="{i}" aria-selected="{"true" if n==0 else "false"}"{"" if n==0 else " tabindex=\"-1\""}>{t}</button>' for n,(i,t,_) in enumerate(items))
    pans = "".join(f'<div class="tabpanel" role="tabpanel" id="{i}" aria-labelledby="t-{i}"{"" if n==0 else " hidden"}>{h}</div>' for n,(i,t,h) in enumerate(items))
    return f'<div class="tabs" data-tabs><div class="tablist" role="tablist" aria-label="{label}">{btns}</div>{pans}</div>'

def faq_list(items):
    FAQ_SINK.extend(items)
    return '<div class="faq-list">' + "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items) + "</div>"

def mini_plans():
    P = [("Vitrin","12.000 ₺","tek sefer","Yeni açılan ya da internette olmayan işletmeler",["Tek sayfa site","Google profili kurulumu","7 günde yayında"],""),
         ("Büyüme","20.000 ₺","/ ay","Düzenli müşteri akışı isteyenler",["Ayda 12 paylaşım + 4 Reels","Yorum ve mesaj yönetimi","Aylık rapor"],"hot"),
         ("Reklam","9.000 ₺","/ ay","Hemen görünür olmak isteyenler",["Google ve/veya Meta","Kurulum ve görseller dahil","Bütçe senin kartından"],"")]
    out = []
    for n,p,u,f,l,h in P:
        tag = '<span class="tag">Önerilen</span>' if h else ''
        bc = 'btn-gold' if h else 'btn-ink'
        out.append(f'<div class="kplan {h}">{tag}<h3>{n}</h3><p class="for">{f}</p><div class="price">{p} <small>{u}</small></div>{checks(l)}<a class="btn {bc}" data-plan="{n} paketi" href="#iletisim">Bu paketle başla</a></div>')
    return '<div class="kplans">' + "".join(out) + '</div>'

def mimg(name, alt=""):
    return f'<img src="img/mock/{name}.webp" alt="{alt}" loading="lazy" decoding="async">'

REEL_COLS = [
  ["site-nil","ig-os","site-otel","ig-astro"],
  ["ig-feronya","site-os","ig-nil","site-sb"],
  ["site-astro","ig-sb","site-feronya","ig-otel"],
  ["ig-sk","site-otel","ig-lp","site-nil"],
  ["site-sb","ig-lp","site-feronya","ig-os"],
  ["ig-otel","site-astro","ig-sk","site-os"],
]

def reel():
    cols = ""
    for i, col in enumerate(REEL_COLS):
        tiles = "".join(f'<div class="tile {"t-ig" if n.startswith("ig") else "t-site"}"><img src="img/mock/sm/{n}.webp" alt="" decoding="async"{" loading=\"lazy\"" if i>2 else ""}></div>' for n in col)
        cols += f'<div class="rcol" style="--dur:{38+i*5}s;--dir:{"normal" if i%2==0 else "reverse"}"><div class="rtrack">{tiles}{tiles}</div></div>'
    return f'<div class="reel" aria-hidden="true"><div class="reel-plane">{cols}</div></div>'

def slide(w, i):
    chips = "".join(f"<span>{s}</span>" for s in w["svcs"])
    link = f'<a class="btn btn-gold" href="{w["url"]}" target="_blank" rel="noopener">{w.get("cta","Siteyi ziyaret et")}</a>' if w.get("url") else f'<a class="btn btn-gold" href="calismalar.html#{w["id"]}">Taslağı incele</a>'
    desc = w.get("note") or w.get("case")
    return f'''<article class="slide" style="--i:{i}"><div class="sl-vis bg-{w["id"]}"><div class="stage"><div class="laptop"><div class="lid"><div class="scr">{mimg("site-"+w["id"], w["name"]+" web sitesi")}</div></div><div class="base"></div></div><div class="phone"><div class="pscr">{mimg("ig-"+w["id"], w["name"]+" mobil görünüm")}</div></div></div></div>
<div class="sl-tx">{kind_tag(w)}<h3>{w["name"]}</h3><p class="sl-sub">{w["sector"]}, {w["city"]}</p><p class="sl-d">{desc}</p><div class="chips">{chips}</div><div class="sl-act">{link}</div></div></article>'''

MANIFESTO = "Müşterin seni önce Google'da arar, sonra Instagram'da inceler, en son WhatsApp'tan yazar. Bu üç anın üçünü de biz kuruyoruz, sen işine bakıyorsun."

def page_index():
    svc = [
      ("web-tasarim.html","site-otel","Web sitesi","Telefonda hızlı açılan, WhatsApp'tan randevu getiren site.","12.000 ₺'den"),
      ("sosyal-medya.html","ig-astro","Sosyal medya","Aylık plan, tasarım, Reels ve mesaj yönetimi.","Aylık 12.000 ₺'den"),
      ("reklam-yonetimi.html","site-feronya","Google ve Meta reklamı","Seni arayan kişinin karşısına ilk sen çık.","9.000 ₺ / ay"),
      ("google-isletme.html","harita","Google profili ve SEO","Haritada ve aramalarda öne çıkman için profilini ve siteni hazırlarız.","Vitrin paketine dahil"),
    ]
    def sv_img(n): return mimg(n) if (n.startswith("site-") or n.startswith("ig-")) else img(n,"")
    cards = "".join(f'<a class="svc3" href="{h}" data-rv style="--d:{i*90}ms"><div class="ph">{sv_img(p)}</div><div class="in"><h3>{t}</h3><p>{d}</p><span class="pr">{pr}</span></div></a>' for i,(h,p,t,d,pr) in enumerate(svc))
    words = "".join(f'<span>{w}</span> ' for w in MANIFESTO.split(" "))
    slides = "".join(slide(w, i) for i, w in enumerate(WORKS))
    steps = [("1. gün","Tanışma","15 dakikalık görüşme; işletmeni ve hedefini dinleriz."),("2–3. gün","İlk taslak","Taslağı görürsün. Beğenmezsen ödeme yok."),("4–6. gün","Tamamlama","Metin, fotoğraf, Google profili. İki düzeltme turu."),("7. gün","Yayında","Siten açılır, hesapların hazır.")]
    st = "".join(f'<li data-rv style="--d:{i*120}ms"><span class="n">{i+1}</span><small>{d}</small><h3>{t}</h3><p>{x}</p></li>' for i,(d,t,x) in enumerate(steps))
    body = f'''
<section class="hero3" aria-labelledby="h-hero">
{reel()}
<div class="h3-shade" aria-hidden="true"></div>
<div class="wrap h3-in">
<h1 id="h-hero"><span class="ln"><span>İşletmeni</span></span> <span class="ln"><span>internete</span></span> <span class="ln"><span>taşıyoruz.</span></span></h1>
<p class="lead">İstanbul merkezli dijital ajans: web tasarım, mobil uygulama, sosyal medya yönetimi, Google reklamı ve SEO. Kuaförden otele, kliniğe kadar her işletme için tek ekip.</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="#calismalar">İşlerimizi gör</a></div>
</div>
<a class="h3-scroll" href="#manifesto" aria-label="Aşağı kaydır"><i></i></a>
</section>

<section id="manifesto" class="mani" aria-label="Ne yapıyoruz"><div class="mani-pin"><div class="wrap"><p class="mani-tx" data-mani>{words}</p></div></div></section>

<section id="hizmetler" class="light ksec" aria-labelledby="h-svc"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Hizmetler</span><h2 id="h-svc">Web tasarım, sosyal medya ve SEO hizmetleri.</h2></div><p>Tek hizmetle başla ya da hepsini birlikte al.</p></div>
<div class="svc3-row snap">{cards}</div>
</div></section>

<section id="calismalar" class="works3" aria-labelledby="h-works">
<div class="w3-pin"><div class="wrap w3-head" data-rv><div><span class="eyebrow">Çalışmalarımız</span><h2 id="h-works">Yaptığımız işler.</h2></div><p>Müşterilerimiz için yaptığımız gerçek işler: Seven For Life, Feronya, Nil Pet Kuaför, Little Paws ve @astrodefnee. <a class="link" href="calismalar.html">Hepsini incele</a></p></div>
<div class="w3-track snap" data-hscroll>{slides}</div>
<div class="wrap w3-prog" aria-hidden="true"><i data-hprog></i></div></div>
</section>

{app_show()}

<section id="nasil" class="light ksec" aria-labelledby="h-proc"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Nasıl çalışıyoruz</span><h2 id="h-proc">İlk görüşmeden yayına 7 gün.</h2></div><p>Önce taslağı görürsün, sonra karar verirsin. Ödemenin yarısı taslağı beğendiğinde.</p></div>
<ol class="proc3" data-line><span class="pl" aria-hidden="true"><i></i></span>{st}</ol>
</div></section>

<section id="fiyatlar" class="ksec" aria-labelledby="h-price"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Fiyatlar</span><h2 id="h-price">Açık fiyat, sürpriz yok.</h2></div><p><a class="link" href="fiyatlar.html">Tüm fiyatları gör</a></p></div>
<div data-rv class="plans-wrap">{mini_plans()}</div>
</div></section>

<section id="sss" class="light ksec" aria-labelledby="h-sss"><div class="wrap kfaq">
<div data-rv><span class="eyebrow">Sık sorulanlar</span><h2 id="h-sss">Aklındaki sorular.</h2><p class="muted">Burada yoksa WhatsApp'tan yaz, aynı gün dönelim.</p></div>
{faq_list(HOME_FAQ[:4])}
</div></section>
{contact()}
'''
    return ("Laurus Dijital | Web Tasarım, Sosyal Medya Yönetimi ve SEO Ajansı · İstanbul",
            "Web sitesi yaptırmak, mobil uygulama, Instagram ve sosyal medya yönetimi, Google reklamı ve SEO için İstanbul merkezli dijital ajans. Fiyatlar açık, ilk site 7 günde yayında.", body)

GUIDE_FOR = {"web-tasarim.html":'Piyasa fiyatlarını merak ediyorsan: <a class="link" href="web-sitesi-yaptirmak.html">Web sitesi yaptırmak rehberi</a>.',"sosyal-medya.html":'Piyasa karşılaştırması: <a class="link" href="sosyal-medya-yonetimi-fiyatlari.html">Sosyal medya yönetimi fiyatları 2026</a>.',"reklam-yonetimi.html":'Bütçe rehberi: <a class="link" href="google-reklam-yonetimi.html">Google reklam yönetimi 2026</a>.',"google-isletme.html":'Detaylı rehber: <a class="link" href="seo-hizmeti.html">SEO hizmeti rehberi</a>.'}

def service_page(slug, crumb, h1, lead, photo, photo_alt, plain_q, plain_a, does, visual, deliver_title, deliverables, month, price_rows, faq, need):
    dg = "".join(f'<div class="do"><span class="ic">{I[ic]}</span><h3>{t}</h3><p>{d}</p></div>' for ic,t,d in does)
    rows = "".join(f"<tr><td>{a}<small>{b}</small></td><td>{c}</td></tr>" for a,b,c in price_rows)
    t_do = f'<div class="kplain"><b>{plain_q}</b><p>{plain_a}</p></div><div class="do-grid">{dg}</div>'
    t_del = f'<div class="ksplit"><div class="vis"><span class="extag">Gerçek iş</span>{visual}</div><div><h3 class="kh3">{deliver_title}</h3>{checks(deliverables)}</div></div>'
    items = [("ne-yapiyoruz","Neler yapıyoruz",t_do),("teslim","Elinde olanlar",t_del)]
    if month:
        items.append(("ritim","Bir ay nasıl geçer",'<div class="month">' + "".join(f"<div><b>{w}</b><h4>{t}</h4><p>{d}</p></div>" for w,t,d in month) + '</div>'))
    items.append(("fiyat","Fiyat",f'<div class="table"><table><thead><tr><th scope="col">Paket</th><th scope="col">Fiyat</th></tr></thead><tbody>{rows}</tbody></table></div>{terms_block()}<p class="knote">Birleşik fiyatlar için <a class="link" href="fiyatlar.html">tüm fiyatlara</a> bak. {GUIDE_FOR.get(slug,"")}</p>'))
    items.append(("sss","Sık sorulanlar",faq_list(faq)))
    T = tabs(items, crumb + " ayrıntıları")
    body = f'''
<section class="phero" aria-labelledby="h-page"><div class="wrap">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / <a href="index.html#hizmetler">Hizmetler</a> / {crumb}</nav>
<h1 id="h-page">{h1}</h1><p class="lead">{lead}</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="#fiyat">Fiyatı gör</a></div></div>
<div class="ph">{img(photo, photo_alt, eager=True)}</div>
</div></section>
<section class="light ksec" aria-label="{crumb} ayrıntıları"><div class="wrap">
{T}
</div></section>
{contact(need=need)}
'''
    return body

def page_web():
    visual = f'<div class="bcase-vis bg-feronya">{w_stage(WMAP["feronya"], "in-case")}</div><p class="knote" style="margin-top:12px">Feronya Restaurant: web sitesi, menü ve iletişim sayfaları.</p>'
    body = service_page("web-tasarim.html","Web tasarım","İşletmen için telefonda hızlı açılan, randevu getiren bir site.",
      "Müşterilerinin çoğu seni telefondan arıyor. Biz de siteyi önce telefona göre kuruyoruz: açılır açılmaz ne yaptığın, nerede olduğun ve nasıl randevu alınacağı belli.",
      "tasarim-laptop","Masada açık dizüstü bilgisayarda web sitesi tasarımı",
      "Instagram'ım var, siteye neden ihtiyacım olsun?",
      "Google'da “kuaför Kadıköy” arayan biri Instagram profilini değil, siteleri ve haritayı görür. Site, Google'ın seni tanımasını sağlar; fiyat listen, hizmetlerin, adresin ve randevu düğmen tek yerde durur. Instagram vitrinin, site ise dükkânının tabelası gibi: ikisi birlikte çalışınca güven artar.",
      [("web","Tasarım ve metin","Sektörüne uygun, sade ve güven veren tasarım. Metinleri biz yazarız, sen onaylarsın."),
       ("phone","Telefon öncelikli","Ziyaretçilerin çoğu telefondan gelir; site önce telefonda kusursuz çalışır."),
       ("chat","WhatsApp ve arama","Her sayfada tek dokunuşla WhatsApp'tan yazma ve arama düğmesi."),
       ("search","Google'da bulunma","Başlıklar, açıklamalar, harita bağlantısı ve Search Console kurulumu."),
       ("lock","Alan adı ve SSL","Alan adı senin adına alınır, güvenli bağlantı (https) kurulur."),
       ("bolt","Hız","Fotoğraflar sıkıştırılır, sayfa telefonda hızlı açılır.")],
      visual, "7 günün sonunda elinde olanlar",
      ["Telefon ve bilgisayarda çalışan site","Senin adına alınmış alan adı (örnek: isletmen.com.tr)","Hizmet, fiyat ve iletişim bilgilerin","WhatsApp randevu ve arama düğmeleri","Google Haritalar bağlantısı","Google Search Console kaydı","Siteyi nasıl güncelleyeceğini anlatan kısa rehber"],
      None,
      [("Tek sayfa site (Vitrin paketi)","Google İşletme kurulumu ve ilk 8 Instagram paylaşımı dahil","12.000 ₺"),("Kurumsal site","5 sayfa: hizmetler, hakkında, galeri, iletişim formu, temel SEO","22.000 ₺"),("Satış sitesi","Ürün kataloğu, online ödeme, sipariş paneli","35.000 ₺"),("Site bakımı","Güncellemeler, küçük değişiklikler, yedekleme","1.500 ₺ / ay")],
      [("Alan adı ve hosting ücreti ayrı mı?","Alan adı yıllık yaklaşık 500 – 1.200 ₺ tutar ve senin adına alınır; ilk yılı fiyata dahildir. Barındırmayı ücretsiz katmanlarda kuruyoruz, ek aylık ücret çıkmaz."),
       ("Siteyi sonra kendim değiştirebilir miyim?","Evet. Fiyat ve saat gibi sık değişen bilgileri nasıl güncelleyeceğini gösteririz. İstersen bakım paketiyle bunu biz yaparız."),
       ("Fotoğraflarım yok, ne olacak?","Telefonla nasıl çekeceğini anlatırız; gerekirse lisanslı stok fotoğraflarla başlarız, sen çektikçe değiştiririz."),
       ("Hazır şablon mu kullanıyorsunuz?","Hayır. Her site işletmenin renklerine, sektörüne ve müşterisine göre tasarlanır.")],
      "Web sitesi")
    return ("Web Tasarım ve Web Sitesi Yapımı · İstanbul | Laurus Dijital","Web sitesi yaptırmak isteyen işletmeler için telefonda hızlı açılan, Google'da bulunan siteler. Tek sayfa site 12.000 ₺, 7 günde yayında, alan adı senin adına.", body)

def page_social():
    visual = f'<div class="bcase-vis bg-astro">{w_stage(WMAP["astro"], "in-case")}</div><p class="knote" style="margin-top:12px">@astrodefnee: içerik planı, tasarım ve hesap yönetimi.</p>'
    body = service_page("sosyal-medya.html","Sosyal medya ve içerik","Instagram'ın düzenli, canlı ve randevu getiren bir vitrin olsun.",
      "İçerik planını biz hazırlarız, tasarlar, paylaşır ve mesajlara yanıt veririz. Sen işine bakarsın; hesabın hiçbir hafta boş kalmaz.",
      "cekim","Telefonla bir mekânı çeken kişinin elleri",
      "Ben zaten paylaşım yapıyorum, fark ne olacak?",
      "Fark düzen ve amaçtır. Rastgele paylaşım yerine her ay bir plan çıkarırız: hangi gün hangi içerik, hangi kampanya, hangi soruya cevap. Tasarımlar aynı dili konuşur, Reels'ler müşterinin merak ettiğini gösterir, her paylaşımın sonunda randevuya giden bir yol olur.",
      [("cal","Aylık içerik planı","Ayın başında takvimi görürsün, onay verirsin, gerisini biz yürütürüz."),
       ("pen","Tasarım ve metin","Gönderi, hikâye ve kapak tasarımları; açıklamalar ve etiketler."),
       ("video","Reels ve kısa video","Telefonla çekilen görüntüleri kurgu, altyazı ve müzikle Reels'e çeviririz."),
       ("chat","Yorum ve mesajlar","Gelen soruları yanıtlar, randevu taleplerini sana iletiriz."),
       ("star","Hikâye ve kampanya","Haftalık hikâyeler, özel gün ve sezon kampanyaları."),
       ("chart","Aylık rapor","Kaç kişi gördü, kaç mesaj geldi, en iyi içerik hangisiydi: tek sayfa.")],
      visual, "Her ay elinde olanlar",
      ["Onayladığın aylık içerik takvimi","Ayda 8 ya da 12 tasarlanmış gönderi","Ayda 4 Reels (Büyüme paketinde)","Haftalık hikâyeler","Yorum ve mesaj yönetimi","Tek sayfalık aylık rapor"],
      [("1. hafta","Plan ve onay","Ayın kampanyalarını ve içerik takvimini birlikte netleştiririz."),("2. hafta","Çekim ve tasarım","Senden gelen fotoğraf ve videolarla tasarımlar ve Reels hazırlanır."),("3. hafta","Paylaşım ve yanıt","İçerikler planlanan günlerde çıkar, mesajlar yanıtlanır."),("4. hafta","Rapor","Ne işe yaradı, ne yaramadı; gelecek aya not düşülür.")],
      [("Başlangıç","Instagram, ayda 8 gönderi ve 8 hikâye, aylık rapor","12.000 ₺ / ay"),("Büyüme","Instagram + TikTok ya da Google profili, 12 gönderi ve 4 Reels, yorum ve mesaj yönetimi","20.000 ₺ / ay"),("Reklam eklentisi","Sosyal medya paketiyle birlikte Google ve/veya Meta reklam yönetimi","+7.500 ₺ / ay")],
      [("Çekimi kim yapacak?","Çoğu işletmede telefonla çekilen görüntüler yeterli. Neyi, nasıl çekeceğini haftalık kısa bir listeyle sana göndeririz."),
       ("Paylaşımları onaylamadan yayınlar mısınız?","Hayır. Ayın başında takvimi ve tasarımları onaylarsın; onaylanmayan hiçbir şey paylaşılmaz."),
       ("Takipçi sayısı artacak mı?","Takipçi satın almayız ve bunu hedef olarak koymayız. Asıl ölçtüğümüz şey gelen mesaj ve randevu sayısı."),
       ("Hesabımın şifresini vermem gerekiyor mu?","Hayır. Instagram'ı Meta İşletme Hesabı üzerinden yetkiyle yönetiriz; şifren sende kalır.")],
      "Sosyal medya yönetimi")
    return ("Sosyal Medya Yönetimi ve Instagram Hesap Yönetimi | Laurus Dijital","Instagram ve TikTok yönetimi, aylık içerik planı, Reels ve mesaj yönetimi. Aylık 12.000 ₺'den başlayan açık fiyatlar.", body)

def page_ads():
    visual = f'<div class="bcase-vis bg-otel">{w_stage(WMAP["otel"], "in-case")}</div><p class="knote" style="margin-top:12px">Seven For Life Thermal Hotel: Google reklamları ve SEO.</p>'
    body = service_page("reklam-yonetimi.html","Google ve Meta reklamları","Seni arayan kişinin karşısına, semtindeki doğru insana çık.",
      "Google'da hizmetini arayanlara ve Instagram'da çevrendeki kişilere görünen reklamlar kurarız. Bütçe senin kartından gider, her kuruşu görürsün.",
      "google-arama","Telefonda Google arama ekranı",
      "Reklama para harcamak mantıklı mı?",
      "Doğru kurulduğunda evet: reklam, seni zaten arayan ya da çevrende yaşayan kişiye gösterilir. Örneğin yalnızca salonuna 3 km mesafedeki ve “kuaför” arayan kişiler. Küçük bir bütçeyle başlar, ilk haftalarda neyin işe yaradığını görür, bütçeyi ona göre büyütürüz. İşe yaramayan reklamı durdururuz.",
      [("search","Google arama reklamı","“Yakınımdaki kuaför”, “Kadıköy kahve” gibi aramalarda üst sıralarda görün."),
       ("pin","Harita reklamı","Google Haritalar'da çevrendeki kişilere öne çıkan işaretle görün."),
       ("ig","Instagram ve Facebook","Semtindeki, ilgi alanı uyan kişilere mesaj ve randevu odaklı reklam."),
       ("target","Hedefleme","Bölge, yaş, saat ve ilgi alanı; boşa giden gösterimleri kapatırız."),
       ("pen","Reklam görselleri","Reklam metni, görseli ve kısa videosu bizden."),
       ("chart","Aylık sonuç raporu","Kaç kişi gördü, tıkladı, aradı ya da yazdı; mesaj başına maliyet.")],
      visual, "Reklam paketinde elinde olanlar",
      ["Senin adına açılmış Google Ads ve Meta reklam hesabı","Kurulmuş ve hedeflenmiş kampanyalar","Reklam metni ve görselleri","Arama ve mesaj takibi (kaç kişi yazdı, kaç kişi aradı)","Haftalık kontrol ve iyileştirme","Tek sayfalık aylık rapor"],
      None,
      [("Reklam yönetimi","Google Ads ve/veya Meta reklamları, kurulum ve görseller dahil","9.000 ₺ / ay"),("Sosyal medya paketiyle birlikte","Başlangıç ya da Büyüme paketine eklendiğinde","7.500 ₺ / ay"),("Reklam bütçesi","Doğrudan senin kartından Google ve Meta'ya ödenir. Önerimiz günlük 150–300 ₺ ile başlamak","Sana ait")],
      [("Ne kadar bütçe ayırmalıyım?","Yerel işletmeler için günlük 150–300 ₺ ile başlamayı öneririz. İlk 2–3 haftanın sonuçlarına göre birlikte karar veririz."),
       ("Sonuç garantisi veriyor musunuz?","Hayır, kimse dürüstçe veremez. Garanti ettiğimiz şey şeffaflık: her ay rakamları görürsün, işe yaramayanı durdururuz."),
       ("Reklam hesabı kimin olacak?","Senin. Hesap senin adına açılır, biz yetkiyle yönetiriz. Ayrılırsan geçmiş verilerle birlikte hesap sende kalır."),
       ("Google Partner misiniz?","Henüz değiliz; bu rozet yüksek yönetilen bütçe şartına bağlı. Kampanyaları Google Ads ve Meta reklam araçlarında kurup yönetiyoruz.")],
      "Google / Meta reklamı")
    return ("Google Ads ve Meta (Instagram) Reklam Yönetimi | Laurus Dijital","Google arama, harita ve Instagram reklamları. Aylık 9.000 ₺ yönetim ücreti, bütçe senin kartından, her ay şeffaf rapor.", body)

def page_gbp():
    visual = f'<div class="bcase-vis bg-nil">{w_stage(WMAP["nil"], "in-case")}</div><p class="knote" style="margin-top:12px">Nil Pet Kuaför: web sitesinin tamamı ve Instagram yönetimi.</p>'
    body = service_page("google-isletme.html","Google İşletme ve yerel SEO","Google Haritalar'da seni arayan ilk bakışta güvensin.",
      "Google İşletme Profili, müşterinin seni haritada bulduğu kartvizittir. Fotoğrafları, saatleri, hizmetleri ve yorumları düzenler, semtindeki aramalarda öne çıkarırız.",
      "harita","Telefonda Google Haritalar ve yakındaki işletmeler",
      "Google İşletme Profili nedir?",
      "Google'da ya da haritada işletmenin adını veya “yakınımdaki …” diye arandığında sağda ya da üstte çıkan kart. Ücretsizdir ama çoğu işletmede eksik kalır: fotoğraf yok, saatler yanlış, yorumlar yanıtsız. Doğru düzenlenmiş bir profil, siteden bile önce müşteri getirir.",
      [("pin","Profil kurulumu","Profil yoksa açarız, varsa sahipliğini doğrularız."),
       ("web","Fotoğraf ve bilgi","Fotoğraf, logo, saatler, hizmet listesi, menü ve açıklama."),
       ("star","Yorum akışı","Müşterine gönderebileceğin yorum isteme bağlantısı ve mesaj şablonu."),
       ("chat","Yorum yanıtları","Gelen yorumlara nazik ve tutarlı yanıtlar."),
       ("cal","Haftalık gönderi","Kampanya ve duyuruları profilde gönderi olarak paylaşırız."),
       ("search","Yerel arama ayarları","Kategori, hizmet bölgesi ve anahtar kelimelerle doğru aramada çıkma.")],
      visual, "Bu hizmette elinde olanlar",
      ["Doğrulanmış ve senin adına kayıtlı profil","Güncel saatler, fotoğraflar ve hizmet listesi","Yorum isteme bağlantısı ve WhatsApp mesaj şablonu","Yanıtlanmış yorumlar","Siteyle ve Instagram'la bağlantı"],
      None,
      [("Profil kurulumu ve düzeni","Vitrin paketinin içinde","Vitrin paketine dahil"),("Aylık profil yönetimi","Haftalık gönderi, yorum yanıtı, fotoğraf güncelleme","Büyüme paketine dahil")],
      [("Profilim zaten var ama ben açmadım, ne olacak?","Sahiplik talebiyle profili sana devrederiz. Google bunun için kısa bir doğrulama ister, adım adım birlikte yaparız."),
       ("Kötü yorumları sildirebilir misiniz?","Kurallara aykırı yorumları Google'a bildiririz; geri kalanına yapıcı bir yanıt yazarız. Sahte yorum ekleme hizmeti vermeyiz."),
       ("Adresimi göstermek istemiyorum, olur mu?","Evet. Eve hizmet veren ya da adres göstermek istemeyen işletmeler için hizmet bölgesi seçeneği var.")],
      "Google İşletme profili")
    return ("Yerel SEO ve Google İşletme Profili Hizmeti | Laurus Dijital","Google Haritalar'da öne çıkın: profil kurulumu, fotoğraflar, saatler, yorum akışı ve yerel arama ayarları.", body)

def page_cases():
    T = tabs([(w["id"], {"otel":"Seven For Life","feronya":"Feronya"}.get(w["id"], w["name"]), brand_case(w)) for w in WORKS] + [(a["id"], a["name"], app_case(a)) for a in APPS], "Çalışmalar")
    body = f'''
<section class="phero" aria-labelledby="h-page" style="padding-bottom:40px"><div class="wrap" style="grid-template-columns:1fr">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / Çalışmalar</nav>
<h1 id="h-page">Ne yaptığımızı gör.</h1>
<p class="lead">Müşterilerimiz için yaptığımız işler (Seven For Life, Feronya, Nil Pet Kuaför, Little Paws Pet Shop, @astrodefnee) ve kendi geliştirdiğimiz uygulamalar (oh same., Sorbi, Sekiz8, Çınar, Nefes).</p>
</div>
</div></section>
<section class="ksec" aria-label="Çalışmalar" style="padding-top:24px"><div class="wrap">{T}</div></section>
{contact()}
'''
    return ("Çalışmalarımız: Web Sitesi, Sosyal Medya, Reklam ve Uygulama | Laurus Dijital","Seven For Life Thermal Hotel, Feronya Restaurant, Nil Pet Kuaför, Little Paws Pet Shop ve @astrodefnee için web sitesi, logo, Instagram, reklam ve SEO işleri; oh same., Sorbi, Sekiz8, Çınar ve Nefes uygulamalarımız.", body)

def page_prices():
    rows = [
      ("Web sitesi", [("Tek sayfa site · Vitrin paketi","Site, Google İşletme kurulumu, WhatsApp düğmesi, ilk 8 Instagram paylaşımı. 7 günde yayında.","12.000 ₺"),("Kurumsal site","5 sayfa: hizmetler, hakkında, galeri, iletişim formu, temel SEO","22.000 ₺"),("Satış sitesi","Ürün kataloğu, online ödeme, sipariş paneli","35.000 ₺"),("Site bakımı","Güncellemeler, küçük değişiklikler, yedekleme","1.500 ₺ / ay")]),
      ("Sosyal medya", [("Başlangıç","Instagram, ayda 8 gönderi ve 8 hikâye, aylık rapor","12.000 ₺ / ay"),("Büyüme","Instagram + TikTok ya da Google profili, 12 gönderi, 4 Reels, yorum ve mesaj yönetimi","20.000 ₺ / ay")]),
      ("Reklam", [("Google ve/veya Meta reklam yönetimi","Kurulum, hedefleme, görseller ve aylık rapor dahil. Bütçe senin kartından.","9.000 ₺ / ay"),("Sosyal medya paketiyle birlikte","Başlangıç ya da Büyüme paketine eklendiğinde","7.500 ₺ / ay")]),
    ]
    ids = {"Web sitesi":"f-web","Sosyal medya":"f-sosyal","Reklam":"f-reklam"}
    tables = tabs([(ids[g], g, '<div class="table"><table><thead><tr><th scope="col">Hizmet</th><th scope="col">Fiyat</th></tr></thead><tbody>' + "".join(f"<tr><td>{a}<small>{b}</small></td><td>{c}</td></tr>" for a,b,c in items) + "</tbody></table></div>") for g,items in rows], "Hizmet fiyatları")
    body = f'''
<section class="phero" aria-labelledby="h-page" style="padding-bottom:48px"><div class="wrap" style="grid-template-columns:1fr">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / Fiyatlar</nav>
<h1 id="h-page">Tüm fiyatlar, tek sayfada.</h1>
<p class="lead">Teklif beklemen gerekmez. Ne alacağını ve ne ödeyeceğini burada görürsün; fatura ayrıntıları ilk görüşmede netleşir.</p></div>
</div></section>
<section class="light ksec" aria-labelledby="h-plans"><div class="wrap">
<div class="khead"><div><span class="eyebrow">Paketler</span><h2 id="h-plans">Çoğu işletme buradan başlıyor.</h2></div><p>Vitrin ile başla, Büyüme ile devam et, istediğinde reklam ekle.</p></div>
{mini_plans()}
</div></section>
<section class="ksec" aria-labelledby="h-tek"><div class="wrap">
<div class="khead"><div><span class="eyebrow">Tek tek hizmetler</span><h2 id="h-tek">Hizmet seç, fiyatı gör.</h2></div></div>
{tables}
{terms_block()}
</div></section>
<section id="sss" class="light ksec" aria-labelledby="h-sss"><div class="wrap kfaq">
<div><span class="eyebrow">Sık sorulanlar</span><h2 id="h-sss">Fiyatlarla ilgili sorular.</h2></div>
{faq_list(HOME_FAQ[:4])}
</div></section>
{contact()}
'''
    return ("Web Sitesi ve Sosyal Medya Yönetimi Fiyatları 2026 | Laurus Dijital","Web sitesi, sosyal medya yönetimi ve reklam yönetimi fiyatları. Tek sayfa site 12.000 ₺, sosyal medya aylık 12.000 ₺'den.", body)


SECTORS = [
 dict(slug="kuafor-dijital-pazarlama.html", short="Kuaför ve berber", name="kuaför ve berber", photo="salon-fon", photo_alt="Kuaförde fön çeken kuaför",
      h1="Kuaförler ve berberler için web sitesi, Instagram ve Google reklamı.",
      lead="Randevularını telefondan ve DM'den toplamaktan kurtul. Seni “yakınımdaki kuaför” diye arayan kişi bulsun, fiyatını görsün, WhatsApp'tan randevu alsın.",
      pains=[("Randevular dağınık","Telefon, DM, WhatsApp; hangisi ne zaman geldi belli değil.","Tek bir WhatsApp randevu düğmesi ve hazır mesaj şablonu. Sitede, Instagram'da ve Google'da aynı yol."),
             ("Google'da görünmüyor","Haritada fotoğraf yok, saatler eski, yorumlar yanıtsız.","Google İşletme Profili'ni fotoğraf, saat, hizmet listesi ve yorum akışıyla tamamlarız."),
             ("Instagram düzensiz","Arada bir paylaşım, renkler ve dil tutarsız.","Aylık plan, önce/sonra Reels serisi ve tutarlı tasarım dili."),
             ("Boş saatler","Hafta içi öğleden sonra koltuklar boş kalıyor.","Boş saatlere özel Instagram ve Google reklamı, sadece 3–5 km çevrene.")],
      plan="Vitrin paketi + Büyüme paketi", case=None, kw="kuaför web sitesi, kuaför sosyal medya yönetimi, berber Instagram yönetimi"),
 dict(slug="guzellik-salonu-dijital-pazarlama.html", short="Güzellik salonu ve nail bar", name="güzellik salonu ve nail bar", photo="nail-is", photo_alt="Güzellik salonunda manikür yapılırken",
      h1="Güzellik salonları ve nail barlar için dijital pazarlama.",
      lead="Kampanyalarını doğru kişiye göster, işlerini Reels'le sergile, yorumlarını topla. Müşterin seni bulsun, güvensin, randevu alsın.",
      pains=[("İşler görünmüyor","Yaptığın tasarımlar telefonda kalıyor, profile düzenli yansımıyor.","Haftalık Reels ve galeri düzeni; her iş, bir sonraki müşterinin vitrini olur."),
             ("Kampanyalar duyulmuyor","Paket ve indirimler sadece mevcut takipçiye ulaşıyor.","Semtine özel Meta reklamı; mesaj ve randevu odaklı kampanyalar."),
             ("Dönemsel müşteri kaybı","Bakım zamanı gelen müşteri dönmeyi unutuyor.","Hatırlatma paylaşımları ve WhatsApp mesaj şablonları."),
             ("Yorum az","Memnun müşteri yorum bırakmıyor.","Yorum isteme bağlantısı ve ödeme sonrası gönderilecek hazır mesaj.")],
      plan="Büyüme paketi + Reklam", case=None, kw="güzellik salonu sosyal medya yönetimi, nail bar Instagram, güzellik salonu reklam"),
 dict(slug="pet-kuafor-dijital-pazarlama.html", short="Pet kuaför", name="pet kuaför", photo="pet-beyaz", photo_alt="Bakımı yapılmış beyaz köpek",
      h1="Pet kuaförler için Instagram, web sitesi ve yerel reklam.",
      lead="Bakım zamanı gelen müşteriyi geri getir, yeni hayvan sahiplerine semtinde ulaş. Önce/sonra paylaşımlarla güven kazan.",
      pains=[("Bakım zamanı unutuluyor","Müşteri 6–8 haftada bir gelmesi gerekirken aylarca kayboluyor.","Mevsime ve ırka göre bakım hatırlatan paylaşımlar ve WhatsApp şablonları."),
             ("Güven eksikliği","Yeni müşteri hayvanını kime emanet ettiğini görmek istiyor.","Önce/sonra Reels serisi, salon fotoğrafları ve gerçek yorumlar."),
             ("Sadece çevre biliyor","Semte yeni taşınanlar seni bulmuyor.","Google İşletme Profili ve 3 km çevreye Google/Meta reklamı."),
             ("Fiyat soruları","Aynı soru her gün DM'den geliyor.","Sitede ve profilde açık hizmet ve fiyat listesi.")],
      plan="Vitrin paketi + Büyüme paketi", case="nil", kw="pet kuaför web sitesi, pet kuaför Instagram, köpek kuaförü reklam"),
 dict(slug="kafe-restoran-dijital-pazarlama.html", short="Kafe ve restoran", name="kafe ve restoran", photo="kafe-latte", photo_alt="Kafede latte ve bitkiler",
      h1="Kafeler ve restoranlar için Google, Instagram ve yerel reklam.",
      lead="“Yakınımdaki kahveci” arayan kişi seni bulsun. Menün, saatlerin ve fotoğrafların güncel olsun; hafta sonu masaların dolsun.",
      pains=[("Haritada kayıp","Ara sokaktasın, yoldan geçen bilmiyor.","Google İşletme Profili, menü ve fotoğraflar; 3 km çevreye arama reklamı."),
             ("Menü güncel değil","Fiyatlar ve ürünler değişiyor, internette eski kalıyor.","Siteye ve profile bağlı, kolay güncellenen menü sayfası."),
             ("Hafta içi sakin","Yoğunluk sadece hafta sonu.","Hafta içi saatlerine özel kampanya paylaşımları ve reklamlar."),
             ("Fotoğraflar zayıf","Ürünler telefonda iştah açmıyor.","Basit çekim rehberi ve düzenlenmiş ürün görselleri.")],
      plan="Vitrin paketi + Reklam", case="feronya", kw="kafe sosyal medya yönetimi, restoran Google reklam, kafe web sitesi"),
 dict(slug="klinik-dijital-pazarlama.html", short="Sağlık ve klinik", name="klinik", photo="dis-klinik", photo_alt="Aydınlık bir diş kliniği muayene odası",
      h1="Klinikler ve muayenehaneler için web sitesi, SEO ve Google profili.",
      lead="Hastaların çoğu önce Google'a sorar. Tedavilerini anlatan, güven veren bir site ve doğru aramalarda görünen bir profil kuruyoruz.",
      pains=[("Aramalarda yoksun","“Ataşehir diş kliniği” gibi aramalarda rakipler önde.","Tedavi sayfaları, yerel SEO ve eksiksiz Google İşletme Profili."),
             ("Site güven vermiyor","Eski tasarım, telefonda bozuk, hekim bilgisi yok.","Hekim tanıtımı, klinik fotoğrafları ve sade, hızlı bir site."),
             ("Aynı sorular","Fiyat ve süreç soruları telefonu meşgul ediyor.","Sık sorulanlar ve tedavi süreçlerini anlatan içerikler."),
             ("Randevu zor","Hasta aramaya çekiniyor, mesajla yazmak istiyor.","WhatsApp ve form ile randevu talebi, her sayfada.")],
      plan="Kurumsal site + Google profili", case=None, kw="klinik web sitesi, diş kliniği SEO, muayenehane Google reklamı"),
 dict(slug="avukat-dijital-pazarlama.html", short="Avukat ve danışmanlık", name="hukuk bürosu ve danışmanlık", photo="hukuk-kutuphane", photo_alt="Hukuk kitaplarıyla dolu bir kütüphane rafı",
      h1="Avukatlar ve danışmanlık firmaları için web sitesi ve SEO.",
      lead="İnsanlar hukuki sorularını önce Google'a yazıyor. Çalışma alanlarını anlatan bir site ve bu sorulara yanıt veren içeriklerle seni bulmalarını sağlıyoruz.",
      pains=[("Görünmüyorsun","Hukuki sorular aranıyor ama büroya ulaşan yok.","Çalışma alanı sayfaları ve soru-cevap içerikleriyle SEO."),
             ("Eski site","Telefonda bozuk açılıyor, güncel değil.","Ciddi ve sade tasarım, hızlı ve güvenli altyapı."),
             ("Tanınırlık","Uzmanlığın sadece tavsiyeyle duyuluyor.","LinkedIn ve Instagram için bilgilendirme kartları."),
             ("İlk temas","Görüşme talebi telefonla sınırlı.","Görüşme talep formu ve WhatsApp düğmesi.")],
      plan="Kurumsal site + SEO", case=None, kw="avukat web sitesi, hukuk bürosu SEO, danışmanlık firması web sitesi"),
 dict(slug="emlak-dijital-pazarlama.html", short="Emlak", name="emlak ofisi", photo="emlak-salon", photo_alt="Aydınlık, sade döşenmiş bir oturma odası",
      h1="Emlak ofisleri için web sitesi, Instagram ve Meta reklamı.",
      lead="İlanların yalnızca ilan sitelerinde kalmasın. Kendi markan, kendi portföy sayfan ve semtine özel reklamlarla talepleri doğrudan sana getiriyoruz.",
      pains=[("Marka yok","Portföy sadece ilan sitelerinde, ofisin adı akılda kalmıyor.","Kendi siten ve portföy sayfaların, her ilana video tur alanı."),
             ("Talep dağınık","Talepler platformlar arasında kayboluyor.","Tek bir talep formu ve WhatsApp hattı."),
             ("İlan görünmüyor","Yeni ilan sınırlı kişiye ulaşıyor.","Semte ve bütçeye göre hedeflenmiş Meta reklamları."),
             ("Değerleme","Satıcı müşteri bulmak zor.","“Evinizin değeri ne kadar?” kampanyası ve formu.")],
      plan="Kurumsal site + Reklam", case=None, kw="emlak web sitesi, emlak ofisi Instagram, emlak reklam yönetimi"),
 dict(slug="butik-e-ticaret-dijital-pazarlama.html", short="Butik ve e-ticaret", name="butik ve mağaza", photo="butik-aski", photo_alt="Askıda doğal tonlarda triko ve giysiler",
      h1="Butikler ve mağazalar için satış sitesi, Instagram ve reklam.",
      lead="Satışların DM'de kaybolmasın. Ürünlerini sergileyen, ödeme alan bir site ve onu besleyen Instagram ve reklamlar kuruyoruz.",
      pains=[("DM'de satış","Fiyat ve stok soruları her gün tekrar ediyor.","Ürün kataloğu, beden ve stok bilgisiyle satış sitesi."),
             ("Ödeme zor","Havale ile ilerleyen siparişler yarım kalıyor.","Online ödeme ve sipariş takibi."),
             ("Sezon geçişi","Yeni ürünler yeterince görünmüyor.","Sezon çekim planı ve Instagram içerik takvimi."),
             ("Yeni müşteri","Satışlar mevcut takipçiyle sınırlı.","Ürün odaklı Meta reklamları ve yeniden hedefleme.")],
      plan="Satış sitesi + Büyüme paketi", case=None, kw="butik e-ticaret sitesi, butik Instagram yönetimi, mağaza Meta reklamı"),
 dict(slug="otel-turizm-dijital-pazarlama.html", short="Otel ve turizm", name="otel ve turizm", photo="otel-havuz", photo_alt="Palmiyelerle çevrili bir otel havuzu",
      h1="Oteller ve turizm işletmeleri için Google reklamı ve SEO.",
      lead="Misafirin çoğu seni bir arama ile bulur. Doğru aramalarda üst sıralarda çıkan reklamlar ve sayfalarla rezervasyonu kendi sitene çekiyoruz.",
      pains=[("Komisyon yükü","Rezervasyonların çoğu komisyonlu sitelerden geliyor.","Kendi sitene yönlenen Google arama reklamları."),
             ("Aramada geride","Otelin sitesi “bölge + otel” aramalarında arka sıralarda.","Oda, havuz ve paket sayfaları için SEO."),
             ("Ölçülmüyor","Reklamın kaç rezervasyon getirdiği belli değil.","Arama, WhatsApp ve rezervasyon tıklamalarının takibi."),
             ("Sezon dışı","Kış aylarında doluluk düşüyor.","Termal, hafta sonu ve erken rezervasyon kampanyaları.")],
      plan="Reklam paketi + SEO", case="otel", kw="otel Google reklamı, otel SEO, turizm dijital pazarlama"),
]

SURE = {"kuafor-dijital-pazarlama.html":"Tek sayfa site 7 günde yayında.","guzellik-salonu-dijital-pazarlama.html":"Tek sayfa site 7 günde yayında.","pet-kuafor-dijital-pazarlama.html":"Tek sayfa site 7 günde yayında.","kafe-restoran-dijital-pazarlama.html":"Tek sayfa site 7 günde yayında.","klinik-dijital-pazarlama.html":"Tek sayfa site 7 günde, kurumsal site 2–3 haftada yayında.","avukat-dijital-pazarlama.html":"Tek sayfa site 7 günde, kurumsal site 2–3 haftada yayında.","emlak-dijital-pazarlama.html":"Tek sayfa site 7 günde, kurumsal site 2–3 haftada yayında.","butik-e-ticaret-dijital-pazarlama.html":"Satış sitesi 3–5 haftada yayında.","otel-turizm-dijital-pazarlama.html":"Reklamlar ilk hafta içinde yayında."}
SECDESC = {"avukat-dijital-pazarlama.html":"Avukatlar ve danışmanlık firmaları için web sitesi, SEO ve bilgilendirici içerik. Çalışma alanlarını anlatan sade bir site, mesleki kurallara uygun dil. Fiyatlar açık.",
 "klinik-dijital-pazarlama.html":"Klinikler ve muayenehaneler için web sitesi, SEO ve Google İşletme Profili. Tedavileri anlatan güven veren site, sağlık tanıtım kurallarına uygun dil. Fiyatlar açık.",
 "otel-turizm-dijital-pazarlama.html":"Oteller ve turizm işletmeleri için Google reklamı ve SEO. Rezervasyonu kendi sitene çeken arama reklamları ve sayfalar. Fiyatlar açık, reklamlar ilk hafta yayında."}

def sector_page(sec):
    rows = "".join(f'<div class="kpain"><h3>{t}</h3><p class="pr">{a}</p><p class="so"><b>Çözüm:</b> {b}</p></div>' for t,a,b in sec["pains"])
    others = " · ".join(f'<a class="link" href="{x["slug"]}">{x["short"]}</a>' for x in SECTORS if x is not sec)
    faq = [(f"{sec['short']} için hangi paketle başlamalıyım?", f"Çoğu {sec['name']} için önerimiz: {sec['plan']}. İlk görüşmede mevcut hesaplarına bakıp net öneri veririz."),
           ("Ne kadar sürede sonuç alırım?","Site yayına girdiği gün Google'a bildirilir; Google profilinin doğrulanması birkaç gün sürebilir. Reklamlarda ilk mesajlar genelde ilk haftada gelir; sosyal medyada düzenli etki 2–3 ayda belirginleşir."),
           ("Başka şehirdeyim, olur mu?","Evet, tüm süreç online ilerliyor; reklam ve Google profili senin semtine göre ayarlanır.")]
    body = f"""
<section class="phero" aria-labelledby="h-page"><div class="wrap">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / Sektörler / {sec['short']}</nav>
<h1 id="h-page">{sec['h1']}</h1><p class="lead">{sec['lead']}</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a>{f'<a class="btn btn-line" href="calismalar.html#{sec["case"]}">Gerçek çalışmayı gör</a>' if sec.get("case") else '<a class="btn btn-line" href="calismalar.html">Çalışmalarımız</a>'}</div></div>
<div class="ph">{img(sec['photo'], sec['photo_alt'], eager=True)}</div>
</div></section>
<section class="light ksec" aria-labelledby="h-pains"><div class="wrap">
<div class="khead"><div><span class="eyebrow">{sec['short']}</span><h2 id="h-pains">En sık 4 sorun, 4 çözüm.</h2></div><p>Bu sektörde en sık karşılaşılan sorunlar ve ne yaptığımız.</p></div>
<div class="kpains">{rows}</div>
<div class="band kband"><div><h3>Önerimiz: {sec['plan']}</h3><p>Fiyatlar açık. {SURE.get(sec["slug"],"")}</p></div><a class="btn" href="fiyatlar.html">Paketleri incele</a></div>
</div></section>
<section class="ksec" aria-labelledby="h-sss"><div class="wrap kfaq">
<div><span class="eyebrow">Sık sorulanlar</span><h2 id="h-sss">{sec['short']} için sorular.</h2><p class="muted">Diğer sektörler: {others}</p></div>
{faq_list(faq)}
</div></section>
{contact()}
"""
    return (f"{sec['short']} için Web Sitesi, Sosyal Medya ve Reklam | Laurus Dijital",
            SECDESC.get(sec["slug"], f"{sec['short']} işletmeleri için web sitesi, Instagram yönetimi, Google İşletme Profili ve yerel reklam. Fiyatlar açık. {SURE.get(sec['slug'],'')}"), body)

# ---------- SEO guides ----------
GUIDE_DATE = "2026-10-23"

def gtable(head, rows):
    th = "".join(f'<th scope="col">{h}</th>' for h in head)
    tr = "".join("<tr>" + "".join(f'<td data-l="{head[i]}">{c}</td>' for i,c in enumerate(r)) + "</tr>" for r in rows)
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
   ("butce","Ne kadar bütçe gerekir?", f"""{gtable(["İşletme tipi","Başlangıç için aylık reklam bütçesi","Not"],[["Mahalle işletmesi (kuaför, kafe)","3.000 – 8.000 ₺","3–5 km çevreyle sınırlı"],["Klinik, emlak, danışmanlık","8.000 – 25.000 ₺","Tıklama maliyeti daha yüksek; sağlıkta tanıtım kurallarına uyulmalı"],["Otel ve turizm","15.000 ₺ ve üzeri","Sezona göre artırılır"]])}
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
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / <a href="rehber.html">Rehber</a> / {g["kw"].capitalize().replace("Seo","SEO")}</nav>
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

def page_about():
    vals = [("Açık fiyat","Fiyatlarımız sitede yazar. Teklif için günlerce beklemezsin, ödeyeceğin tutarı baştan bilirsin."),
            ("Hesaplar senin adına","Alan adı, Instagram, Google İşletme Profili ve reklam hesapları her zaman senin adına açılır."),
            ("Önce taslak","Her işe ücretsiz bir taslakla başlarız. Beğenmezsen ödeme yapmazsın."),
            ("Ölçülebilir sonuç","Her ay kısa bir rapor: kaç kişi gördü, kaç kişi aradı, hangi içerik işe yaradı.")]
    vh = "".join(f'<div class="ab-v" data-rv style="--d:{i*80}ms"><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(vals))
    svc_links = "".join(f'<li><a href="{h}">{t}</a></li>' for h,_,t,_ in SERVICES)
    sec_links = "".join(f'<li><a href="{x["slug"]}">{x["short"]}</a></li>' for x in SECTORS)
    body = f'''
<section class="phero" aria-labelledby="h-page"><div class="wrap">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / Hakkımızda</nav>
<h1 id="h-page">İstanbul merkezli dijital ajans: Laurus Dijital.</h1>
<p class="lead">Web tasarım, sosyal medya yönetimi, Google Ads ve SEO işlerini tek ekipte yürütüyoruz. Amacımız basit: işletmen internette bulunsun, güven versin ve müşteri kazansın.</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="calismalar.html">Çalışmalarımız</a></div></div>
<div class="ph">{img("planlama","Laurus Dijital ekibinin içerik planı üzerinde çalıştığı masa", eager=True)}</div>
</div></section>

<section class="light ksec" aria-labelledby="h-biz"><div class="wrap ab-grid">
<div data-rv><span class="eyebrow">Biz kimiz</span><h2 id="h-biz">8 yılı aşkın deneyim, tek ekip.</h2></div>
<div class="ab-tx" data-rv>
<p>Laurus Dijital, yazılım, bankacılık teknolojileri ve dijital projelerde <b>8 yılı aşkın deneyime</b> sahip bir ekip tarafından kuruldu. Büyük kurumların dijital projelerinde öğrendiğimiz disiplini, küçük ve orta ölçekli işletmelerin anlayacağı sade bir dille ve açık fiyatlarla sunuyoruz.</p>
<p>Yazılım geçmişimiz sayesinde işimiz web sitesiyle sınırlı değil: <b>mobil uygulama</b> ve <b>web uygulaması</b> da geliştiriyoruz. oh same., Sorbi, Sekiz8, Çınar ve Nefes bu ekibin tasarlayıp kodladığı, kendi ürünlerimiz.</p>
<p>Ekibimizde tasarım, yazılım, içerik ve reklam yönetimi tarafları birlikte çalışır. Bir işletmenin <b>web sitesini</b>, <b>Instagram ve sosyal medya hesaplarını</b>, <b>Google Ads ve Meta reklamlarını</b> ve <b>Google İşletme Profili ile SEO çalışmasını</b> aynı masada planlarız. Böylece sitedeki mesaj, Instagram'daki görsel dil ve Google'daki reklam birbirini tamamlar.</p>
<p>İstanbul'dan Türkiye genelinde online hizmet veriyoruz. Kuaförden otele, klinikten hukuk bürosuna kadar müşterisini internetten bulan her işletmeyle çalışıyoruz.</p>
</div></div></section>

<section class="ksec" aria-labelledby="h-deg"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Nasıl çalışırız</span><h2 id="h-deg">Bizi tercih edenlerin dört nedeni.</h2></div></div>
<div class="ab-vals">{vh}</div>
</div></section>

{app_show(h2="Yetkinliğimizi kendi <br>uygulamalarımızla gösteriyoruz.", eyebrow="Kendi ürünlerimiz", sid="urunler")}

<section class="light ksec" aria-labelledby="h-ne"><div class="wrap ab-grid">
<div data-rv><span class="eyebrow">Hizmetlerimiz</span><h2 id="h-ne">Dijital ajans hizmetleri, tek yerden.</h2></div>
<div class="ab-tx" data-rv>
<p>Kurumsal web sitesi ve e-ticaret sitesi tasarımı, mobil uygulama ve web uygulaması geliştirme, sosyal medya yönetimi ve Instagram hesap yönetimi, Google Ads ve Instagram reklam yönetimi, yerel SEO ve Google İşletme Profili kurulumu. İhtiyacın olan tek bir hizmetle başlayabilir, işin büyüdükçe diğerlerini ekleyebilirsin.</p>
<div class="ab-links"><div><b>Hizmetler</b><ul>{svc_links}</ul></div><div><b>Sektörler</b><ul>{sec_links}</ul></div></div>
</div></div></section>
{contact()}
'''
    return ("Hakkımızda | Laurus Dijital, İstanbul Dijital Ajans",
            "Laurus Dijital, 8 yılı aşkın yazılım ve dijital deneyime sahip ekibiyle web tasarım, mobil uygulama, sosyal medya yönetimi, Google Ads ve SEO hizmeti veren İstanbul merkezli dijital ajans.", body)


PAGES = {
  "index.html": (page_index, ""),
  "web-tasarim.html": (page_web, "svc"),
  "sosyal-medya.html": (page_social, "svc"),
  "reklam-yonetimi.html": (page_ads, "svc"),
  "google-isletme.html": (page_gbp, "svc"),
  "mobil-uygulama.html": (page_apps, "svc"),
  "calismalar.html": (page_cases, "calismalar"),
  "fiyatlar.html": (page_prices, "fiyatlar"),
  "rehber.html": (page_rehber, "rehber"),
  "hakkimizda.html": (page_about, "hakkimizda"),
}
for _g in GUIDES:
    PAGES[_g["slug"]] = ((lambda g=_g: guide_page(g)), "rehber")
for _sec in SECTORS:
    PAGES[_sec["slug"]] = ((lambda sec=_sec: sector_page(sec)), "")

PAGE_META.update({
  "web-tasarim.html": dict(crumb=[("Web tasarım","/web-tasarim")], service=("Web tasarım","12000","Telefonda hızlı açılan, WhatsApp'tan randevu getiren web siteleri.")),
  "sosyal-medya.html": dict(crumb=[("Sosyal medya ve içerik","/sosyal-medya")], service=("Sosyal medya yönetimi","12000","Instagram ve TikTok yönetimi, aylık içerik planı ve Reels.")),
  "reklam-yonetimi.html": dict(crumb=[("Google ve Meta reklamları","/reklam-yonetimi")], service=("Google Ads ve Meta reklam yönetimi","9000","Google arama, harita ve Instagram reklamları.")),
  "google-isletme.html": dict(crumb=[("Google İşletme ve yerel SEO","/google-isletme")], service=("Google İşletme Profili ve yerel SEO",None,"Google Haritalar profil kurulumu, fotoğraflar ve yorum akışı.")),
  "mobil-uygulama.html": dict(crumb=[("Mobil uygulama","/mobil-uygulama")], service=("Mobil uygulama ve web uygulaması geliştirme",None,"iOS, Android ve web uygulaması geliştirme; üyelik, abonelik ve mağaza yayını.")),
  "calismalar.html": dict(crumb=[("Çalışmalar","/calismalar")]),
  "fiyatlar.html": dict(crumb=[("Fiyatlar","/fiyatlar")]),
})
PAGE_META["rehber.html"] = dict(crumb=[("Rehber","/rehber")])
PAGE_META["hakkimizda.html"] = dict(crumb=[("Hakkımızda","/hakkimizda")])
for _g in GUIDES:
    PAGE_META[_g["slug"]] = dict(crumb=[("Rehber","/rehber"),(_g["kw"].capitalize().replace("Seo","SEO"),"/"+_g["slug"].replace(".html",""))])
for _sec in SECTORS:
    PAGE_META[_sec["slug"]] = dict(crumb=[(_sec["short"], "/"+_sec["slug"].replace(".html",""))])

def build():
    keep = {"fonts","og.png","favicon.svg","_headers","robots.txt"}
    os.makedirs(OUT, exist_ok=True)
    for f in os.listdir(OUT):
        if f in keep: continue
        p = os.path.join(OUT,f)
        shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    shutil.copytree(os.path.join(SRC,"assets"), os.path.join(OUT,"assets"))
    shutil.copytree(os.path.join(SRC,"img"), os.path.join(OUT,"img"))
    for slug,(fn,active) in PAGES.items():
        title, desc, body = fn()
        open(os.path.join(OUT,slug),"w").write(layout(slug,title,desc,body,active))
    urls = "".join(f"<url><loc>{BASE}{'/' if s=='index.html' else '/'+s.replace('.html','')}</loc><lastmod>{GUIDE_DATE}</lastmod><changefreq>{'weekly' if s=='index.html' else 'monthly'}</changefreq><priority>{'1.0' if s=='index.html' else ('0.9' if s in GMAP or s in ('web-tasarim.html','sosyal-medya.html','mobil-uygulama.html') else '0.7')}</priority></url>" for s in PAGES)
    open(os.path.join(OUT,"sitemap.xml"),"w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    PREV = os.path.join(os.path.dirname(SRC),"site-preview")
    # 404 page
    open(os.path.join(OUT,"404.html"),"w").write(layout("404.html","Sayfa bulunamadı | Laurus Dijital","Aradığın sayfa bulunamadı.",
        '<section class="phero"><div class="wrap" style="grid-template-columns:1fr"><div><h1>Bu sayfa yok.</h1><p class="lead">Adres değişmiş ya da yanlış yazılmış olabilir.</p><div class="actions"><a class="btn btn-gold" href="index.html">Ana sayfaya dön</a><a class="btn btn-line js-wa" href="https://wa.me/905434309702">WhatsApp\'tan yaz</a></div></div></div></section>'))
    if os.path.exists(PREV): shutil.rmtree(PREV)
    shutil.copytree(OUT, PREV)
    # production copy with clean URLs for Cloudflare Pages
    import glob
    for f in glob.glob(os.path.join(OUT,"*.html")):
        t = open(f).read()
        t = t.replace('href="index.html#','href="/#').replace('href="index.html"','href="/"')
        t = re.sub(r'href="([a-z0-9-]+)\.html(#[^"]*)?"', lambda m: f'href="/{m.group(1)}{m.group(2) or ""}"', t)
        t = t.replace('href="assets/','href="/assets/').replace('src="assets/','src="/assets/').replace('src="img/','src="/img/').replace('href="favicon.svg"','href="/favicon.svg"').replace('href="fonts/','href="/fonts/')
        open(f,"w").write(t)
    p404 = os.path.join(OUT,"404.html"); t = open(p404).read()
    t = re.sub(r'(<a\b[^>]*?)href="#', r'\1href="/#', t)
    t = re.sub(r'<link rel="canonical"[^>]*>\n?','',t).replace('content="index, follow, max-image-preview:large"','content="noindex, follow"')
    open(p404,"w").write(t)
    css = os.path.join(OUT,"assets","site.css")
    c = open(css).read().replace("url(../fonts/","url(/fonts/")
    open(css,"w").write(c)
    import hashlib
    LV = os.path.join(SRC,"live")
    live = open(os.path.join(LV,"d3g.min.js")).read() + "\nwindow.LAUR_LAND=" + open(os.path.join(LV,"land.json")).read() + ";\n" + open(os.path.join(LV,"live-src.js")).read()
    open(os.path.join(OUT,"assets","live.js"),"w").write(live)
    lver = hashlib.md5(live.encode()).hexdigest()[:10]
    sj = os.path.join(OUT,"assets","site.js"); sjt = open(sj).read().replace("__LIVEV__", lver); open(sj,"w").write(sjt)
    ver = hashlib.md5((c + open(os.path.join(OUT,"assets","site.js")).read()).encode()).hexdigest()[:10]
    for f in glob.glob(os.path.join(OUT,"*.html")):
        t = open(f).read().replace('href="/assets/site.css"', f'href="/assets/site.css?v={ver}"').replace('src="/assets/site.js"', f'src="/assets/site.js?v={ver}"')
        open(f,"w").write(t)
    open(os.path.join(OUT,"_headers"),"w").write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n/img/*\n  Cache-Control: public, max-age=2592000\n/assets/*\n  Cache-Control: public, max-age=31536000, immutable\n")
    print("built", len(PAGES), "pages ->", OUT)

if __name__ == "__main__":
    build()
