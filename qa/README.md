# Laurus Dijital canlı site testi

Çalıştırma: `node qa/qa.mjs` (Playwright gerekir). İsteğe bağlı: `QA_BASE`, `QA_OUT`.

Kontroller (23 sayfa × telefon 390px + masaüstü 1440px):
- HTTP durum, JS/konsol hataları, 4xx/5xx istekler
- Yatay taşma, sağdan taşan öğeler, kesilen yazı, kırık görsel, eksik alt
- Sayfa başına tek H1, canonical, başlık/açıklama
- İç link (4xx) ve dış link kontrolü
- İletişim formu → WhatsApp mesajı

Çıktı: `problem rows 0`, `internal bad links []`, `form whatsapp ok: true` olmalı.
Instagram 429 yanıtı bot sınırlamasıdır, hata sayılmaz.
