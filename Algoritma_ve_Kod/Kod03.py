"""
Klavyeden girilen x değerinden yine klavyeden girilen n değerine  (x < n) kadar olan tüm doğal sayıları listeleyen programın algoritmasını yazınız. 
1. Başla
2. x, n Oku
3. x Yaz
4. x = x + 1
5. Eğer x < = n ise x. adıma Git
6. Bitir
"""
 
x = int(input("Başlangıç değeri (x): "))
n = int(input("Bitiş değeri (n): "))

while x <= n:
    print(x)
    x += 1