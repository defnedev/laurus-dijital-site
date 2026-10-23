
# ---------- cinematic app showcase (v10) ----------
SB_ICONS = '<svg viewBox="0 0 64 14" aria-hidden="true"><g fill="currentColor"><rect x="0" y="9" width="3" height="5" rx="1"/><rect x="5" y="6" width="3" height="8" rx="1"/><rect x="10" y="3" width="3" height="11" rx="1"/><rect x="15" y="0" width="3" height="14" rx="1"/><path d="M30 13.5l-2.6-3.2a4.2 4.2 0 0 1 5.2 0zM24.6 7a8.6 8.6 0 0 1 10.8 0l-1.5 1.8a6.2 6.2 0 0 0-7.8 0zM21.8 3.6a13 13 0 0 1 16.4 0l-1.5 1.9a10.6 10.6 0 0 0-13.4 0z"/><rect x="44" y="1.5" width="17" height="11" rx="3" fill="none" stroke="currentColor" stroke-width="1.4"/><rect x="46" y="3.5" width="12" height="7" rx="1.6"/><rect x="62" y="5" width="1.6" height="4" rx=".8"/></g></svg>'

def iph(src, alt, cls=""):
    return (f'<div class="iph {cls}"><div class="iph-scr"><div class="iph-sb"><b>9:41</b>{SB_ICONS}</div>'
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
       dev=lambda: (iph("os-start","oh same. giriş ekranı","b1") + iph("os-world","oh same. dünya ekranı: şu an nasılsın?","m") +
                    '<div class="fl fl-pills" aria-hidden="true"><span><i style="background:#F28A3C"></i>heyecanlı</span><span><i style="background:#E8457A"></i>mutlu</span><span><i style="background:#A44CF0"></i>sakin</span></div>'
                    '<div class="fl fl-count" aria-hidden="true"><b>340 kişi</b><span>senin gibi heyecanlı.</span><small>12\'si İstanbul\'da · 41 şehirde</small></div>')),
  dict(id="sorbi", name="Sorbi", kind="Web platformu", tag="Doğduğun an kaç kişide bir?",
       desc="Doğum tarihini yazıyorsun; doğduğun anın gökyüzünü ve haritanın kaç kişide bir görüldüğünü saniyeler içinde görüyorsun.",
       feats=["Kendi hesap motorumuz","Üyelik ve giriş sistemi","Paylaşılabilir kartlar"],
       status="sorbiapp.com'da yayında", url="https://sorbiapp.com", cta="Sorbi'yi aç",
       icon='<span class="as-ico-sorbi" aria-hidden="true">✦</span>',
       dev=lambda: (bwin("sorbi-d","sorbiapp.com","Sorbi ana sayfası, bilgisayar görünümü","bw") + iph("sb-chart","Sorbi doğum haritası ekranı","m") +
                    '<div class="fl fl-img"><img src="img/app/sb-cards.webp" alt="Sorbi Güneş, Ay ve yükselen kartları" loading="lazy"></div>'
                    '<div class="fl fl-stat" aria-hidden="true"><b>1.367.496</b><span>gök anı sayıldı</span></div>')),
  dict(id="sekiz", name="Sekiz8", kind="iOS uygulaması", tag="Karar veremediğinde salla.",
       desc="Aklındaki soruyu tut, telefonu salla; cevap topun içinde belirsin. Evet/hayır, kendi seçeneklerin ya da rastgele sayı için de aynı hareket.",
       feats=["Dört mod: Sekiz, Evet/Hayır, Seç, Sayı","Sallama sensörü ve titreşim","Temalar"],
       status="App Store'da yayında", url="https://apps.apple.com/tr/app/sekiz8/id6758377312", cta="App Store'da indir",
       icon='<img src="img/app/sk-icon.webp" alt="" width="56" height="56">',
       dev=lambda: (iph("sk-sec","Sekiz8 seçim modu","l") + iph("sk-evet","Sekiz8 evet/hayır modu","r") + iph("sk-sekiz","Sekiz8 ana ekranı","m shake") +
                    '<img class="fl fl-icon" src="img/app/sk-icon.webp" alt="" loading="lazy">')),
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
                   f'<div class="as-foot"><a class="btn as-cta" href="{a["url"]}" target="_blank" rel="noopener">{a["cta"]} <span aria-hidden="true">↗</span></a><span class="as-st"><i></i>{a["status"]}</span></div>'
                   f'</div><div class="as-dev"><div class="as-dv-in">{a["dev"]()}</div></div></div></article>')
    return (f'<section id="{sid}" class="appshow" data-appshow aria-labelledby="h-{sid}"><div class="as-pin">'
            f'{scenes}'
            f'<div class="wrap as-head"><div><span class="eyebrow">{eyebrow}</span><h2 id="h-{sid}">{h2}</h2></div>'
            f'<div class="as-tabs" role="tablist" aria-label="Uygulamalar">{tabs}<i class="as-bar" aria-hidden="true"><b data-as-bar></b></i></div></div>'
            f'</div></section>')
