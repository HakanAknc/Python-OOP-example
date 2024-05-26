# 5. Kullanıcıdan üç farklı sayı alan ve bu sayıları büyükten küçüğe sıralayarak ekrana yazdıran bir program yazın.

sayi1 = float(input("1.sayıyı giriniz: "))
sayi2 = float(input("2.sayıyı giriniz: "))
sayi3 = float(input("3.sayıyı giriniz: "))

en_buyuk = max(sayi1,sayi2,sayi3)
en_kucuk = min(sayi1,sayi2,sayi3)
ortancaa = ((sayi1+sayi2+sayi3) - en_buyuk - en_kucuk)


print(f"Sıralama (büyükten küçüğe) : {en_buyuk} > {ortancaa} > {en_kucuk}")
