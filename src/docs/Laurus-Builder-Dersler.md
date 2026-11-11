# Laurus Builder: Dersler Defteri

Her işin sonunda buraya en fazla üç satır eklenir: ne oldu, neden oldu, bundan sonra ne yapılacak.
Aynı ders ikinci kez yazılıyorsa satır eklenmez; skill'in "Kalıcı kurallar" bölümüne taşınması önerilir.

## 10 Kasım 2026
- Yuvarlak çerçeveli ok düğmeleri "yapay" bulundu; yerine konan "KEŞFET →" etiketi de hiç beğenilmedi. Kartlarda ok ve etiket yok: kartın tamamı tıklanır, üstüne gelince başlık altına döner ve altta altın çizgi uzar.
- Bir kusuru düzeltirken ikinci bir şeyi (görsel karartma) abartıp yeni kusur üretildi. Düzeltme, şikâyet edilen şeyle sınırlı tutulur; yan değişiklik ayrı gösterilir.
- Küçük, kalabalık 3D cihazlar "dandik" bulundu. Az sayıda, büyük, ayrıntılı cihaz: metal çerçeve, kenardan kenara cam, kamera adası, arka kamera, cam yansıması. Marka logosu yok.
- Sayfa açılışında fotoğraftan 3D'ye geçiş "bir anda değişti" diye fark edildi. 3D sahnesi olan girişte ilk karede koyu zemin gösterilir; fotoğraf yalnızca WebGL yoksa görünür.
- Ajans ve Kariyer menüleri farklı görününce rahatsız etti. Bir tarafta yapılan gezinme değişikliği aynı turda diğer tarafa da uygulanır.
- Kısa ekranda (yükseklik 760 px altı) 3D sahne menünün altına taştı. Her 3D sahne 1440×900, 1511×757, 1366×650, 1024×768 ve 390×844'te ayrı ayrı görülmeden teslim edilmez.
- Görsel üstündeki yazı, görselin kendi yazısıyla çakıştı (Uygulamalar kartı). Yazı taşıyan görsel üstüne metin konuyorsa görsel karartılır ve alt gölge güçlendirilir.
- Fiyatlar üç kez indirildi (1.290 → 790 → 250). Fiyat önerirken pazarın alt bandı da gösterilir, karar Defne'nindir.
- Canlıya gönderme, Defne açıkça "canlıya al" yazmadan yapılamıyor; önizleme dalına gönderilir ve link mesajda verilir.
- Tarama betiğinde olmayan bir adres (/uygulamalar) denendi; sayfa adları sitemap.xml'den okunur, ezberden yazılmaz.

## 11 Kasım 2026 — CV Analizi aracı ve canlı tarama
- Tarayıcıda çalışan araç (cvscan.js) onaylandı: dosya sunucuya gitmez, pdf.js yalnız dosya seçilince yüklenir. İyi, kötü, taranmış ve docx örnek dosyalarıyla puan ayarı yapılmadan teslim edilmez.
- Cloudflare e-posta gizleme, sayfadaki her e-postayı `/cdn-cgi/l/email-protection` bağlantısına çeviriyor; Google bunu 404 sayıyor. E-posta geçen her yer `<!--email_off-->` ile sarılır, robots.txt `/cdn-cgi/` yolunu kapatır.
- Başlık uzunluğu derlemeden sonra ölçülür (62 karakter üstü kalmaz); kaynak koddaki başlığa bakmak yetmez, META_FIX/TITLE_FIX son sözü söyler.
