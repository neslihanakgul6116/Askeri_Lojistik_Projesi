# Hava Askeri Üssü Lojistik Analiz Merkezi

Büyük veri dosyalarını arka planda işleyen, canlı ilerleme çubuğu sunan asenkron lojistik analiz platformu.

## Özellikler

- Asenkron büyük veri analizi (Celery + Redis)
- Canlı progress bar (polling)
- Dinamik parça tablosu
- Parça ekle / sil
- 5 saniyede bir otomatik stok güncelleme
- Kritik stok seviyesi alarmı (kırmızı/yeşil)
- Tailwind CSS + Chart.js arayüz

## Teknolojiler

- Python / Flask
- Celery + Redis
- HTML / JavaScript
- Tailwind CSS
- Chart.js

## Kurulum

```bash
pip install flask flask-socketio flask-cors celery redis eventlet
redis-server
celery -A worker.app worker --loglevel=info -P threads
python app.py