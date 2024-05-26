"""
h metre yükseklikten bırakılan bir top önceki yüksekliğinin %60’ı kadar zıplamaktadır. Bu topun n. zıplaması sonrası yerden yüksekliğinin ne kadar olacağına bulan programın algoritmasını yazınız. 
1. Başla
2. h, n Oku
3. s = 0
4. s = s + 1
5. h = h * 60 / 100
6. Eğer s < n ise x. adıma Git 
7. h Yaz
8. Bitir
"""

# Kullanıcıdan h (yükseklik) ve n (zıplama sayısı) değerlerini al
h = float(input("Yükseklik (metre): "))
n = int(input("Zıplama sayısı: "))

# Sayacı başlat
s = 0

# Topun zıplamalarını hesapla
while s < n:
    s += 1
    h = h * 60 / 100

# Yeni yüksekliği ekrana yazdır
print(f"Son yükseklik: {h} metre")
