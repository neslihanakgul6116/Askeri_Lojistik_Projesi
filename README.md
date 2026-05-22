# Hava Askeri Ussu Lojistik ve Buyuk Veri Analiz Platformu

Bu proje, hava askeri uslerinde envantere giren ve cikan kritik parcalarin loglarini, sunucuyu kilitlemeden arka planda analiz eden asenkron bir buyuk veri mimarisidir.

## Kullanılan Teknolojiler ve Mimari
* Backend: Python / Flask
* Asynchronous Task Queue (Asenkron Is Kuyrugu): Celery
* Message Broker: Redis
* Frontend: Tailwind CSS & Chart.js

## Dagitik Sistem Mimarisi (Neden Celery ve Redis?)
Klasik web mimarilerinde milyonlarca satirlik bir lojistik dosyasi taratilmaya calisildiginda tarayici donar ve hata alinir. 

Bu projede bu sorunu asmak icin asenkron mimari uygulanmistir:
1. Kullanici butona basarak analizi başlatir.
2. Flask, talebi alir almaz is yukunu Redis uzerinden Celery iscisine firlatir ve tarayiciya aninda yanit donerek sistemi acik tutar.
3. Celery arka planda bagimsiz bir islemci gibi dosyayi islerken, on yuz saniyede bir durum sorgusu atarak canli ilerleme cubugunu gunceller.
4. Analiz bitiminde elde edilen kritik stok esik verileri Chart.js ile gorsellestirilir.

## Kurulum ve Calistirma
1. Redis Sunucusunu Baslatin:
   sudo service redis-server start
2. Celery Iscisini Atesleyin:
   celery -A worker.app worker --loglevel=info -P threads
3. Flask Uygulamasini Baslatin:
   python app.py
4. Tarayicidan http://127.0.0.1:5000 adresine gidin.