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
<p>Ekibimizde tasarım, yazılım, içerik ve reklam yönetimi tarafları birlikte çalışır. Bir işletmenin <b>web sitesini</b>, <b>Instagram ve sosyal medya hesaplarını</b>, <b>Google Ads ve Meta reklamlarını</b> ve <b>Google İşletme Profili ile SEO çalışmasını</b> aynı masada planlarız. Böylece sitedeki mesaj, Instagram'daki görsel dil ve Google'daki reklam birbirini tamamlar.</p>
<p>İstanbul'dan Türkiye genelinde online hizmet veriyoruz. Kuaförden otele, klinikten hukuk bürosuna kadar müşterisini internetten bulan her işletmeyle çalışıyoruz.</p>
</div></div></section>

<section class="ksec" aria-labelledby="h-deg"><div class="wrap">
<div class="khead" data-rv><div><span class="eyebrow">Nasıl çalışırız</span><h2 id="h-deg">Bizi tercih edenlerin dört nedeni.</h2></div></div>
<div class="ab-vals">{vh}</div>
</div></section>

<section class="light ksec" aria-labelledby="h-ne"><div class="wrap ab-grid">
<div data-rv><span class="eyebrow">Hizmetlerimiz</span><h2 id="h-ne">Dijital ajans hizmetleri, tek yerden.</h2></div>
<div class="ab-tx" data-rv>
<p>Kurumsal web sitesi ve e-ticaret sitesi tasarımı, sosyal medya yönetimi ve Instagram hesap yönetimi, Google Ads ve Instagram reklam yönetimi, yerel SEO ve Google İşletme Profili kurulumu. İhtiyacın olan tek bir hizmetle başlayabilir, işin büyüdükçe diğerlerini ekleyebilirsin.</p>
<div class="ab-links"><div><b>Hizmetler</b><ul>{svc_links}</ul></div><div><b>Sektörler</b><ul>{sec_links}</ul></div></div>
</div></div></section>
{contact()}
'''
    return ("Hakkımızda | Laurus Dijital, İstanbul Dijital Ajans",
            "Laurus Dijital, 8 yılı aşkın dijital ve teknoloji deneyimine sahip ekibiyle web tasarım, sosyal medya yönetimi, Google Ads ve SEO hizmeti veren İstanbul merkezli dijital ajans.", body)
