# 7. Bilgisayarın 1 ile 100 arası rastgele bir sayı seçtiği, kullanıcının bu sayıyı tahmin etmeye 
# çalıştığı bir oyun yazın. 5 tahmin içinde bilemezse “bilemediniz” yazdırsın. Eğer 5 
# tahmin içinde bilebilirse tutulan sayıyı ve tahmin sayısını ekrana yazdıran program. Not: 
# Kullanıcı sayıyı bilemediğinde, daha büyük ya da daha küçük sayı girmesini istemelidir

import random

tutulan_sayi = random.randint(1, 100)

for sayi_tahmini in range(1, 6):
    tahmin = int(input("1 ile 100 arasında bir sayı giriniz: "))

    if tahmin == tutulan_sayi:
        print(f"Tebrikler nokta atışı bir tahmin :) tutulan sayı: {tutulan_sayi} tahmin sayınız: {sayi_tahmini} ")
        break
    elif sayi_tahmini == 5:
        print(f"Bilemediniz. Tutulan sayı: {tutulan_sayi}")
    elif tahmin < tutulan_sayi:
        print("Daha büyük bir sayı giriniz.")
    else:
        print("Daha küçük bir sayı giriniz.")