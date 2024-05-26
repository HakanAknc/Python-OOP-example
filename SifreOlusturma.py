import random
import string

def sifre_olustur():
    # Kullanıcıdan kriterleri al
    buyuk_harf_sayisi = int(input("Büyük harf sayısı: "))
    kucuk_harf_sayisi = int(input("Küçük harf sayısı: "))
    rakam_sayisi = int(input("Rakam sayısı: "))
    ozel_sembol_sayisi = int(input("Özel sembol sayısı: "))

    # Kullanıcıdan istenen sayılar ve semboller
    buyuk_harfler = string.ascii_uppercase
    kucuk_harfler = string.ascii_lowercase
    rakamlar = string.digits
    ozel_semboller = string.punctuation

    # Şifre bileşenlerini içeren listeler
    buyuk_harfler_liste = [random.choice(buyuk_harfler) for _ in range(buyuk_harf_sayisi)]
    kucuk_harfler_liste = [random.choice(kucuk_harfler) for _ in range(kucuk_harf_sayisi)]
    rakamlar_liste = [random.choice(rakamlar) for _ in range(rakam_sayisi)]
    ozel_semboller_liste = [random.choice(ozel_semboller) for _ in range(ozel_sembol_sayisi)]

    # Tüm bileşenleri birleştirerek şifreyi oluştur
    sifre = buyuk_harfler_liste + kucuk_harfler_liste + rakamlar_liste + ozel_semboller_liste

    # Şifreyi karıştır
    random.shuffle(sifre)

    # Şifreyi ekrana yazdır
    print("Oluşturulan Şifre: " + "".join(sifre))

# Şifre oluşturma fonksiyonunu çağır
sifre_olustur()
