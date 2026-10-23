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
<div class="topbar"><div class="wrap"><span><a href="mailto:{EMAIL}">{EMAIL}</a><a href="tel:{PHONE_TEL}">{PHONE_TXT}</a></span><span>Hafta içi 09:00–19:00 · Türkiye geneli online hizmet</span></div></div>
<header class="nav"><div class="wrap">
<a class="brand" href="index.html" aria-label="Laurus Dijital ana sayfa"><svg viewBox="0 0 40 40" aria-hidden="true"><use href="#logo"/></svg><span><b>Laurus</b><small>DİJİTAL AJANS</small></span></a>
<nav class="menu" id="menu" aria-label="Ana menü">
<div class="dd"><button type="button" aria-expanded="false" aria-controls="dd-svc">Hizmetler {I['down']}</button><div class="dd-panel" id="dd-svc" hidden>{dd}</div></div>
<a href="calismalar.html"{cur("calismalar")}>Çalışmalar</a>
<a href="index.html#nasil">Nasıl çalışıyoruz</a>
<a href="fiyatlar.html"{cur("fiyatlar")}>Fiyatlar</a>
<a href="index.html#sss">SSS</a>
<a class="btn btn-gold" href="#iletisim">Teklif al</a>
</nav>
<button class="burger" id="burger" aria-label="Menüyü aç" aria-expanded="false" aria-controls="menu"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div></header>'''

def contact(title="İşletmeni anlat, taslağını gör.", need="Web sitesi"):
    needs = ["Web sitesi","Sosyal medya yönetimi","Google / Meta reklamı","Google İşletme profili","Hepsi","Emin değilim, öneri istiyorum"]
    opts = "".join(f'<option{" selected" if n==need else ""}>{n}</option>' for n in needs)
    return f'''<section id="iletisim" class="contact" aria-labelledby="h-contact"><div class="wrap cbox">
<div><span class="eyebrow">İletişim</span><h2 id="h-contact">{title}</h2>
<p class="lead">Formu doldur ya da doğrudan yaz. İşletmeni inceleyip sana ne yapabileceğimizi aynı gün gösterelim. İlk görüşme ücretsiz.</p>
<div class="direct">
<a class="js-wa" href="https://wa.me/905434309702"><span class="ic">{I['wa']}</span><span><small>WhatsApp</small><b>{PHONE_TXT}</b></span></a>
<a href="mailto:{EMAIL}"><span class="ic">{I['mail']}</span><span><small>E-posta</small><b>{EMAIL}</b></span></a>
</div></div>
<form class="quick" id="quick" novalidate>
<h3>Ücretsiz ön görüşme</h3><p>Bilgilerin WhatsApp mesajı olarak hazırlanır, gönder tuşuna sen basarsın.</p>
<div class="two"><label for="f-name">Adın<input id="f-name" name="fname" autocomplete="name" required></label><label for="f-biz">İşletmenin adı<input id="f-biz" name="biz" required></label></div>
<div class="two"><label for="f-sector">Sektör<select id="f-sector" name="sector"><option>Kuaför / berber</option><option>Güzellik salonu</option><option>Nail bar / kirpik</option><option>Pet kuaför</option><option>Kafe / restoran</option><option>Butik / mağaza</option><option>Diğer</option></select></label>
<label for="f-need">İhtiyacın<select id="f-need" name="need">{opts}</select></label></div>
<label for="f-ig">Instagram ya da web siten (varsa)<input id="f-ig" name="ig" placeholder="@isletmen"></label>
<label for="f-note">Eklemek istediğin<textarea id="f-note" name="note" placeholder="Örneğin: Kadıköy'de 2 yıllık salonuz, daha çok randevu istiyoruz."></textarea></label>
<div class="err" id="f-err" aria-live="polite"></div>
<button class="btn btn-wa" type="submit">{I['wa']}WhatsApp'tan gönder</button>
<p class="fine">Form bilgilerini sitede saklamıyoruz; mesaj doğrudan senin WhatsApp'ından gider.</p>
</form></div></section>'''

def footer():
    svc = "".join(f'<li><a href="{h}">{t}</a></li>' for h,_,t,_ in SERVICES)
    return f'''<footer><div class="wrap"><div class="fgrid">
<div><a class="brand" href="index.html" aria-label="Laurus Dijital"><svg viewBox="0 0 40 40" aria-hidden="true"><use href="#logo"/></svg><span><b>Laurus</b><small>DİJİTAL AJANS</small></span></a>
<p class="about">İşletmeler için web sitesi, sosyal medya ve reklam. İstanbul'dan Türkiye geneline online hizmet.</p></div>
<div><h4>Hizmetler</h4><ul>{svc}</ul></div>
<div><h4>Sektörler</h4><ul><li><a href="kuafor-dijital-pazarlama.html">Kuaför ve berber</a></li><li><a href="guzellik-salonu-dijital-pazarlama.html">Güzellik salonu</a></li><li><a href="pet-kuafor-dijital-pazarlama.html">Pet kuaför</a></li><li><a href="kafe-restoran-dijital-pazarlama.html">Kafe ve restoran</a></li></ul></div>
<div><h4>Laurus</h4><ul><li><a href="calismalar.html">Çalışmalar</a></li><li><a href="index.html#nasil">Nasıl çalışıyoruz</a></li><li><a href="fiyatlar.html">Fiyatlar</a></li><li><a href="index.html#sss">Sık sorulanlar</a></li></ul></div>
<div><h4>İletişim</h4><ul><li><a class="js-wa" href="https://wa.me/905434309702">WhatsApp: {PHONE_TXT}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>İstanbul, Türkiye</li></ul></div>
</div><div class="fbot"><span>© 2026 Laurus Dijital</span><span>Bu site çerez kullanmaz. Fotoğraflar: Unsplash.</span></div></div></footer>
<a class="wa-float js-wa" href="https://wa.me/905434309702" aria-label="WhatsApp'tan yaz">{I['wa']}</a>'''

import json, re
def _strip(t): return re.sub(r"<[^>]+>","",t)
PAGE_META = {}  # slug -> dict(crumb=..., service=(name, price, desc))
def schemas(slug, url, title, desc):
    org = {"@type":["ProfessionalService","LocalBusiness"],"@id":BASE+"/#org","name":"Laurus Dijital","url":BASE,"logo":BASE+"/favicon.svg","image":BASE+"/og.png",
           "email":EMAIL,"telephone":PHONE_TEL,"priceRange":"₺₺","address":{"@type":"PostalAddress","addressLocality":"İstanbul","addressRegion":"İstanbul","addressCountry":"TR"},
           "areaServed":[{"@type":"City","name":"İstanbul"},{"@type":"Country","name":"Türkiye"}],
           "openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"09:00","closes":"19:00"}],
           "knowsAbout":["web tasarım","sosyal medya yönetimi","Google Ads","Meta reklamları","yerel SEO","Google İşletme Profili"],
           "hasOfferCatalog":{"@type":"OfferCatalog","name":"Hizmetler","itemListElement":[{"@type":"Offer","itemOffered":{"@type":"Service","name":t,"url":BASE+"/"+h.replace(".html","")}} for h,_,t,_ in SERVICES]}}
    graph=[org,{"@type":"WebSite","@id":BASE+"/#site","url":BASE,"name":"Laurus Dijital","inLanguage":"tr-TR","publisher":{"@id":BASE+"/#org"}},
           {"@type":"WebPage","@id":url+"#page","url":url,"name":title,"description":desc,"inLanguage":"tr-TR","isPartOf":{"@id":BASE+"/#site"}}]
    m = PAGE_META.get(slug,{})
    if m.get("crumb"):
        graph.append({"@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Ana sayfa","item":BASE+"/"}]+[{"@type":"ListItem","position":i+2,"name":n,"item":BASE+u} for i,(n,u) in enumerate(m["crumb"])]})
    if m.get("service"):
        n,price,d = m["service"]
        graph.append({"@type":"Service","name":n,"description":d,"provider":{"@id":BASE+"/#org"},"areaServed":"TR","url":url,
                      "offers":{"@type":"Offer","price":price,"priceCurrency":"TRY","url":url+"#fiyat"}})
    if FAQ_SINK:
        graph.append({"@type":"FAQPage","mainEntity":[{"@type":"Question","name":_strip(q),"acceptedAnswer":{"@type":"Answer","text":_strip(a)}} for q,a in FAQ_SINK]})
    return json.dumps({"@context":"https://schema.org","@graph":graph},ensure_ascii=False)

def layout(slug, title, desc, body, active=""):
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
<body>
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

def igphone(handle, sub, av, grid, posts="148", fol="3.204", fl="412"):
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
 ("Sonuç ne zaman görülür?","Site ve Google profili yayına girdiği gün görünür olursun. Reklamlarda ilk mesajlar genelde ilk haftada gelir; sosyal medyada düzenli büyüme 2–3 ayda belirginleşir. Garanti vermeyiz, her ay rakamları birlikte görürüz."),
 ("İstanbul dışındayım, çalışabilir miyiz?","Evet. Bütün süreç WhatsApp ve görüntülü görüşmeyle ilerliyor; Türkiye'nin her yerinden çalışıyoruz."),
]

# ---------- pages ----------
def page_index():
    svc_cards = [
      ("web-tasarim.html","tasarim-laptop","Web tasarım","İşletmenin internetteki evi","Müşterin seni aradığında karşısına çıkan, telefonda hızlı açılan ve tek dokunuşla WhatsApp'a götüren site.",["Tek sayfa","Kurumsal","Satış sitesi"]),
      ("sosyal-medya.html","telefon-instagram","Sosyal medya ve içerik","Hesabın hiç boş kalmasın","Aylık plan, tasarım, Reels ve mesajlara yanıt. Sen işine bak, Instagram'ın düzenli ve canlı kalsın.",["Instagram","TikTok","Reels"]),
      ("reklam-yonetimi.html","google-arama","Google ve Meta reklamları","Arayan kişinin karşısına çık","“Yakınımdaki kuaför” diye arayana ya da semtindeki kişiye Instagram'da görünen reklamlar.",["Google Ads","Instagram reklamı","Raporlama"]),
      ("google-isletme.html","harita","Google İşletme ve yerel SEO","Haritalarda ilk bakışta güven ver","Fotoğrafları, saatleri, hizmetleri tam bir profil ve düzenli gelen yorumlar.",["Google Haritalar","Yorum","Yerel arama"]),
    ]
    cards = "".join(f'''<a class="svc-card" href="{h}">{img(p,"")}<div class="in"><span class="tagline">{tg}</span><h3>{t}</h3><p>{d}</p><ul>{"".join(f"<li>{x}</li>" for x in tags)}</ul><span class="go">Detaylı incele {I['arrow']}</span></div></a>''' for h,p,t,tg,d,tags in svc_cards)
    sectors = [("salon-fon","Kuaför ve berber","Randevu, hizmet listesi, önce/sonra"),("nail","Nail bar ve güzellik","Kampanya, Reels, yorum"),("pet-beyaz","Pet kuaför","Mevsimsel bakım içerikleri"),("kafe-latte","Kafe ve restoran","Haritalar, menü, yerel reklam"),("butik","Butik ve mağaza","Ürün görselleri ve satış sitesi"),("cicekci","Çiçekçi ve atölye","Sipariş ve özel gün kampanyaları")]
    links = {"Kuaför ve berber":"kuafor-dijital-pazarlama.html","Nail bar ve güzellik":"guzellik-salonu-dijital-pazarlama.html","Pet kuaför":"pet-kuafor-dijital-pazarlama.html","Kafe ve restoran":"kafe-restoran-dijital-pazarlama.html"}
    sec = "".join((f'<a class="sector" href="{links[t]}">' if t in links else '<div class="sector">') + f'{img(p,"")}<div><b>{t}</b><span>{d}</span></div>' + ('</a>' if t in links else '</div>') for p,t,d in sectors)
    cases = [
      ("calismalar.html#moda-salon","salon-yikama","Kuaför · Web sitesi + Google","Moda Salon","Randevuları telefondan WhatsApp'a taşıyan tek sayfa site ve tamamlanmış Google profili."),
      ("calismalar.html#patiler","pet-kosan","Pet kuaför · Instagram","Patiler Pet Kuaför","Renkleri tutarlı, mevsime göre bakım hatırlatan bir Instagram düzeni."),
      ("calismalar.html#kose-kahve","kafe-masa","Kafe · Google reklamı","Köşe Kahve","3 km çevrede “kahve” arayana çıkan reklam ve menüsü güncel harita profili."),
    ]
    cc = "".join(f'<a class="case-card" href="{h}"><div class="ph">{img(p,"")}<span class="badge">Örnek çalışma</span></div><div class="bd"><small>{s}</small><h3>{t}</h3><p>{d}</p><span class="go">Nasıl yaptığımızı gör →</span></div></a>' for h,p,s,t,d in cases)

    body = f'''
<section class="hero" aria-labelledby="h-hero"><div class="wrap">
<div>
<span class="kicker"><i></i>Yeni müşteri kabul ediyoruz</span>
<h1 id="h-hero">Müşterin seni arıyor. <em>Bulsun.</em></h1>
<p class="lead">Web sitesi, Instagram, Google profili ve reklamlarını tek ekipte yürütüyoruz. İşletmeni internette bulunur, güvenilir ve randevu alır hâle getiriyoruz.</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="calismalar.html">Çalışmaları gör</a></div>
<div class="facts"><div><b>7 gün</b><span>ilk site yayında</span></div><div><b>%100</b><span>hesaplar senin adına</span></div><div><b>3 ay</b><span>sonra istediğin an bırak</span></div></div>
</div>
<div class="hero-visual">
<div class="hero-photo">{img("hero-salon","Bir kuaför salonunun resepsiyonunda müşteri ve çalışan tablet üzerinden randevu ayarlıyor",eager=True)}</div>
<div class="chip c1" aria-hidden="true"><span class="ic" style="background:#E8F0FE;color:#1A73E8">{I['search']}</span><span><b>“kuaför kadıköy”</b><small>Google'da ve haritada görünür</small></span></div>
<div class="chip c2" aria-hidden="true"><span class="ic" style="background:#E7F6EC;color:#1FA855">{I['wa']}</span><span><b>Yeni randevu talebi</b><small>“Cumartesi 14:00 boş mu?”</small></span></div>
<div class="chip c3" aria-hidden="true"><span class="ic" style="background:#FDF1F5;color:#E1306C">{I['ig']}</span><span><b>Bu hafta 3 yeni Reels</b><small>Planlandı ve paylaşıldı</small></span></div>
</div></div></section>

<div class="platforms"><div class="wrap"><p>Çalıştığımız platformlar</p><ul><li>Google Ads</li><li>Meta</li><li>Instagram</li><li>TikTok</li><li>Google İşletme</li><li>WhatsApp Business</li></ul></div></div>

<section class="light" aria-labelledby="h-story"><div class="wrap">
<div class="head center"><span class="eyebrow">Ne yapıyoruz, basitçe</span><h2 id="h-story">Bir müşteri seni bulmadan önce üç şey olur. Üçünü de biz hallederiz.</h2>
<p>Teknik terimlere gerek yok. Müşterinin telefonunda olanı düşün: arar, bakar, yazar.</p></div>
<div class="story">
<article><div class="ph">{img("harita","Telefonda Google Haritalar'da yakındaki işletmeler")}<span class="num">1</span></div><h3>Seni bulur</h3><p>Biri “yakınımdaki kuaför” ya da “Kadıköy kahve” diye arar. Google'da ve haritada senin işletmen çıkar.</p><div class="means"><b>Bunun için:</b> Google İşletme Profili, yerel SEO, Google reklamı</div></article>
<article><div class="ph">{img("telefon-instagram","Telefonda bir işletmenin Instagram profiline bakan kişi")}<span class="num">2</span></div><h3>Sana güvenir</h3><p>Instagram'ına, sitene, fotoğraflarına bakar. Düzenli, güncel ve profesyonel görünürsün; fiyat ve hizmetlerin net.</p><div class="means"><b>Bunun için:</b> web sitesi, Instagram düzeni, Reels, yorumlar</div></article>
<article><div class="ph">{img("kadin-telefon","Telefonundan mesaj yazan gülümseyen bir kadın")}<span class="num">3</span></div><h3>Sana yazar</h3><p>Tek dokunuşla WhatsApp'tan randevu ister ya da arar. Aradaki her engeli kaldırırız.</p><div class="means"><b>Bunun için:</b> WhatsApp düğmesi, randevu akışı, Meta reklamı</div></article>
</div></div></section>

<section id="hizmetler" aria-labelledby="h-svc"><div class="wrap">
<div class="head"><div><span class="eyebrow">Hizmetler</span><h2 id="h-svc">İşletmenin dijital tarafını baştan sona biz yürütürüz.</h2></div><p>İstersen tek bir hizmetle başla, istersen hepsini birlikte al. Her hizmetin ne kazandırdığını kendi sayfasında anlattık.</p></div>
<div class="svc-grid">{cards}</div>
</div></section>

<section class="light" aria-labelledby="h-ba"><div class="wrap ba" data-ba>
<div><span class="eyebrow">Önce ve sonra</span><h2 class="h2" id="h-ba">Aynı işletme, iki farklı Google profili.</h2>
<p class="muted" style="margin-top:16px;font-size:18px">Müşteri seni ilk kez gördüğünde karar verir. Düğmeye bas ve farkı gör.</p>
<div class="toggle" role="group" aria-label="Profil görünümü"><button type="button" data-ba-set="once" aria-pressed="false">Önce</button><button type="button" data-ba-set="sonra" aria-pressed="true">Sonra</button></div>
<ul class="ba-list" data-ba-view="once" hidden><li><span class="x">✕</span>Fotoğraf yok, ne iş yaptığın anlaşılmıyor</li><li><span class="x">✕</span>Saatler yanlış, kapalı sanılıyor</li><li><span class="x">✕</span>Web sitesi ve randevu yolu yok</li><li><span class="x">✕</span>Yorum az ve yanıtsız</li></ul>
<ul class="ba-list" data-ba-view="sonra"><li><span class="ok">✓</span>Gerçek salon fotoğrafları, ilk bakışta güven</li><li><span class="ok">✓</span>Doğru saatler ve “Şu an açık” bilgisi</li><li><span class="ok">✓</span>Site, arama ve WhatsApp'tan randevu tek dokunuşta</li><li><span class="ok">✓</span>Düzenli toplanan ve yanıtlanan yorumlar</li></ul>
</div>
<div>
<div class="gmock" data-ba-view="once" hidden aria-label="Bakımsız Google profili örneği">
<div class="sbar">{I['search']}<span>kuaför moda kadıköy</span></div>
<div class="photos"><div class="empty">Fotoğraf eklenmemiş</div></div>
<div class="bd"><h4>Moda Kuaför</h4><div class="meta">Kuaför · <span class="closed">Saatler güncellenmedi</span></div>
<div class="acts"><span>Yol tarifi</span><span class="dim">Web sitesi yok</span><span class="dim">Randevu yok</span></div>
<div class="rows"><div class="na">Hizmet listesi yok</div><div class="na">2 yorum · son yorum 2 yıl önce</div></div></div></div>
<div class="gmock" data-ba-view="sonra" aria-label="Düzenlenmiş Google profili örneği">
<div class="sbar">{I['search']}<span>kuaför moda kadıköy</span></div>
<div class="photos">{img("salon-yikama","")}{img("salon-fon","")}{img("salon-ic","")}</div>
<div class="bd"><h4>Moda Salon</h4><div class="meta">Kuaför · Moda, Kadıköy · <span class="open">Şu an açık</span> · 20:00'de kapanır</div>
<div class="acts"><span>Web sitesi</span><span>Yol tarifi</span><span>Ara</span><span>WhatsApp'tan randevu</span></div>
<div class="rows"><div>Kesim + fön · Dip boya · Keratin bakım · Gelin saçı</div><div>Yorumlar düzenli yanıtlanıyor</div></div></div></div>
</div></div></section>

<section aria-labelledby="h-cases"><div class="wrap">
<div class="head"><div><span class="eyebrow">Çalışmalar</span><h2 id="h-cases">Sektörüne göre neler yaptığımızı gör.</h2></div><p>Her işletme için önce bir taslak hazırlarız. Aşağıdakiler sektörlere göre hazırladığımız örnek çalışmalar; nasıl kurgulandıklarını adım adım anlattık.</p></div>
<div class="cases">{cc}</div>
<p class="muted" style="margin-top:22px;font-size:14px">İşletme adları örnektir. Gerçek müşteri çalışmalarımız, müşteri onayıyla burada yayınlanacak.</p>
</div></section>

<section id="nasil" class="light" aria-labelledby="h-proc"><div class="wrap proc">
<div class="ph">{img("planlama","Masada defter ve dizüstü bilgisayarla içerik planı yapan kişi")}</div>
<div><span class="eyebrow">Nasıl çalışıyoruz</span><h2 class="h2" id="h-proc">İlk görüşmeden yayına 7 gün.</h2>
<p class="muted" style="margin:16px 0 28px;font-size:18px">Önce görürsün, sonra karar verirsin. Ödemenin yarısı taslağı beğendiğinde, kalanı yayından önce.</p>
<ol class="steps">
<li><div><span class="d">1. gün</span><h3>Tanışma</h3><p>15 dakikalık görüşme. İşletmeni, müşterini ve hedefini dinleriz, mevcut hesaplarına bakarız.</p></div></li>
<li><div><span class="d">2–3. gün</span><h3>İlk taslak</h3><p>Ana sayfanı ve ilk içerik örneklerini görürsün. Beğenmezsen ödeme yapmazsın.</p></div></li>
<li><div><span class="d">4–6. gün</span><h3>Tamamlama</h3><p>Metinler, fotoğraflar, Google profili ve ilk paylaşımlar hazırlanır. İki düzeltme turu senin.</p></div></li>
<li><div><span class="d">7. gün</span><h3>Yayında</h3><p>Siten açılır, profillerin düzenlenir. Aylık pakette ayda bir kısa rapor gelir.</p></div></li>
</ol></div></div></section>

<section aria-labelledby="h-sec"><div class="wrap">
<div class="head"><div><span class="eyebrow">Sektörler</span><h2 id="h-sec">Randevuyla ve müşteriyle yüz yüze çalışan işletmeler için.</h2></div><p>Müşterisini telefondan bulan, Instagram'dan mesaj alan her işletmeyle çalışıyoruz.</p></div>
<div class="sectors">{sec}</div>
</div></section>

<section id="fiyatlar" class="light" aria-labelledby="h-price"><div class="wrap">
<div class="head"><div><span class="eyebrow">Fiyatlar</span><h2 id="h-price">Açık fiyat, sürpriz yok.</h2></div><p>Önerdiğimiz üç paket aşağıda. Tüm hizmetlerin tek tek fiyatları <a class="link" href="fiyatlar.html">fiyatlar sayfasında</a>.</p></div>
{plans_block()}{terms_block()}
</div></section>

{faq_block(HOME_FAQ)}
{contact()}
'''
    return ("Laurus Dijital | Web Tasarım, Sosyal Medya ve Reklam Ajansı · İstanbul",
            "İşletmeler için web sitesi, Instagram yönetimi, Reels, Google ve Meta reklamları. Fiyatlar açık, ilk site 7 günde yayında, tüm hesaplar senin adına.", body)

def service_page(slug, crumb, h1, lead, photo, photo_alt, plain_q, plain_a, does, visual, deliver_title, deliverables, month, price_rows, faq, need):
    dg = "".join(f'<div class="do"><span class="ic">{I[ic]}</span><h3>{t}</h3><p>{d}</p></div>' for ic,t,d in does)
    mo = ""
    if month:
        mo = '<section class="light" aria-labelledby="h-month" style="padding-top:0"><div class="wrap"><div class="head"><div><span class="eyebrow">Bir ay nasıl geçer</span><h2 id="h-month">Seninle çalışırken her ay aynı ritim.</h2></div><p>Ne zaman ne olacağını baştan bilirsin, sürpriz yok.</p></div><div class="month">' + "".join(f"<div><b>{w}</b><h4>{t}</h4><p>{d}</p></div>" for w,t,d in month) + '</div></div></section>'
    rows = "".join(f"<tr><td>{a}<small>{b}</small></td><td>{c}</td></tr>" for a,b,c in price_rows)
    body = f'''
<section class="phero" aria-labelledby="h-page"><div class="wrap">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / <a href="index.html#hizmetler">Hizmetler</a> / {crumb}</nav>
<h1 id="h-page">{h1}</h1><p class="lead">{lead}</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="#fiyat">Fiyatı gör</a></div></div>
<div class="ph">{img(photo, photo_alt, eager=True)}</div>
</div></section>

<section class="light" aria-labelledby="h-plain"><div class="wrap">
<div class="plain"><span class="q">?</span><div><h3 id="h-plain">{plain_q}</h3><p>{plain_a}</p></div></div>
<div class="head" style="margin-top:72px"><div><span class="eyebrow">Neler yapıyoruz</span><h2>İşin içinde neler var?</h2></div><p>Her adımı biz yürütürüz; senden yalnızca işletmeni anlatman ve onay vermen beklenir.</p></div>
<div class="do-grid">{dg}</div>
</div></section>
{mo}
<section aria-labelledby="h-deliv"><div class="wrap split">
<div>{visual}</div>
<div class="deliv"><span class="eyebrow">Teslim aldıkların</span><h3 id="h-deliv">{deliver_title}</h3>{checks(deliverables, "checks dark-checks")}</div>
</div></section>

<section id="fiyat" class="light" aria-labelledby="h-fiyat"><div class="wrap">
<div class="head"><div><span class="eyebrow">Fiyat</span><h2 id="h-fiyat">Ne ödeyeceğini baştan bil.</h2></div><p>Diğer paketler ve birleşik fiyatlar için <a class="link" href="fiyatlar.html">tüm fiyatlara</a> bak.</p></div>
<div class="table"><table><thead><tr><th scope="col">Paket</th><th scope="col">Fiyat</th></tr></thead><tbody>{rows}</tbody></table></div>
{terms_block()}
</div></section>
{faq_block(faq, "Bu hizmetle ilgili sorular.", "sss")}
{contact(need=need)}
'''
    return body

def page_web():
    visual = site_mock("modasalon.ornek","MODA · KADIKÖY","Saçın için sakin bir saat.","Kesim, renk ve bakım. Salı–Pazar 10:00–20:00.","WhatsApp'tan randevu al","salon-fon",[("Kesim + fön","45 dk"),("Dip boya","90 dk"),("Keratin bakım","120 dk")])
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
      [("Alan adı ve hosting ücreti ayrı mı?","Alan adı yıllık birkaç yüz lira tutar ve senin adına alınır; ilk yılı fiyata dahildir. Barındırmayı ücretsiz katmanlarda kuruyoruz, ek aylık ücret çıkmaz."),
       ("Siteyi sonra kendim değiştirebilir miyim?","Evet. Fiyat ve saat gibi sık değişen bilgileri nasıl güncelleyeceğini gösteririz. İstersen bakım paketiyle bunu biz yaparız."),
       ("Fotoğraflarım yok, ne olacak?","Telefonla nasıl çekeceğini anlatırız; gerekirse lisanslı stok fotoğraflarla başlarız, sen çektikçe değiştiririz."),
       ("Hazır şablon mu kullanıyorsunuz?","Hayır. Her site işletmenin renklerine, sektörüne ve müşterisine göre tasarlanır.")],
      "Web sitesi")
    return ("Web Tasarım | Laurus Dijital","Telefonda hızlı açılan, WhatsApp'tan randevu getiren web siteleri. Tek sayfa site 12.000 ₺, 7 günde yayında.", body)

def page_social():
    visual = f'<div style="display:flex;gap:20px;justify-content:center;flex-wrap:wrap">{igphone("modasalon","Kuaför · Kadıköy<br>Randevu için WhatsApp","salon-yikama",["salon-fon","#3B2418","salon-ic","nail","salon-yikama","#C99B7C"])}</div>'
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
    return ("Sosyal Medya Yönetimi ve Reels | Laurus Dijital","Instagram ve TikTok yönetimi, aylık içerik planı, Reels ve mesaj yönetimi. Aylık 12.000 ₺'den başlayan açık fiyatlar.", body)

def page_ads():
    visual = f'''<div style="display:grid;gap:18px;justify-items:center">
<div class="adcard" style="max-width:480px;width:100%"><div class="ad">Sponsorlu</div><div class="u">modasalon.ornek</div><h6>Moda Salon | Kadıköy'de Kuaför · Bugün Randevu</h6><p>Kesim, dip boya ve keratin bakım. Moda'da, iskeleye 5 dakika. WhatsApp'tan hemen randevu al.</p></div>
<div class="metaad"><div class="top"><i>{img("salon-yikama","")}</i><div><b>Moda Salon</b><small>Sponsorlu</small></div></div><div class="im">{img("salon-fon","")}</div><div class="cta"><div><small style="color:#65676B">Kadıköy · Moda</small><br><b>Bu hafta keratin bakımda yer var</b></div><span>Mesaj gönder</span></div></div>
</div>'''
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
    return ("Google Ads ve Meta Reklam Yönetimi | Laurus Dijital","Google arama, harita ve Instagram reklamları. Aylık 9.000 ₺ yönetim ücreti, bütçe senin kartından, her ay şeffaf rapor.", body)

def page_gbp():
    visual = f'''<div class="gmock" aria-label="Düzenlenmiş Google profili örneği">
<div class="sbar">{I['search']}<span>kahve bostancı</span></div>
<div class="photos">{img("kafe-masa","")}{img("kafe-latte","")}{img("kafe-kupa","")}</div>
<div class="bd"><h4>Köşe Kahve</h4><div class="meta">Kafe · Bostancı · <span class="open">Şu an açık</span> · 23:00'te kapanır</div>
<div class="acts"><span>Yol tarifi</span><span>Ara</span><span>Menü</span><span>Web sitesi</span></div>
<div class="rows"><div>Kahvaltı · Filtre kahve · Ev yapımı tatlı · Wi-Fi</div><div>Sahibinden yanıt: “Tekrar bekleriz!”</div></div></div></div>'''
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
      [("Profil kurulumu ve düzeni","Vitrin paketinin içinde ya da tek başına","Vitrin paketinde dahil"),("Aylık profil yönetimi","Haftalık gönderi, yorum yanıtı, fotoğraf güncelleme","Büyüme paketinde dahil")],
      [("Profilim zaten var ama ben açmadım, ne olacak?","Sahiplik talebiyle profili sana devrederiz. Google bunun için kısa bir doğrulama ister, adım adım birlikte yaparız."),
       ("Kötü yorumları sildirebilir misiniz?","Kurallara aykırı yorumları Google'a bildiririz; geri kalanına yapıcı bir yanıt yazarız. Sahte yorum ekleme hizmeti vermeyiz."),
       ("Adresimi göstermek istemiyorum, olur mu?","Evet. Eve hizmet veren ya da adres göstermek istemeyen işletmeler için hizmet bölgesi seçeneği var.")],
      "Google İşletme profili")
    return ("Google İşletme Profili ve Yerel SEO | Laurus Dijital","Google Haritalar'da öne çıkın: profil kurulumu, fotoğraflar, saatler, yorum akışı ve yerel arama ayarları.", body)

def page_cases():
    def row(cid, rev, vis_bg, visual, tag, name, sector, problem, did, result, items):
        return f'''<div class="case-row{' rev' if rev else ''}" id="{cid}">
<div class="vis">{img(vis_bg,"","",cls="bg")}{visual}</div>
<div><span class="tag">Örnek çalışma · {sector}</span><h2>{name}</h2>
<dl><div><dt>Durum</dt><dd>{problem}</dd></div><div><dt>Ne yaparız</dt><dd>{did}</dd></div><div><dt>Hedeflenen sonuç</dt><dd>{result}</dd></div></dl>
{checks(items)}<p style="margin-top:22px"><a class="btn btn-ink" href="#iletisim">Benim için de hazırla</a></p></div></div>'''
    r1 = row("moda-salon", False, "salon-ic", site_mock("modasalon.ornek","MODA · KADIKÖY","Saçın için sakin bir saat.","Kesim, renk ve bakım. Salı–Pazar 10:00–20:00.","WhatsApp'tan randevu al","salon-fon",[("Kesim + fön","45 dk"),("Dip boya","90 dk"),("Keratin","120 dk")]),
      "", "Moda Salon", "Kuaför",
      "Randevular telefonla ve Instagram DM'den karışık geliyor; Google profilinde fotoğraf yok, saatler eski.",
      "Tek sayfalık site kurarız: hizmet, süre ve fiyat listesi, her yerde WhatsApp'tan randevu düğmesi. Google profilini fotoğraflar, doğru saatler ve hizmet listesiyle tamamlarız.",
      "Randevuların tek kanaldan (WhatsApp) gelmesi, Google'dan gelen arama ve yol tarifi sayısının artması.",
      ["Tek sayfa site, 7 günde yayında","Google İşletme Profili düzeni","WhatsApp randevu mesaj şablonu"])
    r2 = row("patiler", True, "pet-kosan", f'{igphone("patilerpetkuafor","Pet kuaför · Ataşehir","pet-beyaz",["pet-kosan","#4AA3C8","pet-beyaz","#F2B880","#1F5F7E","pet-kosan"],"86","1.912","230")}<div class="metaad" style="width:240px"><div class="top"><i>{img("pet-beyaz","")}</i><div><b>Patiler Pet Kuaför</b><small>Sponsorlu</small></div></div><div class="im">{img("pet-beyaz","")}</div><div class="cta"><b>Tüy dökümü mevsimi</b><span>Randevu al</span></div></div>',
      "", "Patiler Pet Kuaför", "Pet kuaför",
      "Instagram'da ayda bir iki rastgele paylaşım var; müşteriler bakım zamanını unutuyor.",
      "Renkleri ve yazı dili tutarlı bir Instagram düzeni kurarız. Her ay önce/sonra Reels serisi ve mevsime göre bakım hatırlatan paylaşımlar; profilde randevu düğmesi.",
      "Bakım zamanı gelen müşterilerin hatırlatmayla geri dönmesi, mesajla gelen randevuların artması.",
      ["Aylık içerik takvimi","Önce/sonra Reels serisi","Mevsimsel kampanya görselleri"])
    r3 = row("kose-kahve", False, "kafe-kupa", f'''<div style="display:grid;gap:14px;max-width:460px;width:100%"><div class="adcard"><div class="ad">Sponsorlu</div><div class="u">kosekahve.ornek</div><h6>Köşe Kahve | Bostancı'da Sahil Kahvesi</h6><p>Taze kavrulmuş çekirdek, ev yapımı tatlılar. Sahile 2 dakika.</p></div>
<div class="gmock"><div class="photos" style="height:120px">{img("kafe-masa","")}{img("kafe-latte","")}{img("kafe-kupa","")}</div><div class="bd"><h4>Köşe Kahve</h4><div class="meta">Kafe · Bostancı · <span class="open">Şu an açık</span></div><div class="acts" style="margin-bottom:0"><span>Yol tarifi</span><span>Menü</span><span>Ara</span></div></div></div></div>''',
      "", "Köşe Kahve", "Kafe",
      "Sahile yakın ama ara sokakta; yoldan geçenler ve semtte yeni olanlar kafeyi bilmiyor.",
      "3 km çevrede “kahve”, “kahvaltı” arayanlara çıkan Google arama reklamı kurarız. Harita profilini menü, fotoğraflar ve güncel saatlerle düzenleriz.",
      "Haritadan gelen yol tarifi isteklerinin ve hafta sonu kahvaltı rezervasyonlarının artması.",
      ["Google arama reklamı (3 km)","Google İşletme Profili ve menü","Aylık sonuç raporu"])
    body = f'''
<section class="phero" aria-labelledby="h-page" style="padding-bottom:64px"><div class="wrap" style="grid-template-columns:1fr">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / Çalışmalar</nav>
<h1 id="h-page">Ne yaptığımızı adım adım gör.</h1>
<p class="lead">Her işletme için önce bir taslak hazırlarız. Aşağıda üç sektör için hazırladığımız örnek çalışmaları, durumu, yaptıklarımızı ve hedeflediğimiz sonucu anlatarak gösteriyoruz.</p>
<p class="muted" style="font-size:14px">İşletme adları örnektir. Gerçek müşteri çalışmalarımız, müşteri onayıyla burada yayınlanacak.</p></div>
</div></section>
<section class="white" style="padding:24px 0" aria-label="Örnek çalışmalar"><div class="wrap">{r1}{r2}{r3}</div></section>
<section class="light" style="padding:72px 0"><div class="wrap"><div class="band"><div><h2>Senin işletmen için de bir taslak hazırlayalım.</h2><p>Ücretsiz, 2–3 gün içinde. Beğenmezsen hiçbir şey ödemezsin.</p></div><a class="btn" href="#iletisim">Taslak iste</a></div></div></section>
{contact()}
'''
    return ("Çalışmalar | Laurus Dijital","Kuaför, pet kuaför ve kafe için hazırladığımız örnek çalışmalar: web sitesi, Instagram ve Google reklamı adım adım.", body)

def page_prices():
    rows = [
      ("Web sitesi", [("Tek sayfa site · Vitrin paketi","Site, Google İşletme kurulumu, WhatsApp düğmesi, ilk 8 Instagram paylaşımı. 7 günde yayında.","12.000 ₺"),("Kurumsal site","5 sayfa: hizmetler, hakkında, galeri, iletişim formu, temel SEO","22.000 ₺"),("Satış sitesi","Ürün kataloğu, online ödeme, sipariş paneli","35.000 ₺"),("Site bakımı","Güncellemeler, küçük değişiklikler, yedekleme","1.500 ₺ / ay")]),
      ("Sosyal medya", [("Başlangıç","Instagram, ayda 8 gönderi ve 8 hikâye, aylık rapor","12.000 ₺ / ay"),("Büyüme","Instagram + TikTok ya da Google profili, 12 gönderi, 4 Reels, yorum ve mesaj yönetimi","20.000 ₺ / ay")]),
      ("Reklam", [("Google ve/veya Meta reklam yönetimi","Kurulum, hedefleme, görseller ve aylık rapor dahil. Bütçe senin kartından.","9.000 ₺ / ay"),("Sosyal medya paketiyle birlikte","Başlangıç ya da Büyüme paketine eklendiğinde","7.500 ₺ / ay")]),
    ]
    tables = "".join(f'<h3 style="font-size:24px;margin:40px 0 16px">{g}</h3><div class="table"><table><thead><tr><th scope="col">Hizmet</th><th scope="col">Fiyat</th></tr></thead><tbody>' + "".join(f"<tr><td>{a}<small>{b}</small></td><td>{c}</td></tr>" for a,b,c in items) + "</tbody></table></div>" for g,items in rows)
    body = f'''
<section class="phero" aria-labelledby="h-page" style="padding-bottom:64px"><div class="wrap" style="grid-template-columns:1fr">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / Fiyatlar</nav>
<h1 id="h-page">Tüm fiyatlar, tek sayfada.</h1>
<p class="lead">Teklif beklemen gerekmez. Ne alacağını ve ne ödeyeceğini burada görürsün; fatura ayrıntıları ilk görüşmede netleşir.</p></div>
</div></section>
<section class="light" aria-labelledby="h-plans"><div class="wrap">
<div class="head"><div><span class="eyebrow">Önerdiğimiz paketler</span><h2 id="h-plans">Çoğu işletme buradan başlıyor.</h2></div><p>Paketler birbirinin yerine değil, üst üste çalışır: Vitrin ile başla, Büyüme ile devam et, istediğinde reklam ekle.</p></div>
{plans_block()}
{tables}
{terms_block()}
</div></section>
{faq_block(HOME_FAQ[:4], "Fiyatlarla ilgili sorular.", "sss")}
{contact()}
'''
    return ("Fiyatlar | Laurus Dijital","Web sitesi, sosyal medya yönetimi ve reklam yönetimi fiyatları. Tek sayfa site 12.000 ₺, sosyal medya aylık 12.000 ₺'den.", body)


SECTORS = [
 dict(slug="kuafor-dijital-pazarlama.html", short="Kuaför ve berber", name="kuaför ve berber", photo="salon-fon", photo_alt="Kuaförde fön çeken kuaför",
      h1="Kuaförler ve berberler için web sitesi, Instagram ve Google reklamı.",
      lead="Randevularını telefondan ve DM'den toplamaktan kurtul. Seni “yakınımdaki kuaför” diye arayan kişi bulsun, fiyatını görsün, WhatsApp'tan randevu alsın.",
      pains=[("Randevular dağınık","Telefon, DM, WhatsApp; hangisi ne zaman geldi belli değil.","Tek bir WhatsApp randevu düğmesi ve hazır mesaj şablonu. Sitede, Instagram'da ve Google'da aynı yol."),
             ("Google'da görünmüyor","Haritada fotoğraf yok, saatler eski, yorumlar yanıtsız.","Google İşletme Profili'ni fotoğraf, saat, hizmet listesi ve yorum akışıyla tamamlarız."),
             ("Instagram düzensiz","Arada bir paylaşım, renkler ve dil tutarsız.","Aylık plan, önce/sonra Reels serisi ve tutarlı tasarım dili."),
             ("Boş saatler","Hafta içi öğleden sonra koltuklar boş kalıyor.","Boş saatlere özel Instagram ve Google reklamı, sadece 3–5 km çevrene.")],
      plan="Vitrin paketi + Büyüme paketi", case="moda-salon", kw="kuaför web sitesi, kuaför sosyal medya yönetimi, berber Instagram yönetimi"),
 dict(slug="guzellik-salonu-dijital-pazarlama.html", short="Güzellik salonu ve nail bar", name="güzellik salonu ve nail bar", photo="nail-is", photo_alt="Güzellik salonunda manikür yapılırken",
      h1="Güzellik salonları ve nail barlar için dijital pazarlama.",
      lead="Kampanyalarını doğru kişiye göster, işlerini Reels'le sergile, yorumlarını topla. Müşterin seni bulsun, güvensin, randevu alsın.",
      pains=[("İşler görünmüyor","Yaptığın tasarımlar telefonda kalıyor, profile düzenli yansımıyor.","Haftalık Reels ve galeri düzeni; her iş, bir sonraki müşterinin vitrini olur."),
             ("Kampanyalar duyulmuyor","Paket ve indirimler sadece mevcut takipçiye ulaşıyor.","Semtine özel Meta reklamı; mesaj ve randevu odaklı kampanyalar."),
             ("Dönemsel müşteri kaybı","Bakım zamanı gelen müşteri dönmeyi unutuyor.","Hatırlatma paylaşımları ve WhatsApp mesaj şablonları."),
             ("Yorum az","Memnun müşteri yorum bırakmıyor.","Yorum isteme bağlantısı ve ödeme sonrası gönderilecek hazır mesaj.")],
      plan="Büyüme paketi + Reklam", case="moda-salon", kw="güzellik salonu sosyal medya yönetimi, nail bar Instagram, güzellik salonu reklam"),
 dict(slug="pet-kuafor-dijital-pazarlama.html", short="Pet kuaför", name="pet kuaför", photo="pet-beyaz", photo_alt="Bakımı yapılmış beyaz köpek",
      h1="Pet kuaförler için Instagram, web sitesi ve yerel reklam.",
      lead="Bakım zamanı gelen müşteriyi geri getir, yeni hayvan sahiplerine semtinde ulaş. Önce/sonra paylaşımlarla güven kazan.",
      pains=[("Bakım zamanı unutuluyor","Müşteri 6–8 haftada bir gelmesi gerekirken aylarca kayboluyor.","Mevsime ve ırka göre bakım hatırlatan paylaşımlar ve WhatsApp şablonları."),
             ("Güven eksikliği","Yeni müşteri hayvanını kime emanet ettiğini görmek istiyor.","Önce/sonra Reels serisi, salon fotoğrafları ve gerçek yorumlar."),
             ("Sadece çevre biliyor","Semte yeni taşınanlar seni bulmuyor.","Google İşletme Profili ve 3 km çevreye Google/Meta reklamı."),
             ("Fiyat soruları","Aynı soru her gün DM'den geliyor.","Sitede ve profilde açık hizmet ve fiyat listesi.")],
      plan="Vitrin paketi + Büyüme paketi", case="patiler", kw="pet kuaför web sitesi, pet kuaför Instagram, köpek kuaförü reklam"),
 dict(slug="kafe-restoran-dijital-pazarlama.html", short="Kafe ve restoran", name="kafe ve restoran", photo="kafe-latte", photo_alt="Kafede latte ve bitkiler",
      h1="Kafeler ve restoranlar için Google, Instagram ve yerel reklam.",
      lead="“Yakınımdaki kahveci” arayan kişi seni bulsun. Menün, saatlerin ve fotoğrafların güncel olsun; hafta sonu masaların dolsun.",
      pains=[("Haritada kayıp","Ara sokaktasın, yoldan geçen bilmiyor.","Google İşletme Profili, menü ve fotoğraflar; 3 km çevreye arama reklamı."),
             ("Menü güncel değil","Fiyatlar ve ürünler değişiyor, internette eski kalıyor.","Siteye ve profile bağlı, kolay güncellenen menü sayfası."),
             ("Hafta içi sakin","Yoğunluk sadece hafta sonu.","Hafta içi saatlerine özel kampanya paylaşımları ve reklamlar."),
             ("Fotoğraflar zayıf","Ürünler telefonda iştah açmıyor.","Basit çekim rehberi ve düzenlenmiş ürün görselleri.")],
      plan="Vitrin paketi + Reklam", case="kose-kahve", kw="kafe sosyal medya yönetimi, restoran Google reklam, kafe web sitesi"),
]

def sector_page(sec):
    rows = "".join(f'<div class="do"><span class="ic">{I["target"]}</span><h3>{t}</h3><p><b>Sorun:</b> {a}</p><p><b>Çözümümüz:</b> {b}</p></div>' for t,a,b in sec["pains"])
    others = " · ".join(f'<a class="link" href="{x["slug"]}">{x["short"]}</a>' for x in SECTORS if x is not sec)
    faq = [(f"{sec['short']} için hangi paketle başlamalıyım?", f"Çoğu {sec['name']} işletmesine önerimiz: {sec['plan']}. İlk görüşmede mevcut hesaplarına bakıp net öneri veririz."),
           ("Ne kadar sürede sonuç alırım?","Site ve Google profili yayına girdiği gün görünür olursun. Reklamlarda ilk mesajlar genelde ilk haftada gelir; sosyal medyada düzenli etki 2–3 ayda belirginleşir."),
           ("Başka şehirdeyim, olur mu?","Evet, tüm süreç online ilerliyor; reklam ve Google profili senin semtine göre ayarlanır.")]
    body = f"""
<section class="phero" aria-labelledby="h-page"><div class="wrap">
<div><nav class="crumbs" aria-label="Konum"><a href="index.html">Ana sayfa</a> / Sektörler / {sec['short']}</nav>
<h1 id="h-page">{sec['h1']}</h1><p class="lead">{sec['lead']}</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="calismalar.html#{sec['case']}">Örnek çalışmayı gör</a></div></div>
<div class="ph">{img(sec['photo'], sec['photo_alt'], eager=True)}</div>
</div></section>
<section class="light" aria-labelledby="h-pains"><div class="wrap">
<div class="head"><div><span class="eyebrow">{sec['short']}</span><h2 id="h-pains">{sec['short']} işletmelerinin dijitalde en sık yaşadığı dört sorun ve çözümü.</h2></div><p>Bu sektörde en sık karşılaşılan sorunlar bunlar. Her biri için ne yaptığımızı sade bir dille anlattık.</p></div>
<div class="do-grid" style="grid-template-columns:repeat(2,1fr)">{rows}</div>
</div></section>
<section aria-labelledby="h-plan"><div class="wrap"><div class="band"><div><h2 id="h-plan">Önerimiz: {sec['plan']}</h2><p>Fiyatlar açık, ilk 7 günde yayında. Paketlerin içeriğini fiyatlar sayfasında görebilirsin.</p></div><a class="btn" href="fiyatlar.html">Paketleri incele</a></div>
<p class="muted" style="margin-top:28px">Diğer sektörler: {others}</p></div></section>
{faq_block(faq, f"{sec['short']} için sık sorulanlar.", "sss")}
{contact()}
"""
    return (f"{sec['short']} için Web Sitesi, Sosyal Medya ve Reklam | Laurus Dijital",
            f"{sec['short']} işletmeleri için web sitesi, Instagram yönetimi, Google İşletme Profili ve yerel reklam. Fiyatlar açık, 7 günde yayında.", body)

PAGES = {
  "index.html": (page_index, ""),
  "web-tasarim.html": (page_web, "svc"),
  "sosyal-medya.html": (page_social, "svc"),
  "reklam-yonetimi.html": (page_ads, "svc"),
  "google-isletme.html": (page_gbp, "svc"),
  "calismalar.html": (page_cases, "calismalar"),
  "fiyatlar.html": (page_prices, "fiyatlar"),
}
for _sec in SECTORS:
    PAGES[_sec["slug"]] = ((lambda sec=_sec: sector_page(sec)), "")

PAGE_META.update({
  "web-tasarim.html": dict(crumb=[("Web tasarım","/web-tasarim")], service=("Web tasarım","12000","Telefonda hızlı açılan, WhatsApp'tan randevu getiren web siteleri.")),
  "sosyal-medya.html": dict(crumb=[("Sosyal medya ve içerik","/sosyal-medya")], service=("Sosyal medya yönetimi","12000","Instagram ve TikTok yönetimi, aylık içerik planı ve Reels.")),
  "reklam-yonetimi.html": dict(crumb=[("Google ve Meta reklamları","/reklam-yonetimi")], service=("Google Ads ve Meta reklam yönetimi","9000","Google arama, harita ve Instagram reklamları.")),
  "google-isletme.html": dict(crumb=[("Google İşletme ve yerel SEO","/google-isletme")], service=("Google İşletme Profili ve yerel SEO","12000","Google Haritalar profil kurulumu, fotoğraflar ve yorum akışı.")),
  "calismalar.html": dict(crumb=[("Çalışmalar","/calismalar")]),
  "fiyatlar.html": dict(crumb=[("Fiyatlar","/fiyatlar")]),
})
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
    urls = "".join(f"<url><loc>{BASE}{'/' if s=='index.html' else '/'+s.replace('.html','')}</loc></url>" for s in PAGES)
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
    t = t.replace('href="#','href="/#')
    t = re.sub(r'<link rel="canonical"[^>]*>\n?','',t).replace('content="index, follow, max-image-preview:large"','content="noindex, follow"')
    open(p404,"w").write(t)
    css = os.path.join(OUT,"assets","site.css")
    c = open(css).read().replace("url(../fonts/","url(/fonts/")
    open(css,"w").write(c)
    open(os.path.join(OUT,"_headers"),"w").write("/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: DENY\n/fonts/*\n  Cache-Control: public, max-age=31536000, immutable\n/img/*\n  Cache-Control: public, max-age=2592000\n/assets/*\n  Cache-Control: public, max-age=86400\n")
    print("built", len(PAGES), "pages ->", OUT)

if __name__ == "__main__":
    build()
