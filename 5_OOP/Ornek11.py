class Kitap:
    def __init__(self, kitap_adı, yazar, yayınevi, yayın_tarihi):
        self.kitap_adı = kitap_adı
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.yayın_tarihi = yayın_tarihi

    def __str__(self):
        return f"{self.kitap_adı} - {self.yazar}"

class Kütüphane:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"{kitap.kitap_adı} kütüphaneye eklendi.")

    def kitap_sil(self, kitap):
        if kitap in self.kitaplar:
            self.kitaplar.remove(kitap)
            print(f"{kitap.kitap_adı} kütüphaneden silindi.")
        else:
            print(f"{kitap.kitap_adı} kütüphanede bulunamadı.")

    def kitapları_listele(self):
        print("Kütüphane Kitapları:")
        for kitap in self.kitaplar:
            print(kitap)
# Kitap nesneleri oluşturalım
kitap1 = Kitap("Python Programlama", "Guido van Rossum", "ABC Yayınevi", "2020")
kitap2 = Kitap("Veri Bilimi İçin Python", "Jake VanderPlas", "XYZ Yayınevi", "2019")
kitap3 = Kitap("Algoritma ve Veri Yapıları", "John Smith", "123 Yayınevi", "2018")

# Kütüphane nesnesi oluşturalım
kütüphane = Kütüphane()

# Kitapları kütüphaneye ekleyelim
kütüphane.kitap_ekle(kitap1)
kütüphane.kitap_ekle(kitap2)

# Kitapları listeleme
kütüphane.kitapları_listele()

