print("********    Hesap Makinesi   *********")
print("/*/*/*/*     Hoşgeldiniz     /*/*/*/*")

secim = input("""
            İşlemler:
              1-) Toplama
              2-) Çıkarma
              3-) Çarpama
              4-) Bölme
              5-) Üs alma
              6-) Karekök bulma
              7-) Mod alma
            Yapmak istediğiniz işlemi seçiniz (1/2/3/4/5/6/7): """)

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    sonuc = sayi1 + sayi2
    print(f"{sayi1} + {sayi2} = {sonuc}")
elif secim == '2':
    sonuc = sayi1 - sayi2
    print(f"{sayi1} - {sayi2} = {sonuc}")
elif secim == '3':
    sonuc = sayi1 * sayi2
    print(f"{sayi1} * {sayi2} = {sonuc}")
elif secim == '4':
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print(f"{sayi1} / {sayi2} = {sonuc}")
    else:
        print("Bir sayıyı 0'a bölemezsiniz.")
elif secim == '5':
    sonuc = sayi1 ** sayi2
    print(f"{sayi1} üzeri {sayi2} = {sonuc}")
elif secim == '6':
    if sayi1 >= 0:
        sonuc = sayi1 ** 0.5
        print(f"{sayi1}'in karekökü = {sonuc}")
    else:
        print("Negatif sayıların karekökü bulunamaz.")
elif secim == '7':
    sonuc = sayi1 % sayi2
    print(f"{sayi1} mod {sayi2} = {sonuc}")
else:
    print("Geçersiz seçim. Lütfen 1, 2, 3, 4, 5, 6 veya 7 seçin.")