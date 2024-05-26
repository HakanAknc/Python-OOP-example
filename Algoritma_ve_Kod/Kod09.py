"""
Klavyeden girilen A ve B gibi iki değerin yerlerini değiştirerek ekrana yazdıran programın algoritmasını yazınız. 
1. Başla
2. A, B Oku
3. Depo = 0
4. Depo = A
5. A = B
6. B = Depo
7. A, B Yaz
8. Bitir
"""

# Kullanıcıdan A ve B değerlerini al
A = input("A değeri: ")
B = input("B değeri: ")

# Geçici değişken (Depo) kullanarak A ve B'nin yerlerini değiştir
Depo = A
A = B
B = Depo

# Yeni A ve B değerlerini ekrana yazdır
print("Yeni A:", A)
print("Yeni B:", B)
