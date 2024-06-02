# Python İle Sayı Tahmin Oyunu

import random 
import time

print("Sayı tahmin oyununa hoşgeldiniz :) 1-100 arasında sayı tahmin ediniz.")
sayi = random.randint(1,100)
tahmin_hakki = 5

while True:
    tahmin = int(input("Tahmininiz: "))

    if tahmin == sayi:
        print("Sayı sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler! doğru bildiniz.")

    elif tahmin > sayi:
        print("Sayı sorgulanıyor...")
        time.sleep(1)
        tahmin_hakki -= 1
        print("Daha küçük bir sayı giriniz.")
        print("Kalan tahmin hakkı : ", tahmin_hakki)
    
    else:
        print("Sayı sorgulanıyor...")
        time.sleep(1)
        tahmin_hakki -= 1
        print("Daha büyük bir sayı giriniz.")
        print("Kalan tahmin hakkı : ", tahmin_hakki)

    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitmiştir.")
        print("Bilgisiyarın tahmini : ",sayi)
        break

