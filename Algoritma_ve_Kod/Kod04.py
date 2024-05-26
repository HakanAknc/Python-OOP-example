"""
Klavyeden girilen A ve B gibi iki sayıyı çarpma işlemi kullanmadan çarpıp sonucu ekrana yazan programın algoritmasını yazınız. 
1. Başla
2. A, B Oku
3. Sayac = 0, Toplam = 0
4. Toplam = Toplam + A
5. Sayac = Sayac + 1
6. Eğer Sayac < B ise x. adıma Git
7. Toplam Yaz
8. Bitir
"""

A = int(input("A değeri: "))
B = int(input("B değeri: "))

Sayac = 0
Toplam = 0

while Sayac < B:
    Toplam += A
    Sayac += 1

print("Çarpım sonucu: ",Toplam)