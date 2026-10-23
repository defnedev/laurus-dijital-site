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

def page_index():
    svc = [
      ("web-tasarim.html","tasarim-laptop","Web sitesi","Telefonda hızlı açılan, WhatsApp'tan randevu getiren site.","12.000 ₺'den"),
      ("sosyal-medya.html","telefon-instagram","Sosyal medya","Aylık plan, tasarım, Reels ve mesaj yönetimi.","12.000 ₺ / ay'dan"),
      ("reklam-yonetimi.html","google-arama","Google ve Meta reklamı","Semtinde seni arayan kişinin karşısına çık.","9.000 ₺ / ay"),
      ("google-isletme.html","harita","Google profili ve yerel SEO","Haritada tam profil, düzenli yorum.","Vitrin paketine dahil"),
    ]
    cards = "".join(f'<a class="kcard" href="{h}"><div class="ph">{img(p,"")}</div><div class="in"><h3>{t}</h3><p>{d}</p><div class="ft"><span>{pr}</span><span class="go">İncele {I["arrow"]}</span></div></div></a>' for h,p,t,d,pr in svc)

    steps = [("1. gün","Tanışma","15 dakikalık görüşme; işletmeni ve hedefini dinleriz."),("2–3. gün","İlk taslak","Taslağı görürsün. Beğenmezsen ödeme yok."),("4–6. gün","Tamamlama","Metin, fotoğraf, Google profili. İki düzeltme turu."),("7. gün","Yayında","Siten açılır, profillerin hazır.")]
    p_steps = '<div class="ksteps">' + "".join(f'<div><span class="n">{i+1}</span><small>{d}</small><h3>{t}</h3><p>{x}</p></div>' for i,(d,t,x) in enumerate(steps)) + '</div><p class="knote">Ödemenin yarısı taslağı beğendiğinde, kalanı yayından önce.</p>'

    p_ba = f'''<div class="kba" data-ba>
<div><h3>Aynı işletme, iki farklı Google profili.</h3><p class="muted">Müşteri seni ilk gördüğünde karar verir.</p>
<div class="toggle" role="group" aria-label="Profil görünümü"><button type="button" data-ba-set="once" aria-pressed="false">Önce</button><button type="button" data-ba-set="sonra" aria-pressed="true">Sonra</button></div>
<ul class="ba-list" data-ba-view="once" hidden><li><span class="x">✕</span>Fotoğraf yok</li><li><span class="x">✕</span>Saatler yanlış</li><li><span class="x">✕</span>Site ve randevu yolu yok</li><li><span class="x">✕</span>Yorumlar yanıtsız</li></ul>
<ul class="ba-list" data-ba-view="sonra"><li><span class="ok">✓</span>Gerçek fotoğraflar</li><li><span class="ok">✓</span>Doğru saatler, “Şu an açık”</li><li><span class="ok">✓</span>WhatsApp'tan randevu</li><li><span class="ok">✓</span>Yanıtlanan yorumlar</li></ul></div>
<div>
<div class="gmock" data-ba-view="once" hidden aria-label="Bakımsız Google profili örneği"><div class="sbar">{I['search']}<span>kuaför moda kadıköy</span></div><div class="photos"><div class="empty">Fotoğraf eklenmemiş</div></div>
<div class="bd"><h4>Moda Kuaför</h4><div class="meta">Kuaför · <span class="closed">Saatler güncellenmedi</span></div><div class="acts"><span>Yol tarifi</span><span class="dim">Web sitesi yok</span><span class="dim">Randevu yok</span></div><div class="rows"><div class="na">2 yorum · son yorum 2 yıl önce</div></div></div></div>
<div class="gmock" data-ba-view="sonra" aria-label="Düzenlenmiş Google profili örneği"><div class="sbar">{I['search']}<span>kuaför moda kadıköy</span></div><div class="photos">{img("salon-yikama","")}{img("salon-fon","")}{img("salon-ic","")}</div>
<div class="bd"><h4>Moda Salon</h4><div class="meta">Kuaför · Kadıköy · <span class="open">Şu an açık</span></div><div class="acts"><span>Web sitesi</span><span>Yol tarifi</span><span>Ara</span><span>WhatsApp'tan randevu</span></div><div class="rows"><div>Yorumlar düzenli yanıtlanıyor</div></div></div></div>
</div></div>'''

    cases = [("calismalar.html#moda-salon","salon-yikama","Kuaför · Site + Google","Moda Salon"),("calismalar.html#patiler","pet-kosan","Pet kuaför · Instagram","Patiler Pet Kuaför"),("calismalar.html#kose-kahve","kafe-masa","Kafe · Google reklamı","Köşe Kahve")]
    p_cases = '<div class="ktiles">' + "".join(f'<a class="ktile" href="{h}">{img(p,"")}<span class="badge">Örnek çalışma</span><div><small>{s}</small><b>{t}</b></div></a>' for h,p,s,t in cases) + '</div><p class="knote">İşletme adları örnektir. <a class="link" href="calismalar.html">Nasıl kurguladığımızı adım adım gör →</a></p>'

    secs = [("kuafor-dijital-pazarlama.html","salon-fon","Kuaför ve berber"),("guzellik-salonu-dijital-pazarlama.html","nail","Güzellik ve nail bar"),("pet-kuafor-dijital-pazarlama.html","pet-beyaz","Pet kuaför"),("kafe-restoran-dijital-pazarlama.html","kafe-latte","Kafe ve restoran")]
    p_secs = '<div class="ktiles four">' + "".join(f'<a class="ktile" href="{h}">{img(p,"")}<div><b>{t}</b><small>Ne yapıyoruz →</small></div></a>' for h,p,t in secs) + '</div><p class="knote">Butik, çiçekçi, atölye: müşterisini telefondan bulan her işletmeyle çalışıyoruz.</p>'

    T = tabs([("nasil","Nasıl çalışıyoruz",p_steps),("once-sonra","Önce / sonra",p_ba),("ornekler","Örnek çalışmalar",p_cases),("sektorler","Sektörler",p_secs)], "Laurus hakkında")
    body = f'''
<section class="hero" aria-labelledby="h-hero"><div class="wrap">
<div>
<span class="kicker"><i></i>Yeni müşteri kabul ediyoruz</span>
<h1 id="h-hero">Müşterin seni arıyor. <em>Bulsun.</em></h1>
<p class="lead">Web sitesi, Instagram, Google profili ve reklamların tek ekipte. İşletmeni bulunur, güvenilir ve randevu alır hâle getiriyoruz.</p>
<div class="actions"><a class="btn btn-gold" href="#iletisim">Ücretsiz ön görüşme al</a><a class="btn btn-line" href="#hizmetler">Hizmetleri gör</a></div>
<div class="facts"><div><b>7 gün</b><span>ilk site yayında</span></div><div><b>%100</b><span>hesaplar senin adına</span></div><div><b>Açık</b><span>fiyat, sürpriz yok</span></div></div>
</div>
<div class="hero-visual">
<div class="hero-photo">{img("hero-salon","Bir kuaför salonunun resepsiyonunda müşteri ve çalışan tablet üzerinden randevu ayarlıyor",eager=True)}</div>
<div class="chip c1" aria-hidden="true"><span class="ic" style="background:#E8F0FE;color:#1A73E8">{I['search']}</span><span><b>“kuaför kadıköy”</b><small>Google'da ve haritada görünür</small></span></div>
<div class="chip c2" aria-hidden="true"><span class="ic" style="background:#E7F6EC;color:#1FA855">{I['wa']}</span><span><b>Yeni randevu talebi</b><small>“Cumartesi 14:00 boş mu?”</small></span></div>
</div></div></section>

<section id="hizmetler" class="light ksec" aria-labelledby="h-svc"><div class="wrap">
<div class="khead"><div><span class="eyebrow">Hizmetler</span><h2 id="h-svc">Ne yapıyoruz?</h2></div><p>Tek hizmetle başla ya da hepsini birlikte al.</p></div>
<div class="kcards">{cards}</div>
</div></section>

<section class="ksec" aria-labelledby="h-why"><div class="wrap">
<div class="khead"><div><span class="eyebrow">Laurus'u tanı</span><h2 id="h-why">Merak ettiğini seç.</h2></div></div>
{T}
</div></section>

<section id="fiyatlar" class="light ksec" aria-labelledby="h-price"><div class="wrap">
<div class="khead"><div><span class="eyebrow">Fiyatlar</span><h2 id="h-price">Açık fiyat, sürpriz yok.</h2></div><p><a class="link" href="fiyatlar.html">Tüm fiyatları gör →</a></p></div>
{mini_plans()}
</div></section>

<section id="sss" class="ksec" aria-labelledby="h-sss"><div class="wrap kfaq">
<div><span class="eyebrow">Sık sorulanlar</span><h2 id="h-sss">Aklındaki sorular.</h2><p class="muted">Burada yoksa WhatsApp'tan yaz, aynı gün dönelim.</p></div>
{faq_list(HOME_FAQ[:5])}
</div></section>
{contact()}
'''
    return ("Laurus Dijital | Web Tasarım, Sosyal Medya ve Reklam Ajansı · İstanbul",
            "İşletmeler için web sitesi, Instagram yönetimi, Reels, Google ve Meta reklamları. Fiyatlar açık, ilk site 7 günde yayında, tüm hesaplar senin adına.", body)

def service_page(slug, crumb, h1, lead, photo, photo_alt, plain_q, plain_a, does, visual, deliver_title, deliverables, month, price_rows, faq, need):
    dg = "".join(f'<div class="do"><span class="ic">{I[ic]}</span><h3>{t}</h3><p>{d}</p></div>' for ic,t,d in does)
    rows = "".join(f"<tr><td>{a}<small>{b}</small></td><td>{c}</td></tr>" for a,b,c in price_rows)
    t_do = f'<div class="kplain"><b>{plain_q}</b><p>{plain_a}</p></div><div class="do-grid">{dg}</div>'
    t_del = f'<div class="ksplit"><div class="vis">{visual}</div><div><h3 class="kh3">{deliver_title}</h3>{checks(deliverables)}</div></div>'
    items = [("ne-yapiyoruz","Neler yapıyoruz",t_do),("teslim","Elinde olanlar",t_del)]
    if month:
        items.append(("ritim","Bir ay nasıl geçer",'<div class="month">' + "".join(f"<div><b>{w}</b><h4>{t}</h4><p>{d}</p></div>" for w,t,d in month) + '</div>'))
    items.append(("fiyat","Fiyat",f'<div class="table"><table><thead><tr><th scope="col">Paket</th><th scope="col">Fiyat</th></tr></thead><tbody>{rows}</tbody></table></div>{terms_block()}<p class="knote">Birleşik fiyatlar için <a class="link" href="fiyatlar.html">tüm fiyatlara</a> bak.</p>'))
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

