def mimg(name, alt=""):
    return f'<img src="img/mock/{name}.webp" alt="{alt}" loading="lazy" decoding="async">'

REEL_COLS = [
  ["site-moda","ig-nil","site-otel","ig-dis"],
  ["ig-kose","site-nil","ig-butik","site-emlak"],
  ["site-dis","ig-moda","site-hukuk","ig-otel"],
  ["ig-emlak","site-butik","ig-hukuk","site-kose"],
  ["site-nil","ig-butik","site-moda","ig-kose"],
  ["ig-dis","site-otel","ig-nil","site-hukuk"],
]

def reel():
    cols = ""
    for i, col in enumerate(REEL_COLS):
        tiles = "".join(f'<div class="tile {"t-ig" if n.startswith("ig") else "t-site"}"><img src="img/mock/{n}.webp" alt="" decoding="async"{" loading=\"lazy\"" if i>2 else ""}></div>' for n in col)
        cols += f'<div class="rcol" style="--dur:{38+i*5}s;--dir:{"normal" if i%2==0 else "reverse"}"><div class="rtrack">{tiles}{tiles}</div></div>'
    return f'<div class="reel" aria-hidden="true"><div class="reel-plane">{cols}</div></div>'

def slide(w, i):
    chips = "".join(f"<span>{s}</span>" for s in w["svcs"])
    link = f'<a class="btn btn-gold" href="{w["url"]}" target="_blank" rel="noopener">Siteyi ziyaret et</a>' if w.get("url") else f'<a class="btn btn-gold" href="calismalar.html#{w["id"]}">Nasıl kurduk</a>'
    desc = w.get("note") or w.get("case")
    return f'''<article class="slide" style="--i:{i}"><div class="sl-vis bg-{w["id"]}"><div class="stage"><div class="laptop"><div class="lid"><div class="scr">{mimg("site-"+w["id"], w["name"]+" web sitesi")}</div></div><div class="base"></div></div><div class="phone"><div class="pscr">{mimg("ig-"+w["id"], w["name"]+" mobil görünüm")}</div></div></div></div>
<div class="sl-tx">{kind_tag(w)}<h3>{w["name"]}</h3><p class="sl-sub">{w["sector"]}, {w["city"]}</p><p class="sl-d">{desc}</p><div class="chips">{chips}</div><div class="sl-act">{link}</div></div></article>'''

MANIFESTO = "Müşterin seni önce Google'da arar, sonra Instagram'da inceler, en son WhatsApp'tan yazar. Bu üç anın üçünü de biz kuruyoruz, sen işine bakıyorsun."

def page_index():
    svc = [
      ("web-tasarim.html","site-moda","Web sitesi","Telefonda hızlı açılan, WhatsApp'tan randevu getiren site.","12.000 ₺'den"),
      ("sosyal-medya.html","ig-butik","Sosyal medya","Aylık plan, tasarım, Reels ve mesaj yönetimi.","12.000 ₺ / ay'dan"),
      ("reklam-yonetimi.html","site-otel","Google ve Meta reklamı","Seni arayan kişinin karşısına ilk sen çık.","9.000 ₺ / ay"),
      ("google-isletme.html","harita","Google profili ve SEO","Haritada ve aramalarda üst sıralara çık.","Vitrin paketine dahil"),
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
<p class="lead">Web sitesi, sosyal medya, Google reklamı ve SEO. Kuaförden otele, kliniğe kadar her işletme için tek ekip.</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="#calismalar">İşlerimizi gör</a></div>
</div>
<a class="h3-scroll" href="#manifesto" aria-label="Aşağı kaydır"><i></i></a>
</section>

<section id="manifesto" class="mani" aria-label="Ne yapıyoruz"><div class="mani-pin"><div class="wrap"><p class="mani-tx" data-mani>{words}</p></div></div></section>

<section id="hizmetler" class="light ksec" aria-labelledby="h-svc"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Hizmetler</span><h2 id="h-svc">Ne yapıyoruz?</h2></div><p>Tek hizmetle başla ya da hepsini birlikte al.</p></div>
<div class="svc3-row snap">{cards}</div>
</div></section>

<section id="calismalar" class="works3" aria-labelledby="h-works">
<div class="w3-pin"><div class="wrap w3-head" data-rv><div><span class="eyebrow">Çalışmalarımız</span><h2 id="h-works">Yaptığımız işler.</h2></div><p>Gerçek müşteri işlerimiz ve farklı sektörler için hazırladığımız örnek tasarımlar. <a class="link" href="calismalar.html">Hepsini incele</a></p></div>
<div class="w3-track snap" data-hscroll>{slides}</div>
<div class="wrap w3-prog" aria-hidden="true"><i data-hprog></i></div></div>
</section>

<section id="nasil" class="light ksec" aria-labelledby="h-proc"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Nasıl çalışıyoruz</span><h2 id="h-proc">İlk görüşmeden yayına 7 gün.</h2></div><p>Önce taslağı görürsün, sonra karar verirsin. Ödemenin yarısı taslağı beğendiğinde.</p></div>
<ol class="proc3" data-line><span class="pl" aria-hidden="true"><i></i></span>{st}</ol>
</div></section>

<section id="fiyatlar" class="ksec" aria-labelledby="h-price"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Fiyatlar</span><h2 id="h-price">Açık fiyat, sürpriz yok.</h2></div><p><a class="link" href="fiyatlar.html">Tüm fiyatları gör</a></p></div>
<div data-rv>{mini_plans()}</div>
</div></section>

<section id="sss" class="light ksec" aria-labelledby="h-sss"><div class="wrap kfaq">
<div data-rv><span class="eyebrow">Sık sorulanlar</span><h2 id="h-sss">Aklındaki sorular.</h2><p class="muted">Burada yoksa WhatsApp'tan yaz, aynı gün dönelim.</p></div>
{faq_list(HOME_FAQ[:4])}
</div></section>
{contact()}
'''
    return ("Laurus Dijital | Web Tasarım, Sosyal Medya, Google Reklam ve SEO Ajansı",
            "Kuaförden otele, kliniğe kadar her işletme için web sitesi, Instagram yönetimi, Google ve Meta reklamları ve SEO. Fiyatlar açık, ilk site 7 günde yayında.", body)

