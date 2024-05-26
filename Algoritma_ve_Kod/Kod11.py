"""
Genel gösterimi Xn = n2 şeklinde olan bir dizinin n. elemanına kadar olan tüm elemanlarını ekranda listeleyen programın algoritmasını yazınız. 
1. Başla
2. n Oku
3. X = 1
4. X * X Yaz
5. X = X+1
6. Eğer X < = n ise x. adıma Git
7. Bitir
"""

# Kullanıcıdan n değerini al
n = int(input("n değeri: "))

# Sayıyı başlat
X = 1

# Diziyi ekrana yazdır
while X <= n:
    print(X * X)
    X += 1
