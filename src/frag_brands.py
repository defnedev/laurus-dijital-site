# ---------- sample brand showcase (designed mockups) ----------
BRANDS = [
  dict(id="moda", name="Moda Salon", sector="Kuaför", city="Kadıköy, Moda",
       logo='<span class="lg-moda">Moda<em>Salon</em></span>', mono="M",
       pal=[("#2E1A24","Mürdüm"),("#F4E4DC","Pudra"),("#B8875F","Bakır"),("#FFFDFB","Krem")],
       fonts="Başlık: serif · Metin: sade sans",
       h="Saçın için sakin bir saat.", p="Kesim, renk ve bakım. Salı–Pazar 10:00–20:00, Moda iskelesine 5 dakika.",
       hero="salon-fon", nav=["Hizmetler","Fiyatlar","Galeri","İletişim"],
       items=[("Kesim + fön","45 dk","650 ₺"),("Dip boya","90 dk","1.400 ₺"),("Keratin bakım","120 dk","2.200 ₺")],
       handle="modasalon.kadikoy", bio="Kuaför · Moda, Kadıköy<br>Randevu için WhatsApp ↓",
       grid=["salon-yikama",("Gelin saçı<br>sezonu açıldı","#2E1A24","#F4E4DC"),"salon-ic",("Hafta içi<br>%15 dip boya","#B8875F","#FFFDFB"),"salon-fon","nail",("Önce / sonra<br>Keratin","#F4E4DC","#2E1A24"),"salon-yikama","salon-ic"],
       did=["Tek sayfa site ve WhatsApp randevu düğmesi","Google profili: fotoğraf, saat, hizmet listesi","Instagram için renk ve yazı düzeni"],
       case="Randevular telefondan ve DM'den karışık geliyor; Google profilinde fotoğraf yok, saatler eski."),
  dict(id="patiler", name="Patiler", sector="Pet kuaför", city="Ataşehir",
       logo='<span class="lg-pat"><b>pati</b>ler</span>', mono="p",
       pal=[("#1F5F9E","Gök"),("#FFC845","Güneş"),("#EAF4FB","Bulut"),("#14263A","Lacivert")],
       fonts="Başlık: yuvarlak, kalın · Metin: sade sans",
       h="Mis gibi, mutlu, bakımlı.", p="Yıkama, tıraş ve tırnak bakımı. Ataşehir'de, randevuyla, sakin bir ortamda.",
       hero="pet-beyaz", nav=["Bakımlar","Fiyatlar","Önce/Sonra","Ulaşım"],
       items=[("Küçük ırk bakım","60 dk","900 ₺"),("Orta ırk bakım","90 dk","1.250 ₺"),("Tırnak + kulak","20 dk","300 ₺")],
       handle="patiler.petkuafor", bio="Pet kuaför · Ataşehir<br>Tüy dökümü mevsimi başladı 🐾",
       grid=["pet-kosan",("Tüy dökümü<br>mevsimi","#FFC845","#14263A"),"pet-beyaz",("Önce / sonra<br>Maltipoo","#1F5F9E","#FFFFFF"),"pet-kosan",("Bakım zamanı<br>geldi mi?","#EAF4FB","#1F5F9E"),"pet-beyaz","pet-kosan",("Yeni müşteriye<br>tırnak hediye","#14263A","#FFC845")],
       did=["Renkleri tutarlı Instagram düzeni","Her ay önce/sonra Reels serisi","Bakım zamanını hatırlatan paylaşımlar"],
       case="Instagram'da ayda bir iki rastgele paylaşım var; müşteriler bakım zamanını unutuyor."),
  dict(id="kose", name="Köşe Kahve", sector="Kafe", city="Bostancı",
       logo='<span class="lg-kose">köşe<i>kahve</i></span>', mono="k",
       pal=[("#2A1B12","Espresso"),("#EADBC4","Krema"),("#6E7B3B","Zeytin"),("#C8692F","Tarçın")],
       fonts="Başlık: el yazısına yakın serif · Metin: sade sans",
       h="Sahile iki dakika, kahveye bir adım.", p="Taze kavrulmuş çekirdek, ev yapımı tatlılar ve hafta sonu kahvaltısı.",
       hero="kafe-latte", nav=["Menü","Kahvaltı","Saatler","Yol tarifi"],
       items=[("Filtre kahve","","95 ₺"),("Flat white","","120 ₺"),("Serpme kahvaltı","2 kişilik","890 ₺")],
       handle="kosekahve.bostanci", bio="Kafe · Bostancı<br>Her gün 08:00–22:00",
       grid=["kafe-masa",("Hafta sonu<br>kahvaltısı","#2A1B12","#EADBC4"),"kafe-latte","kafe-kupa",("Yeni çekirdek:<br>Etiyopya","#6E7B3B","#FFFFFF"),"kafe-masa",("Sahile<br>2 dakika","#EADBC4","#2A1B12"),"kafe-kupa","kafe-latte"],
       did=["3 km çevreye Google arama reklamı","Menü ve fotoğraflarla harita profili","Kolay güncellenen menü sayfası"],
       case="Sahile yakın ama ara sokakta; yoldan geçenler ve semte yeni gelenler kafeyi bilmiyor."),
]

def b_site(b):
    nav = "".join(f"<span>{x}</span>" for x in b["nav"])
    items = "".join(f'<div><b>{a}</b><small>{d}</small><span>{p}</span></div>' for a,d,p in b["items"])
    return f'''<div class="bsite b-{b["id"]}" data-fit="1000"><div class="bs-nav">{b["logo"]}<nav>{nav}</nav><span class="bs-cta">Randevu al</span></div>
<div class="bs-hero"><div class="bs-tx"><small>{b["city"]}</small><h3>{b["h"]}</h3><p>{b["p"]}</p><div class="bs-btns"><span class="b1">WhatsApp'tan yaz</span><span class="b2">Fiyatları gör</span></div></div><div class="bs-im">{img(b["hero"],"")}</div></div>
<div class="bs-list">{items}</div></div>'''

def b_ig(b):
    g = ""
    for x in b["grid"]:
        if isinstance(x, tuple):
            t,bg,fg = x; g += f'<i class="tx" style="background:{bg};color:{fg}"><span>{t}</span></i>'
        else:
            g += f'<i>{img(x,"")}</i>'
    return f'''<div class="big b-{b["id"]}" data-fit="380"><div class="ig-top"><b>{b["handle"]}</b></div>
<div class="ig-h"><span class="ig-av">{b["logo"]}</span><div class="ig-n"><div><b>{len(b["grid"])*9}</b>gönderi</div><div><b>Örnek</b>hesap</div></div></div>
<div class="ig-bio"><b>{b["name"]}</b><br>{b["bio"]}</div>
<div class="ig-bt"><span class="p">Mesaj gönder</span><span>Randevu</span></div>
<div class="ig-g">{g}</div></div>'''

def b_stage(b, cls=""):
    return f'''<div class="stage {cls}"><div class="laptop"><div class="lid"><div class="scr">{b_site(b)}</div></div><div class="base"></div></div>
<div class="phone"><div class="pscr">{b_ig(b)}</div></div></div>'''

def hero_showcase():
    sets = "".join(f'<div class="show-set{" on" if i==0 else ""}" data-show="{b["id"]}"{"" if i==0 else " aria-hidden=\"true\""}>{b_stage(b)}</div>' for i,b in enumerate(BRANDS))
    pills = "".join(f'<button type="button" data-show-btn="{b["id"]}" aria-pressed="{"true" if i==0 else "false"}"><b>{b["name"]}</b><small>{b["sector"]}</small></button>' for i,b in enumerate(BRANDS))
    return f'''<div class="showcase" data-showcase><div class="show-stage">{sets}</div>
<div class="show-bar"><span>Örnek işler: site ve Instagram</span><div class="show-pills" role="group" aria-label="Örnek marka seç">{pills}</div></div></div>'''

def brand_case(b):
    sw = "".join(f'<span><i style="background:{c}"></i>{n}</span>' for c,n in b["pal"])
    return f'''<div class="bcase">
<div class="bcase-vis b-{b["id"]}-bg">{b_stage(b,"big")}</div>
<div class="bcase-tx">
<div class="bcase-id"><span class="bcase-logo b-{b["id"]}">{b["logo"]}</span><div><b>{b["name"]}</b><small>Örnek çalışma, {b["sector"].lower()}</small></div></div>
<h3>Durum</h3><p>{b["case"]}</p>
<h3>Ne yaparız</h3>{checks(b["did"])}
<h3>Marka dili</h3><div class="swatches">{sw}</div><p class="fonts">{b["fonts"]}</p>
<a class="btn btn-gold" href="#iletisim">Benim için de hazırla</a>
</div></div>'''
