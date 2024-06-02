# PyhonSoruCozum

 # -- Python örnek sorular ve çözümler 



# Python İle Amiral Battı Oyunu

Bu proje, Python programlama dili kullanılarak basit bir Amiral Battı oyununun nasıl oluşturulacağını göstermektedir. Oyunun amacı, düşman gemilerini bulmak ve batırmaktır.

## Oyun Kuralları

- Oyun 5x5 bir tahtada oynanır.
- Toplamda 3 düşman gemisi vardır ve bu gemiler rastgele konumlandırılır.
- Oyuncu, gemileri bulmaya çalışır ve her doğru tahminde puan kazanır.
- Her yanlış tahminde puan kaybedilir.
- Oyuncu 3 düşman gemisini de batırdığında oyunu kazanır.

## Nasıl Oynanır

1. Oyun başladığında, 5x5 bir tahtada başlarsınız ve puanınız 300 olarak başlar.
2. Rastgele konumlandırılan 3 düşman gemisini bulmaya çalışırsınız.
3. Her turda, satır ve sütun koordinatlarını girmeniz istenir.
4. Eğer doğru tahmin yaparsanız, gemiyi batırmış olursunuz ve puan kazanırsınız.
5. Eğer yanlış tahmin yaparsanız, puan kaybedersiniz.
6. Oyunu kazanmak için 3 düşman gemisini de batırmalısınız.

## Kod Açıklaması

Bu proje, Python programlama dili kullanılarak geliştirilmiştir. Projenin ana bileşenleri şunlardır:

- Koşullar (if-elif-else) ve döngüler (while) kullanılarak oyun mantığı oluşturulmuştur.
- Fonksiyonlar kullanılarak kodun daha okunaklı ve modüler hale getirilmiştir.
- Veri yapıları (liste) oyun tahtasını temsil etmek için kullanılmıştır.
- Nesne Yönelimli Programlama (OOP) ilkesine uygun bir şekilde oyun tasarlanmıştır.

## Nasıl Çalıştırılır

Oyunu yerel bir Python ortamında veya Python IDE'sinde çalıştırabilirsiniz. Önce Python'u bilgisayarınıza yüklemeniz gerekebilir.

```bash
python amiral_batti.py
