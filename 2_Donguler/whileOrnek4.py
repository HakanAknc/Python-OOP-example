# Boş bir öğrenci not defteri oluşturalım
not_defteri = {}

while True:
    print("Not Defteri Uygulaması")
    print("1. Not Ekle")
    print("2. Notları Listele")
    print("3. Not Düzenle")
    print("4. Not Sil")
    print("5. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5): ")

    if secim == '5':
        print("Not defteri uygulamasından çıkılıyor.")
        break

    if secim not in ['1', '2', '3', '4']:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
        continue

    if secim == '1':
        ogrenci_adi = input("Öğrenci adını girin: ")
        notu = float(input("Öğrenci notunu girin: "))
        if ogrenci_adi in not_defteri:
            print(f"{ogrenci_adi} zaten not defterinde var. Not güncellendi.")
        not_defteri[ogrenci_adi] = notu

    elif secim == '2':
        if not not_defteri:
            print("Not defteri boş.")
        else:
            print("Öğrenci Notları:")
            for ogrenci, notu in not_defteri.items():
                print(f"{ogrenci}: {notu}")

    elif secim == '3':
        ogrenci_adi = input("Düzenlemek istediğiniz öğrenci adını girin: ")
        if ogrenci_adi in not_defteri:
            yeni_not = float(input(f"Yeni notu girin ({ogrenci_adi}): "))
            not_defteri[ogrenci_adi] = yeni_not
            print(f"{ogrenci_adi} notu güncellendi.")
        else:
            print(f"{ogrenci_adi} not defterinde bulunamadı.")

    elif secim == '4':
        ogrenci_adi = input("Silmek istediğiniz öğrenci adını girin: ")
        if ogrenci_adi in not_defteri:
            del not_defteri[ogrenci_adi]
            print(f"{ogrenci_adi} not defterinden silindi.")
        else:
            print(f"{ogrenci_adi} not defterinde bulunamadı.")
