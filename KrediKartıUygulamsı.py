# kredi kartı kontrolü gerçek mi? değil mi?

# 5487 9330 4653 6630

# Çözüm1
"""
kart_numarasi = "5487 9330 4653 6630"
kart_numarasi = kart_numarasi.replace(" ", "")  # Boşlukları kaldır

toplam = 0

for i in range(len(kart_numarasi)):
    basamak = int(kart_numarasi[i])

    if i % 2 == 0:
        basamak *= 2
        if basamak > 9:
            basamak = basamak - 9

    toplam += basamak

if toplam % 10 == 0:
    print("Geçerli kredi kartı numarası.")
else:
    print("Geçersiz kredi kartı numarası.")

"""


kart_no = [4,4,0,2,4,7,0,0,0,8,9,5,0,6,6,0]   #Verilen kredi kartı numarasını temsil eden bir liste.

toplam = 0  # Kredi kartı numarasının geçerliliğini kontrol etmek için bir toplam değişkeni.

for i in range(len(kart_no)):   # Kart numarasındaki her basamak üzerinde bir döngü başlatılır.
    basamak = kart_no[i]  # Her döngü adımında, o anki basamağın değeri alınır.

    if i % 2 == 0:  # Her döngü adımında, o anki basamağın değeri alınır.
        basamak *= 2
        if basamak > 9:  # Eğer çarpım sonucu 9'dan büyükse:
            basamak = basamak - 9  # Çıkarma işlemi yapılır. Bu, sonucun tek basamaklı olmasını sağlar.

    toplam += basamak   # Elde edilen basamak değeri toplama eklenir.

if toplam % 10 == 0:   # Toplamın 10'a bölümünden kalan kontrol edilir.
    print("Geçerli kredi kartı numarası.")
else:
    print("Geçersiz kredi kartı numarası.")

#Eğer kalan 0 ise: Bu durumda kredi kartı numarası geçerlidir ve ekrana "Geçerli kredi kartı numarası." yazdırılır.
#Değilse: Kredi kartı numarası geçersizdir ve ekrana "Geçersiz kredi kartı numarası." yazdırılır.