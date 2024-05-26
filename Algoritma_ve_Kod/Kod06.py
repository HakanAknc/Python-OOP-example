"""
Klavyeden girilecek n adet sayının tek olanlarını ayrı çift olanlarını ayrı ayrı toplayıp sonuçları ekrana yazan programın algoritmasını yazınız. 
1. Başla
2. n Oku
3. i = 0, tekToplam = 0, ciftToplam = 0
4. Sayi Oku
5. i = i + 1
6. Eğer Sayi MOD 2 = 0 ise x. adıma Git
7. tekToplam = tekToplam + Sayi
8. 10. adıma Git
9. ciftToplam = ciftToplam + Sayi
10. Eğer i < n ise x. adıma Git
11. tekToplam, ciftToplam Yaz
12. Bitir
"""

# Kullanıcıdan n değerini al
n = int(input("Kaç adet sayı gireceksiniz? "))

# Sayacı ve toplamları başlat
i = 0
tekToplam = 0
ciftToplam = 0

# n adet sayı al ve tek/cift toplamları hesapla
while i < n:
    Sayi = int(input("Sayı girin: "))
    i += 1
    if Sayi % 2 == 0:
        ciftToplam += Sayi
    else:
        tekToplam += Sayi

# Toplamları ekrana yazdır
print("Tek Toplam:", tekToplam)
print("Çift Toplam:", ciftToplam)