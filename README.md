# ETKINLIKPASS
EtkinlikPass, kullanıcıların aldıkları konser biletlerini satmak için ilan oluşturabilecekleri, anlık olarak mesajlaşabilecekleri bir website projesidir. Etkinlikler API aracılığıyla dinamik olarak güncellenmektedir. İllegal satışları önlemek adına şikayet sistemi eklenmiştir ve ileri süreçte bilet fiyatlarını dinamik olarak çekerek maksimum fiyat belirlenmesi araştırılmaktadır.

# BAŞLARKEN

## Ön Koşullar

Bilgisayarınızda güncel Python sürümü kurulu olmalıdır. 
[Python indir](https://www.python.org/downloads/)

Redis kurulu olmalıdır.
### Linux için
[Install Redis on Linux](https://redis.io/docs/install/install-redis/install-redis-on-linux/)

### Windows için
[Redis for Windows](https://github.com/tporadowski/redis/releases)

## Kurulum

Gerekli paketleri kurmak için requirements.txt dosyasında yazan paketler kurulur:
```pip install -r requirements.txt``` 

## Kullanım

Website aşağıdaki komut ile default olarak http://localhost:8000/ adresinde çalışmaya başlar:
```python manage.py runserver```

Chat sunucusunu çalıştırmak için aşağıdakı adımlar izlenir:
### Redis'i çalıştır
Linux için:
```redis-server``` komut kullanılarak sunucu başlatılır.
Sunucunun çalıştığından emin olmak için ```redis-cli ping``` komutunu çalıştırabilirsiniz. Eğer düzgün başlatılmışsa 'PONG' şeklinde bir cevap dönecektir.

Windows için:
Redis for Windows reposundaki güncel sürüm yüklendikten sonra kurulu olan klasörden ```redis-server.exe``` dosyası çalıştırılır.
Sunucunun çalıştığından emin olmak için Redis'in kurulu olan klasörden ```redis-cli.exe``` dosyasını çalıştırarak ```ping``` komutunu kullanabilirsiniz. Her şey doğruysa 'PONG' şeklinde bir cevap dönecektir.

### Uvicorn'u başlat
```uvicorn core.asgi:application --host localhost --port 8001``` komutu kullanılarak 8001 portunda socket başlatılır.

Bütün sunucuları çalıştırdıktan sonra website http://localhost:8000/ adresinde çalışmaya başlar.

## Teşekkürler
Tüm Türkiye üzerindeki etkinlikleri API aracılığıyla sunan [etkinlik.io](https://etkinlik.io/) ekibine teşekkürlerimizi sunarız.
