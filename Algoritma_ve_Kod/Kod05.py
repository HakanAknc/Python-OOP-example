"""
Klavyeden girilen bir sayının tüm tam bölenlerini bulup ekranda listeleyen programın algoritmasını yazınız. 
1. Başla
2. A Oku
3. Say = 1
4. Eğer A MOD Say = 0 ise x. adıma Git
5. 7. adıma Git
6. Say Yaz
7. Say = Say + 1
8. Eğer Say < = A ise x. adıma Git
9. Bitir
"""

# Kullanıcıdan A değerini al
A = int(input("A değeri: "))

# Sayacı başlat
Say = 1

# Tam bölenleri bul ve ekrana yazdır
while Say <= A:
    if A % Say == 0:
        print(Say)
    Say += 1