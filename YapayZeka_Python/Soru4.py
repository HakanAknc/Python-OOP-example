# 4. Kullanıcıdan bir metin alarak, bu metinde kaç harf, kaç rakam ve kaç boşluk karakteri 
# olduğunu gösteren bir program yazın. python kodunu yazar mısın

metin = input("Bir metin giriniz:")

harf_sayisi = 0
rakam_sayisi = 0
bosluk_sayisi = 0

# Metindeki her karekteri kontrol ediyorum.
for karekter in metin:
    if karekter.isalpha():    # Harf kontrolü
        harf_sayisi += 1
    elif karekter.isdigit():  # Rakam kontrolü
        rakam_sayisi += 1
    elif karekter.isspace():  # Boşluk kontrolü
        bosluk_sayisi += 1

print("Metindeki harf sayısı: ",harf_sayisi)
print("Metindeki rakam sayısı: ",rakam_sayisi)
print("Metindeki boşluk sayısı: ",bosluk_sayisi)


# Fonksiyon ile çözümü
"""
def karakter_analizi(metin):
    harf_sayisi = 0
    rakam_sayisi = 0
    bosluk_sayisi = 0

    for karakter in metin:
        if karakter.isalpha():
            harf_sayisi += 1
        elif karakter.isdigit():
            rakam_sayisi += 1
        elif karakter.isspace():
            bosluk_sayisi += 1

    print(f"Metinde {harf_sayisi} harf, {rakam_sayisi} rakam ve {bosluk_sayisi} boşluk karakteri bulunmaktadır.")

# Kullanıcıdan metin al
kullanici_metni = input("Lütfen bir metin girin: ")

# Karakter analizini gerçekleştir
karakter_analizi(kullanici_metni)
"""