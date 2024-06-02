from __future__ import division

secenek1 = "Toplam (1)"
secenek2 = "Çıkarma (2)"
secenek3 = "Çarpma (3)"
secenek4 = "Bölme (4)"

print(secenek1, "\n",secenek2, "\n",secenek3, "\n",secenek4)

soru = int(input("Yapılacak işlemin numarasını girin: "))

if soru == "1":
    sayi1 = int(input("İlk sayıyı giriniz: "))
    print(sayi1)
    sayi2 = int(input("ikinici sayıyı giriniz"))
    print(sayi1, "+", sayi2, "=" )