"""
Klavyeden girilen bir n değeri için Fibonacci dizisinin terimlerini ekranda görüntüleyen programın algoritmasını yazınız. 
1. Başla
2. n Oku
3. i=3
4. A = 1, B = 1
5. A, B Yaz
6. C=A+B 
7. C Yaz
8. A = B
9. B = C
10. i=i+1
11. Eğer i <= n ise x. adıma Git
12. Bitir
"""

# Kullanıcıdan n değerini al
n = int(input("n değeri: "))

# Sayacı başlat
i = 3

# Başlangıç terimlerini başlat
A, B = 1, 1

# İlk iki terimi ekrana yazdır
print(A)
print(B)

# Fibonacci dizisinin geri kalanını hesapla ve ekrana yazdır
while i <= n:
    C = A + B
    print(C)
    
    A, B = B, C
    i += 1
