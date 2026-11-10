# ===== v22: CV hazırlama ve kariyer danışmanlığı sayfaları =====
CV_DATE = "2026-11-10"
WA_CV = "https://wa.me/905434309702?text=" + "Merhaba%2C%20CV%27mi%20%C3%BCcretsiz%20taratmak%20istiyorum."

def cv_scanner():
    rows = [("İletişim bilgileri","",False),("Deneyim tarihleri","",False),("Yetenekler","tablo içinde",True),("Unvan","ikonla birleşmiş",True),("Eğitim","iki kolonlu düzen",True)]
    rh = "".join(f'<li><span class="cr-ic {"fx" if fx else "ok"}" aria-hidden="true"></span><span class="cr-t">{t}{f" <small>({n})</small>" if n else ""}</span>'
                 f'<span class="cr-s">{"<b class=no>okunmadı</b><b class=yes>okundu</b>" if fx else "<b class=ok>okundu</b>"}</span></li>' for t,n,fx in rows)
    return f'''<div class="cvscan" role="img" aria-label="Örnek CV okunabilirlik raporu: düzeltmeden önce 100 üzerinden 61, düzeltmeden sonra 94">
<div class="cvs-doc" aria-hidden="true"><div class="cd-top"><i class="cd-av"></i><div><i class="cd-l w60 g"></i><i class="cd-l w40"></i></div></div>
<div class="cd-cols"><div><i class="cd-h"></i><i class="cd-l"></i><i class="cd-l w80"></i><i class="cd-l w70"></i><i class="cd-h"></i><i class="cd-l w90"></i><i class="cd-l w60"></i><i class="cd-l w75"></i></div>
<div class="cd-side"><i class="cd-h"></i><i class="cd-chip"></i><i class="cd-chip"></i><i class="cd-chip s"></i><i class="cd-h"></i><i class="cd-l w80"></i><i class="cd-l w60"></i></div></div>
<i class="cvs-beam"></i></div>
<div class="cvs-rep" aria-hidden="true"><div class="cvr-h"><b>CV okunabilirlik raporu</b><small>örnek</small></div>
<div class="cvr-sc"><span class="sc-b">61</span><span class="sc-a">94</span><small><span class="sc-bt">/ 100 · 3 alan okunmuyor</span><span class="sc-at">/ 100 · tüm alanlar okunuyor</span></small></div>
<ul class="cvr-rows">{rh}</ul><p class="cvr-f">Rapor hangi alanın neden okunmadığını ve nasıl düzeltileceğini satır satır yazar.</p></div>
</div>'''

def cv_cta(title="CV'n okunuyor mu?|Ücretsiz öğren.", sub="CV'ni WhatsApp'tan gönder, okunabilirlik raporunu aynı gün yollayalım. Ödeme adımı yok."):
    return f'''<section class="ctab" aria-label="Ücretsiz CV taraması"><div class="ctab-bg" aria-hidden="true"><img src="img/planlama.webp" alt="" loading="lazy" decoding="async"></div>
<div class="wrap ctab-in" data-rv><span class="eyebrow">Ücretsiz CV taraması</span><h2>{_words(title)}</h2><p class="lead">{sub}</p>
<div class="actions"><a class="btn btn-gold js-wa" href="{WA_CV}">CV'mi ücretsiz tarat</a><a class="btn btn-line" href="cv-hazirlama.html#paketler">Paketleri gör</a></div></div></section>'''

CV_FAQ = [
 ("Gerçekten abonelik yok mu?","Yok. Her paket tek seferlik ödenir; otomatik yenilenen hiçbir ödeme kurmuyoruz ve kart bilgini istemiyoruz."),
 ("ATS nedir, CV'm neden eleniyor?","ATS, başvuruları insan görmeden önce okuyan yazılımdır. İki kolonlu düzenler, tablolar, ikonlar ve grafikler bu yazılımda parçalanır; adın bile yanlış alana düşebilir. Ücretsiz raporumuz hangi alanın okunmadığını gösterir."),
 ("Benim yerime başvuru yapıyor musunuz?","Hayır. Hesap şifreni istemiyoruz ve senin adına hiçbir siteye giriş yapmıyoruz. Danışmanlıkta profilini birlikte dolduruyor, ön yazını yazıyor ve sürecini takip ediyoruz; göndermek her zaman sende."),
 ("Kısa CV ile detaylı özgeçmiş arasındaki fark ne?","Kısa CV tek sayfadır; iş sitelerine yükleme ve hızlı başvurular içindir. Detaylı özgeçmiş iki sayfadır; e-postayla gönderdiğin kurumsal ve üst düzey başvurularda kullanılır. Pakette ikisi de var."),
 ("Ne kadar sürede hazır olur?","Okunabilirlik raporu aynı gün, hazırlanan dosyalar iki iş günü içinde teslim edilir. Danışmanlık görüşmesi için uygun saati sen seçersin."),
 ("Verilerim ne oluyor?","CV'n kişisel veridir ve yalnızca hizmeti vermek için kullanılır. Kimseyle paylaşılmaz; tek mesajla silinir, teslimden 90 gün sonra da kendiliğinden silinir."),
 ("İş bulma garantisi veriyor musunuz?","Hayır, veren kimseye de inanma. Verdiğimiz şey işe yarayan bir CV, doğru doldurulmuş profiller ve birlikte çalışılan zaman."),
]

def page_cv():
    promises = [("x","Abonelik diye bir şey yok","Hizmeti alırsın, dosyalarını indirirsin, biter. Otomatik yenilenen hiçbir ödeme kurmuyoruz."),
                ("lock","Kart bilgini istemiyoruz","Ödeme tek seferliktir. Kart numaranı bize vermen, bir yere kaydetmemiz söz konusu değil."),
                ("trash","İsteyince verin silinir","CV'n kişisel veridir. Tek mesajla tüm kaydını sileriz; teslimden 90 gün sonra kendiliğinden de silinir.")]
    PIC = {"x":'<path d="M18 6 6 18M6 6l12 12"/>',"lock":'<rect x="4" y="10" width="16" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',"trash":'<path d="M3 6h18M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6M10 11v6M14 11v6M9 6V4h6v2"/>'}
    pr = "".join(f'<div class="cvp" data-rv style="--d:{i*90}ms"><span class="cvp-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{PIC[k]}</svg></span><h3>{t}</h3><p>{d}</p></div>' for i,(k,t,d) in enumerate(promises))
    steps = [("5 dakika","CV'ni gönder","Mevcut CV'ni WhatsApp'tan ya da e-postayla yolla. CV'n yoksa 12 soruluk kısa formu birlikte dolduralım."),
             ("Aynı gün","Raporunu al","Ücretsiz. Hangi alanın neden okunmadığını satır satır görürsün."),
             ("2 iş günü","Dosyalarını indir","Kısa CV ve detaylı özgeçmiş; Türkçe ve İngilizce, PDF ve Word."),
             ("Teslimde","Nereye ne yazılır","İş sitelerindeki profil alanlarına ne gireceğin, kopyala-yapıştır hazır metinlerle.")]
    st = "".join(f'<li data-rv style="--d:{i*120}ms"><span class="n">{i+1}</span><small>{d}</small><h3>{t}</h3><p>{x}</p></li>' for i,(d,t,x) in enumerate(steps))
    where = [("İş ilanı siteleri","Profil formu alanları, pozisyon ve şehir tercihi, yetenek etiketleri"),
             ("Profesyonel ağ","Başlık, hakkında metni, yetenek bölümü ve beceri sıralaması"),
             ("Kamu portalı","Meslek kodu seçimi ve beceri beyanı"),
             ("Şirket panelleri","Maaş beklentisi, ön yazı kutusu, “neden bu pozisyon” sorusu")]
    wh = "".join(f'<li data-rv style="--d:{i*80}ms"><b>{a}</b><span>{b}</span></li>' for i,(a,b) in enumerate(where))
    plans = [("CV","1.290 ₺","tek seferlik","Hızlıca okunur bir CV isteyenler",["Kısa CV, Türkçe ve İngilizce","Detaylı özgeçmiş, Türkçe","ATS okunabilirlik raporu","PDF ve Word","2 düzeltme turu"],"","CV paketi"),
             ("CV + Başvuru Kiti","2.490 ₺","tek seferlik","Aktif başvuru yapanlar",["CV paketinin tamamı","Detaylı özgeçmiş, İngilizce","5 ilana özel ön yazı","Her ilan için maaş rakamı ve gerekçesi","Profil alanları için hazır metinler"],"hot","CV + Başvuru Kiti"),
             ("Birebir Danışmanlık","Görüşmede netleşir","ihtiyacına göre","Süreci biriyle birlikte yürütmek isteyenler",["Başvuru Kiti'nin tamamı","60 dakika birebir görüşme","Profil kurulumu ve alan doldurma desteği","Başvurduğun sitelerde ön yazı yazımı","10 gün WhatsApp desteği ve süreç takibi"],"","Birebir danışmanlık")]
    ph = ""
    for n,p,u,f,l,h,key in plans:
        tag = '<span class="tag">En çok seçilen</span>' if h else ''
        bc = 'btn-gold' if h else 'btn-ink'
        msg = "Merhaba%2C%20" + key.replace(" ","%20").replace("+","%2B").replace("'","%27") + "%20ile%20ilgileniyorum."
        lab = "İletişime geç" if p.startswith("Görüşmede") else "Bu paketi seç"
        pcls = " ask" if p.startswith("Görüşmede") else ""
        ph += f'<div class="kplan {h}" data-rv>{tag}<h3>{n}</h3><p class="for">{f}</p><div class="price{pcls}">{p} <small>{u}</small></div>{checks(l)}<a class="btn {bc} js-wa" href="https://wa.me/905434309702?text={msg}">{lab}</a></div>'
    guides = [("cv-ornekleri.html","CV örnekleri","Mesleğine göre hazır örnekler ve güçlü madde önerileri."),
              ("ats-uyumlu-cv.html","ATS uyumlu CV","Yazılımın okuyabildiği CV için 10 kural ve kontrol listesi."),
              ("ingilizce-cv.html","İngilizce CV","Başlık karşılıkları, güçlü fiiller ve örnek özet."),
              ("on-yazi-ornegi.html","Ön yazı örnekleri","Deneyimli, yeni mezun ve kariyer değiştiren için 3 hazır şablon."),
              ("maas-beklentisi.html","Maaş beklentisi","Formdaki kutuya ve mülakatta ne yazılır, nasıl söylenir."),
              ("cv-ornekleri.html#cv-nasil-yazilir","CV nasıl yazılır","Yedi bölümde, sırasıyla, ne yazılır.")]
    gh = "".join(f'<a class="cvg" href="{h}" data-rv style="--d:{i*70}ms"><b>{t}</b><span>{d}</span><i aria-hidden="true">{I["arrow"]}</i></a>' for i,(h,t,d) in enumerate(guides))
    body = f'''
{cine_hero("CV hazırlama","CV hazırlama ve kariyer danışmanlığı","CV'n işverene|ulaşmıyor olabilir.","Başvurular artık önce yazılıma düşüyor. Güzel görünen bir CV, yazılım onu okuyamıyorsa hiç gönderilmemiş sayılır. CV'ni okunur hale getiriyor, nereye nasıl yükleyeceğini gösteriyor, istersen telefonda birlikte oturuyoruz.",["planlama","tasarim-laptop","kadin-telefon"],f'<a class="btn btn-gold js-wa" href="{WA_CV}">CV\'mi ücretsiz tarat</a><a class="btn btn-line" href="#paketler">Paketleri gör</a>','',
  '<ul class="cv-pills"><li>Abonelik yok</li><li>Kart bilgisi istemiyoruz</li><li>Tek seferlik ödeme</li></ul>')}
<section class="cvx" aria-labelledby="h-cvx"><div class="wrap cvx-g">
<div class="cvx-tx" data-rv><span class="eyebrow">Ücretsiz okunabilirlik raporu</span><h2 id="h-cvx">{_words("Yazılım senin CV'ni|nasıl okuyor?")}</h2>
<p class="lead">Başvurduğun şirketlerin çoğu CV'ni önce bir yazılıma okutur. Tablo içindeki yetenekler, ikonla birleşmiş unvanlar ve iki kolonlu düzenler bu yazılımda kaybolur. Raporumuz hangi alanın okunmadığını ve nasıl düzeltileceğini satır satır gösterir.</p>
<div class="actions"><a class="btn btn-gold js-wa" href="{WA_CV}">CV'mi gönder</a><a class="btn btn-line" href="ats-uyumlu-cv.html" data-pt="ATS uyumlu CV">ATS nedir?</a></div></div>
<div data-rv>{cv_scanner()}</div></div></section>
<section class="light ksec" aria-labelledby="h-prom"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Önce şunu netleştirelim</span><h2 id="h-prom">Üç yazılı söz.</h2></div><p>CV sitelerinden en çok duyulan şikayet ürünle değil ödemeyle ilgili: “tek seferlik” diye alınan hizmet aylık kesintiye dönüşüyor. Bizde böyle bir şey yok.</p></div>
<div class="cvps">{pr}</div></div></section>
<section class="ksec" aria-labelledby="h-steps"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Nasıl çalışır</span><h2 id="h-steps">Dört adımda hazır.</h2></div><p>Raporun aynı gün, dosyaların iki iş günü içinde elinde.</p></div>
<ol class="proc3" data-line><span class="pl" aria-hidden="true"><i></i></span>{st}</ol></div></section>
<section class="cvw" aria-labelledby="h-cvw"><div class="wrap cvw-g">
<div data-rv><span class="eyebrow">Kimsenin söylemediği kısım</span><h2 id="h-cvw">{_words("Yüklediğin PDF çoğu zaman|işverene gitmiyor.")}</h2>
<p class="lead">Büyük iş sitelerinde başvurduğunda işverenin gördüğü şey çoğu zaman sitenin kendi profil formudur. O alanlar boşsa en güzel PDF bile fark etmez.</p>
<p class="lead">CV'ni hazırlarken o alanlara ne yazılacağını da veriyoruz: unvan, yetenek listesi, pozisyon tercihleri, maaş kutusu. Tek tek, kopyala-yapıştır hazır.</p></div>
<div class="cvw-card" data-rv><b>Nereye ne yazılır</b><ul>{wh}</ul></div></div></section>
<section id="paketler" class="light ksec" aria-labelledby="h-pk"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Paketler</span><h2 id="h-pk">Fiyatlar açık.</h2></div><p>Deneme süresi, sepet ve otomatik yenileme yok. Danışmanlığın kapsamını ihtiyacına göre görüşmede birlikte belirliyoruz.</p></div>
<div class="kplans">{ph}</div>
<div class="cvjet" data-rv><span><b>Sadece bir ön yazı mı lazım?</b> Jeton al: 1 jeton = 1 ilana özel ön yazı ve o ilan için maaş rakamı. 1 jeton 249 ₺, 5 jeton 990 ₺. Jetonların süresi dolmaz.</span><a class="btn btn-ink js-wa" href="https://wa.me/905434309702?text=Merhaba%2C%20%C3%B6n%20yaz%C4%B1%20jetonu%20almak%20istiyorum.">Jeton al</a></div>
</div></section>
<section class="ksec" aria-labelledby="h-hum"><div class="wrap cvh-g">
<div data-rv><span class="eyebrow">İnsan desteği</span><h2 id="h-hum">{_words("Karşında konuşabileceğin|biri var.")}</h2>
<p class="lead">Hangi pozisyonlara başvurmalısın, profilindeki hangi alan boş kalmış, maaş kutusuna ne yazmalısın, mülakatta kariyer boşluğunu nasıl anlatmalısın? Bunlar form doldurarak çözülmüyor.</p>
<p class="lead">Danışmanlıkta profilini birlikte kuruyoruz, başvurduğun ilanlara ön yazıyı biz yazıyoruz ve 10 gün boyunca süreci birlikte takip ediyoruz.</p>
<p class="muted">İş bulma garantisi vermiyoruz, veren kimseye de inanma. Verdiğimiz şey yöntem, hazırlık ve birlikte çalışılan zaman.</p></div>
<div class="cvc" data-rv><b>Doğrudan iletişim</b>
<a class="btn btn-gold js-wa" href="{WA_CV}">{I["wa"] if "wa" in I else ""}WhatsApp'tan yaz</a>
<a class="btn btn-line" href="tel:+905434309702">Telefonla ara: 0543 430 97 02</a>
<a class="cvc-l" href="mailto:merhaba@laurusdijital.com">merhaba@laurusdijital.com</a>
<small>Hafta içi 09.00–19.00 · aynı gün dönüş</small></div></div></section>
<section class="light ksec" aria-labelledby="h-gd"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Ücretsiz rehberler</span><h2 id="h-gd">Kendin yapmak istersen.</h2></div><p>CV'ni kendin düzeltmek istersen ihtiyacın olan her şey burada; takılırsan yazman yeterli.</p></div>
<div class="cvgs">{gh}</div></div></section>
<section id="sss" class="ksec" aria-labelledby="h-sss"><div class="wrap kfaq">
<div data-rv><span class="eyebrow">Sık sorulanlar</span><h2 id="h-sss">Aklındaki sorular.</h2><p class="muted">Burada yoksa WhatsApp'tan yaz, aynı gün dönelim.</p></div>
{faq_list(CV_FAQ)}</div></section>
{cv_cta()}
'''
    return ("CV Hazırlama Hizmeti: ATS Uyumlu CV ve Ön Yazı | Laurus Dijital",
            "Profesyonel CV hazırlama ve CV oluşturma: ATS uyumlu Türkçe ve İngilizce CV, ilana özel ön yazı, kariyer danışmanlığı. Ücretsiz CV taraması, abonelik yok, tek seferlik ödeme.", body)

# ---------- SEO rehberleri ----------
def _ul(items): return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
def _ol(items): return "<ol>" + "".join(f"<li>{x}</li>" for x in items) + "</ol>"
def _ex(title, txt): return f'<div class="gex"><b>{title}</b><p>{txt}</p></div>'

ROLES = [
 ("satis-temsilcisi","Satış temsilcisi CV örneği",
  "Hedef odaklı satış temsilcisi; 5 yıl boyunca B2B kurumsal müşterilerle çalıştım. Yeni müşteri kazanımı ve mevcut müşteri büyütmede düzenli olarak hedefin üzerinde kapattım.",
  ["Bölgedeki 40 kurumsal müşteriden oluşan portföyü yönettim, yıllık satışı yüzde 18 artırdım.","Soğuk aramayla ayda ortalama 12 yeni görüşme ayarladım; bunların üçte biri sözleşmeye döndü.","CRM kayıtlarını düzenleyerek teklif süresini 3 günden 1 güne indirdim.","Yeni katılan 4 temsilcinin işbaşı eğitimini verdim."],
  "Rakam ver. “Satışları artırdım” yerine “yüzde 18 artırdım” yaz; hangi dönemde, hangi portföyde olduğunu belirt."),
 ("muhasebe","Muhasebe CV örneği",
  "Genel muhasebe ve vergi süreçlerinde 6 yıllık deneyim. Ay sonu kapanışları, beyannameler ve bağımsız denetim hazırlıklarını zamanında ve hatasız yürüttüm.",
  ["Aylık KDV, muhtasar ve SGK bildirgelerini zamanında hazırladım.","Ay sonu kapanış süresini 8 iş gününden 5 iş gününe indirdim.","Bağımsız denetim için mutabakat ve dosya hazırlığını yönettim.","ERP geçişinde hesap planının yeni sisteme aktarılmasında görev aldım."],
  "Kullandığın programları (ERP, ön muhasebe yazılımları) ve sertifikalarını ayrı bir başlıkta yaz; ilanlar en çok bunlarla eşleşir."),
 ("muhendis","Mühendis CV örneği",
  "Üretim ve süreç iyileştirme alanında 4 yıllık deneyime sahip endüstri mühendisi. Veriyle karar alan, sahada çalışmayı seven bir ekip oyuncusu.",
  ["Montaj hattında çevrim süresini yüzde 12 kısaltan yerleşim değişikliğini yürüttüm.","Fire oranını yüzde 4,1'den yüzde 2,6'ya düşüren kalite projesini yönettim.","Haftalık üretim planlamasını tabloya dayalı bir modelle otomatikleştirdim.","3 vardiyada 25 kişilik ekibe iş güvenliği ve 5S eğitimleri verdim."],
  "Projeyi, senin rolünü ve sonucu aynı maddede yaz: ne yaptın, nasıl yaptın, ne değişti."),
 ("ogretmen","Öğretmen CV örneği",
  "8 yıllık deneyime sahip İngilizce öğretmeni. Ortaokul ve lise düzeyinde iletişim odaklı ders tasarımı ve sınav hazırlığında deneyimli.",
  ["Haftalık 24 saat ders yükünü 5 şubede yürüttüm.","Hazırladığım konuşma kulübüyle öğrenci katılımı bir dönemde iki katına çıktı.","Ortak sınav sorularını hazırlayan zümre ekibinde görev aldım.","Velilerle düzenli geri bildirim toplantıları planladım ve yürüttüm."],
  "Branşını, kademeni ve sertifikalarını (pedagojik formasyon, dil sınavı puanı) ilk satırlarda göster."),
 ("yeni-mezun","Yeni mezun CV örneği",
  "İşletme bölümü yeni mezunu. Staj ve kulüp deneyimlerimde etkinlik organizasyonu, sosyal medya ve veri tabloları üzerinde çalıştım; pazarlama alanında kariyerime başlamak istiyorum.",
  ["Üniversite kariyer kulübünde 300 kişilik kariyer gününün organizasyon ekibinde yer aldım.","Stajımda haftalık satış raporlarını hazırlayıp ekip toplantılarında sundum.","Kulübün Instagram hesabını bir yıl yönettim, takipçi sayısını 1.200'den 3.400'e çıkardım.","İleri düzey tablo programı ve temel veri görselleştirme bilgisine sahibim."],
  "İş deneyimin azsa staj, gönüllülük, kulüp ve bitirme projesini deneyim gibi yaz; ne yaptığını ve sonucu belirt."),
]

def cvg_page(slug, kw, h1, lead, read, title, desc, sections, faq, related):
    toc = "".join(f'<li><a href="#{sid}">{t}</a></li>' for sid,t,_ in sections)
    secs = "".join(f'<section id="{sid}" class="gsec">' + (f"<h2>{t}</h2>" if t else "") + f'{b}</section>' for sid,t,b in sections)
    names = {"cv-hazirlama.html":"CV hazırlama hizmeti","cv-ornekleri.html":"CV örnekleri","ats-uyumlu-cv.html":"ATS uyumlu CV","ingilizce-cv.html":"İngilizce CV","on-yazi-ornegi.html":"Ön yazı örnekleri","maas-beklentisi.html":"Maaş beklentisi"}
    rel = "".join(f'<a class="grel" href="{r}">{names.get(r,r)}</a>' for r in related)
    mid = f'<aside class="gnote cvnote"><b>CV\'ni biz hazırlayalım</b><p>ATS uyumlu Türkçe ve İngilizce CV, ilana özel ön yazı ve profil metinleri. Önce ücretsiz okunabilirlik raporunu al, sonra karar ver.</p><a class="btn btn-gold js-wa" href="{WA_CV}">Ücretsiz CV taraması</a></aside>'
    body = f'''
{cine_hero('<a href="cv-hazirlama.html">CV hazırlama</a> / ' + kw, "CV rehberi", h1, lead, ["planlama","tasarim-laptop","kadin-telefon"], f'<a class="btn btn-gold js-wa" href="{WA_CV}">CV\'mi ücretsiz tarat</a><a class="btn btn-line" href="cv-hazirlama.html#paketler">Paketler</a>', "sm", f'<p class="gmeta">Güncelleme: 10 Kasım 2026 · Okuma: {read} · Laurus Dijital</p>')}
<section class="light gbody"><div class="wrap ggrid">
<aside class="gtoc"><b>Bu rehberde</b><ol>{toc}</ol><a class="btn btn-gold js-wa" href="{WA_CV}">Ücretsiz CV taraması</a></aside>
<article class="gart">{secs}{mid}
<section id="sss" class="gsec"><h2>Sık sorulan sorular</h2>{faq_list(faq)}</section>
<div class="grels"><b>İlgili sayfalar</b>{rel}</div></article>
</div></section>
{cv_cta()}
'''
    return (title, desc, body)

def page_cv_examples():
    roles = ""
    for rid,t,summary,bullets,tip in ROLES:
        roles += f'<section id="{rid}" class="gsec"><h2>{t}</h2>{_ex("Profil özeti", summary)}<p><b>Güçlü madde örnekleri</b></p>{_ul(bullets)}<p class="gtip"><b>İpucu:</b> {tip}</p></section>'
    how = _ol(["<b>İletişim bilgileri:</b> ad soyad, telefon, e-posta, şehir. Fotoğraf, doğum yeri ve kimlik numarası gerekmez.",
               "<b>Profil özeti:</b> 2–3 cümlede kim olduğunu, kaç yıllık deneyimin olduğunu ve ne aradığını yaz.",
               "<b>İş deneyimi:</b> en yeniden eskiye; şirket, unvan, tarih ve 3–5 sonuç odaklı madde.",
               "<b>Eğitim:</b> okul, bölüm, mezuniyet yılı. Deneyimin azsa not ortalamasını ve projeni ekle.",
               "<b>Yetenekler:</b> ilandaki kelimelerle eşleşen araçlar, programlar ve beceriler; tablo değil düz liste.",
               "<b>Sertifikalar ve diller:</b> dil seviyesini ve sınav puanını açıkça belirt.",
               "<b>Referanslar:</b> “istenirse verilir” yazmak yeterli; isim ve telefonu ilk başvuruda paylaşmana gerek yok."])
    secs = [("cv-nasil-yazilir","CV nasıl yazılır? Yedi bölüm, bu sırayla", "<p>İyi bir CV'nin sırrı tasarım değil, düzen. İşveren ve başvuru yazılımı aynı sırayı bekler:</p>"+how+"<p>Tek sayfa yeterli. Deneyimin 10 yılı geçiyorsa iki sayfa olabilir; daha fazlası okunmaz.</p>")] + \
           [(rid, None, "") for rid,*_ in []]
    body_secs = secs[:1]
    for rid,t,summary,bullets,tip in ROLES:
        body_secs.append((rid, t, f'{_ex("Profil özeti", summary)}<p><b>Güçlü madde örnekleri</b></p>{_ul(bullets)}<p class="gtip"><b>İpucu:</b> {tip}</p>'))
    body_secs.append(("ingilizce","İngilizce CV örneği",'<p>İngilizce CV başlıkları, güçlü fiiller ve örnek özet için <a href="ingilizce-cv.html">İngilizce CV rehberimize</a> bak.</p>'))
    faq = [("CV'de fotoğraf olmalı mı?","Zorunlu değil. Türkiye'de birçok ilan fotoğraf istemez; koyacaksan sade, güncel ve profesyonel bir vesikalık seç."),
           ("CV kaç sayfa olmalı?","Çoğu başvuru için tek sayfa. Uzun ve üst düzey deneyimlerde iki sayfa olabilir."),
           ("Hazır CV şablonu kullanmak sorun mu?","Tasarımı yoğun şablonlar (iki kolon, tablo, ikon) başvuru yazılımlarında okunmayabilir. Sade, tek kolonlu bir düzen daha güvenlidir.")]
    return cvg_page("cv-ornekleri.html","CV örnekleri","CV örnekleri:|mesleğine göre hazır.",
        "Satış, muhasebe, mühendislik, öğretmenlik ve yeni mezunlar için hazır profil özetleri ve güçlü madde örnekleri. Kopyala, kendine uyarla.","7 dakika",
        "CV Örnekleri 2026: Mesleğe Göre Hazır Özgeçmiş Örnekleri | Laurus",
        "CV örnekleri 2026: satış temsilcisi, muhasebe, mühendis, öğretmen ve yeni mezun için hazır profil özeti ve madde örnekleri. CV nasıl yazılır, adım adım.",
        body_secs, faq, ["cv-hazirlama.html","ats-uyumlu-cv.html","on-yazi-ornegi.html","ingilizce-cv.html"])

def page_cv_ats():
    rules = _ol(["Tek kolonlu düzen kullan; iki kolonlu tasarımlar yanlış sırada okunur.",
                 "Yetenekleri tablo ya da grafik içinde değil, virgülle ayrılmış düz liste olarak yaz.",
                 "Unvanı, iletişim bilgilerini ve başlıkları ikonlarla birleştirme; ikon yazılım için boşluktur.",
                 "Standart başlıklar kullan: “İş deneyimi”, “Eğitim”, “Yetenekler”.",
                 "Tarihleri aynı biçimde yaz: “03/2022 – 08/2025” gibi.",
                 "İlandaki anahtar kelimeleri birebir kullan; “müşteri ilişkileri” arıyorlarsa sen de öyle yaz.",
                 "Üst bilgi ve alt bilgi alanına önemli bilgi koyma; bazı yazılımlar bu alanları okumaz.",
                 "Yaygın yazı tipleri seç; süslü yazı tipleri karakter hatasına yol açabilir.",
                 "Dosyayı ilan Word istemiyorsa metin seçilebilir PDF olarak kaydet; taranmış resim PDF okunmaz.",
                 "Dosya adını düzgün ver: “Ad-Soyad-CV.pdf”."])
    chk = _ul(["PDF'te metni fareyle seçebiliyor musun?","Başlıkların standart mı?","Yetenekler düz liste mi?","Tarihler aynı biçimde mi?","İlandaki 5 temel kelime CV'nde geçiyor mu?","Tek sayfa mı (ya da en fazla iki)?"])
    secs = [("ats-nedir","ATS nedir?","<p>ATS (aday takip sistemi), şirketlerin başvuruları toplayıp sıraladığı yazılımdır. CV'ni okur, bilgileri alanlara ayırır ve ilana ne kadar uyduğuna göre sıralar. İnsan çoğu zaman önce bu listeye bakar.</p><p>Sorun şu: güzel görünen birçok CV bu yazılımda parçalanır. Adın yanlış alana düşer, yeteneklerin hiç görünmez, deneyim tarihleri karışır.</p>"),
            ("neden-eleniyor","CV'm neden eleniyor?","<p>En sık üç neden var: tasarım (tablo, ikon, iki kolon), ilandaki kelimelerle eşleşmeyen ifadeler ve okunamayan dosya biçimi. Üçü de düzeltilebilir.</p>"),
            ("10-kural","ATS uyumlu CV için 10 kural", rules),
            ("kontrol","Göndermeden önce 6 soruluk kontrol", chk + "<p>Hepsine “evet” diyemiyorsan CV'ni bize gönder; ücretsiz raporda hangi alanın okunmadığını satır satır gösterelim.</p>")]
    faq = [("ATS uyumlu CV şablonu nerede bulunur?","Sade, tek kolonlu ve tablo içermeyen her şablon ATS uyumludur. Ücretsiz raporla kendi CV'nin durumunu öğrenebilirsin."),
           ("ATS uyumlu CV PDF mi Word mü olmalı?","İlan özellikle Word istemiyorsa metni seçilebilir PDF yeterlidir. Taranmış (resim) PDF kullanma."),
           ("Canva ile hazırladığım CV ATS uyumlu mu?","Tasarıma bağlı. Kolonlu ve ikonlu şablonlar çoğu zaman okunmaz; metni seçilebilir ve tek kolonluysa sorun azdır.")]
    return cvg_page("ats-uyumlu-cv.html","ATS uyumlu CV","ATS uyumlu CV|nasıl hazırlanır?",
        "Başvuru yazılımlarının okuyabildiği CV için 10 kural ve göndermeden önce 6 soruluk kontrol listesi.","6 dakika",
        "ATS Uyumlu CV Nasıl Hazırlanır? 2026 Kontrol Listesi | Laurus",
        "ATS uyumlu CV nedir, CV neden elenir? Başvuru yazılımlarının okuyabildiği CV için 10 kural, PDF mi Word mü sorusu ve göndermeden önce kontrol listesi.",
        secs, faq, ["cv-hazirlama.html","cv-ornekleri.html","ingilizce-cv.html","on-yazi-ornegi.html"])

def page_cv_en():
    tbl = '<div class="gtbl"><table><thead><tr><th>Türkçe başlık</th><th>İngilizce karşılığı</th></tr></thead><tbody>' + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in [
        ("Kişisel bilgiler","Contact Information"),("Profil özeti","Professional Summary"),("İş deneyimi","Work Experience"),("Eğitim","Education"),
        ("Yetenekler","Skills"),("Sertifikalar","Certifications"),("Yabancı dil","Languages"),("Projeler","Projects"),("Gönüllü çalışmalar","Volunteer Experience"),("Referanslar","References")]) + "</tbody></table></div>"
    verbs = _ul(["<b>Led</b> (yönettim), <b>Managed</b> (sorumluydum), <b>Delivered</b> (teslim ettim)","<b>Increased</b> (artırdım), <b>Reduced</b> (azalttım), <b>Improved</b> (iyileştirdim)","<b>Launched</b> (başlattım), <b>Built</b> (kurdum), <b>Designed</b> (tasarladım)","<b>Negotiated</b> (müzakere ettim), <b>Trained</b> (eğittim), <b>Analyzed</b> (analiz ettim)"])
    secs = [("basliklar","İngilizce CV başlıkları ve karşılıkları", tbl),
            ("fiiller","Güçlü fiillerle başla","<p>İngilizce CV'de her madde geçmiş zaman bir fiille başlar; “I” kullanılmaz. En sık işe yarayanlar:</p>"+verbs),
            ("farklar","Türkçe CV'den farkları", _ul(["Fotoğraf, doğum tarihi ve medeni hal yazılmaz; özellikle yurt dışı başvurularda çıkar.","Tarih biçimi “Mar 2022 – Aug 2025” olur.","Not ortalaması 4'lük sistemde verilir: “GPA: 3.2/4.0”.","Dil seviyesini Avrupa çerçevesiyle yaz: “English – C1 (IELTS 7.0)”."])),
            ("ornek","Örnek profil özeti", _ex("Professional Summary","Results-driven sales specialist with 5 years of B2B experience. Grew a 40-account regional portfolio by 18% in one year and consistently closed above target. Looking to bring consultative selling skills to an international team."))]
    faq = [("İngilizce CV'yi çeviri programıyla yapabilir miyim?","Kelime kelime çeviri çoğu zaman yapay durur ve iş terimleri yanlış çıkar. Başlıkları ve fiilleri bu rehberdeki gibi kullan; emin değilsen kontrol ettir."),
           ("Resume ile CV aynı şey mi?","Amerika'da “resume” kısa iş başvurusu belgesi, “CV” akademik ve uzun özgeçmiştir. Türkiye ve Avrupa'da ikisi de genelde aynı anlamda kullanılır.")]
    return cvg_page("ingilizce-cv.html","İngilizce CV","İngilizce CV|nasıl yazılır?",
        "Başlık karşılıkları, güçlü fiiller, Türkçe CV'den farkları ve örnek profil özeti. Yurt dışı ve yabancı şirket başvuruları için.","6 dakika",
        "İngilizce CV Nasıl Yazılır? Örnek ve Başlık Karşılıkları | Laurus",
        "İngilizce CV hazırlama rehberi: başlıkların İngilizce karşılıkları, güçlü fiiller, tarih ve not biçimi, örnek profil özeti (Professional Summary).",
        secs, faq, ["cv-hazirlama.html","cv-ornekleri.html","ats-uyumlu-cv.html","on-yazi-ornegi.html"])

def page_cv_cover():
    secs = [("yapi","İyi bir ön yazının yapısı", _ol(["<b>Giriş:</b> hangi pozisyona başvurduğunu ve neden bu şirketi seçtiğini bir cümlede söyle.","<b>Kanıt:</b> ilandaki en önemli iki ihtiyaca, kendi deneyiminden birer somut örnekle cevap ver.","<b>Kapanış:</b> görüşme isteğini net ve kısa yaz; teşekkür et."]) + "<p>Toplam 150–250 kelime yeter. Herkese aynı metni göndermek yerine her ilana iki cümleyi değiştirmek bile fark yaratır.</p>"),
            ("deneyimli","Örnek 1: deneyimli aday", _ex("Ön yazı","Merhaba, şirketinizin Satış Uzmanı ilanını büyük bir ilgiyle okudum. Son 5 yılda B2B kurumsal müşterilerle çalıştım ve sorumlu olduğum 40 müşterilik portföyde yıllık satışı yüzde 18 artırdım. İlanda vurguladığınız yeni pazar açma hedefine, bir önceki görevimde iki yeni şehirde kurduğum bayi ağıyla katkı sunabileceğime inanıyorum. Bu deneyimi ekibinize nasıl taşıyabileceğimi bir görüşmede anlatmak isterim. Zaman ayırdığınız için teşekkür ederim.")),
            ("yeni-mezun","Örnek 2: yeni mezun", _ex("Ön yazı","Merhaba, İşletme bölümünden bu yıl mezun oldum ve Pazarlama Asistanı pozisyonunuza başvuruyorum. Stajım boyunca haftalık satış raporları hazırladım, kariyer kulübümüzde 300 kişilik bir etkinliğin organizasyonunda yer aldım ve kulübün Instagram hesabını bir yıl yönettim. Markanızın dijital kanallardaki büyümesine öğrenmeye açık ve çalışkan bir ekip arkadaşı olarak katkı sunmak isterim. Görüşme fırsatı için şimdiden teşekkür ederim.")),
            ("kariyer-degisimi","Örnek 3: kariyer değiştiren aday", _ex("Ön yazı","Merhaba, 6 yıllık öğretmenlik deneyimimin ardından insan kaynakları alanına geçiyorum ve Eğitim ve Gelişim Uzmanı ilanınıza başvuruyorum. Yıllarca farklı yaş gruplarına program tasarladım, ölçme ve değerlendirme yaptım ve velilerle zor görüşmeleri yönettim. Bu sene tamamladığım insan kaynakları sertifika programıyla bu deneyimi kurumsal eğitimlere taşımaya hazırım. Deneyimimin ekibinize nasıl katkı sağlayacağını konuşmak isterim.")),
            ("kisa","İş sitelerindeki kısa ön yazı kutusu", "<p>Birçok başvuru formunda 500 karakterlik bir kutu çıkar. Buraya yukarıdaki yapının kısa hâlini yaz: pozisyon, en güçlü bir kanıt ve görüşme isteği. Üç cümle yeter.</p>"),
            ("hatalar","Sık yapılan hatalar", _ul(["Her ilana aynı metni göndermek.","CV'deki her şeyi tekrar anlatmak.","“Her türlü işe hazırım” gibi hedefsiz ifadeler.","Şirketin ya da yetkilinin adını yanlış yazmak."]))]
    faq = [("Ön yazı zorunlu mu?","Her ilanda değil ama yazıldığında öne geçirir; özellikle kutu boş bırakıldığında bu bir fırsat kaybıdır."),
           ("Ön yazı ile niyet mektubu aynı şey mi?","İş başvurularında evet, aynı anlamda kullanılır. Akademik başvurularda niyet mektubu daha uzun ve kişiseldir.")]
    return cvg_page("on-yazi-ornegi.html","Ön yazı örnekleri","Ön yazı örnekleri:|kopyala, uyarla.",
        "Deneyimli, yeni mezun ve kariyer değiştiren adaylar için üç hazır ön yazı; iş sitelerindeki kısa kutu için de üç cümlelik versiyon.","5 dakika",
        "Ön Yazı Örnekleri 2026: İş Başvurusu İçin Hazır Şablon | Laurus",
        "İş başvurusu ön yazı örnekleri: deneyimli, yeni mezun ve kariyer değiştiren adaylar için hazır şablonlar, ön yazı nasıl yazılır ve sık yapılan hatalar.",
        secs, faq, ["cv-hazirlama.html","maas-beklentisi.html","cv-ornekleri.html","ats-uyumlu-cv.html"])

def page_cv_salary():
    secs = [("arastir","Önce piyasayı araştır", _ul(["Aynı pozisyon için yayımlanan ilanlarda maaş aralığı yazıyorsa not al.","Maaş karşılaştırma sitelerine ve sektör raporlarına bak; şehir, deneyim yılı ve şirket büyüklüğüne göre süz.","Aynı işi yapan tanıdıklarına aralık sor; tek rakam değil, aralık iste."])),
            ("kutu","Formdaki maaş kutusuna ne yazılır?", "<p>Kutu tek rakam istiyorsa araştırdığın aralığın üst yarısından bir rakam yaz. Aralık yazılabiliyorsa alt sınırın, kabul edebileceğin en düşük rakamdan biraz yukarıda olsun. Rakamın <b>net mi brüt mü</b> olduğunu mutlaka belirt; açıklama alanı varsa “net, yan haklar hariç” gibi kısa bir not ekle.</p><p>Kutuyu boş bırakmak ya da “1” yazmak bazı sistemlerde başvurunu filtreye takar.</p>"),
            ("mulakat","Mülakatta nasıl söylenir?", _ex("Örnek cevap","Araştırmalarım ve deneyimim doğrultusunda net 55–65 bin TL aralığını düşünüyorum. Yan haklar ve sorumluluklar netleştiğinde bu konuyu birlikte değerlendirmekten memnuniyet duyarım.") + "<p>Örnekteki rakamlar yalnızca cümle yapısını göstermek içindir; kendi araştırmanla değiştir.</p>"),
            ("yan-haklar","Yan hakları da hesaba kat", _ul(["Yemek, yol ve özel sağlık sigortası","Prim ve ikramiye düzeni","Uzaktan ya da hibrit çalışma","Yıllık izin ve eğitim bütçesi"]) + "<p>Toplam paketi karşılaştır; bazen daha düşük maaş, yan haklarla daha yüksek bir toplam eder.</p>")]
    faq = [("Maaş beklentisi net mi brüt mü yazılır?","Hangisini yazdığını açıkça belirt. Türkiye'de adaylar genelde net konuşur; şirket brüt düşünebilir, karışıklık pazarlıkta sorun çıkarır."),
           ("Maaş beklentisini düşük yazarsam işe alınma şansım artar mı?","Her zaman değil. Çok düşük rakam deneyimsizlik gibi okunabilir; araştırmaya dayalı makul bir aralık daha güven verir.")]
    return cvg_page("maas-beklentisi.html","Maaş beklentisi","Maaş beklentisi|ne yazılmalı?",
        "Başvuru formundaki kutuya ve mülakatta ne yazılır, nasıl söylenir? Araştırma yöntemi, net ve brüt farkı, örnek cevap ve yan haklar.","5 dakika",
        "Maaş Beklentisi Ne Yazılmalı? Formda ve Mülakatta Doğru Cevap | Laurus",
        "Maaş beklentisi ne yazılır? İş başvurusu formundaki maaş kutusu, mülakatta maaş sorusuna örnek cevap, net ve brüt farkı ve yan haklar.",
        secs, faq, ["cv-hazirlama.html","on-yazi-ornegi.html","cv-ornekleri.html","ats-uyumlu-cv.html"])

CV_PAGES = {
  "cv-hazirlama.html": page_cv,
  "cv-ornekleri.html": page_cv_examples,
  "ats-uyumlu-cv.html": page_cv_ats,
  "ingilizce-cv.html": page_cv_en,
  "on-yazi-ornegi.html": page_cv_cover,
  "maas-beklentisi.html": page_cv_salary,
}
CV_NAMES = {"cv-ornekleri.html":"CV örnekleri","ats-uyumlu-cv.html":"ATS uyumlu CV","ingilizce-cv.html":"İngilizce CV","on-yazi-ornegi.html":"Ön yazı örnekleri","maas-beklentisi.html":"Maaş beklentisi"}
for _s,_f in CV_PAGES.items():
    PAGES[_s] = (_f, "cv")
    if _s == "cv-hazirlama.html":
        PAGE_META[_s] = dict(crumb=[("CV hazırlama","/cv-hazirlama")], service=("CV hazırlama ve kariyer danışmanlığı","1290","ATS uyumlu Türkçe ve İngilizce CV, ilana özel ön yazı ve kariyer danışmanlığı."))
    else:
        PAGE_META[_s] = dict(crumb=[("CV hazırlama","/cv-hazirlama"),(CV_NAMES[_s],"/"+_s.replace(".html",""))], article=True)
PT_NAMES.update({"cv-hazirlama":"CV Hazırlama","cv-ornekleri":"CV Örnekleri","ats-uyumlu-cv":"ATS Uyumlu CV","ingilizce-cv":"İngilizce CV","on-yazi-ornegi":"Ön Yazı","maas-beklentisi":"Maaş Beklentisi"})
