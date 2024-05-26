import cmath   # cmath, Python'da karmaşık sayılarla çalışmayı sağlayan bir modüldür

# Kullanıcıdan denklemi al
denklem = input("Lütfen ikinci dereceden bir denklem girin (örn: ax^2 + bx + c): ")

# Denklemin katsayılarını ayırma
katsayilar = denklem.split('+')

a = float(katsayilar[0].split('x^2')[0])
b = float(katsayilar[1].split('x')[0])
c = float(katsayilar[2])

# Diskriminantı hesaplar
delta = (b**2) - (4*a*c)

# Kökleri bulur ve ekrana yazdırır.
if delta > 0:
    kok1 = (-b + delta**0.5) / (2*a)
    kok2 = (-b - delta**0.5) / (2*a)
    print("Kök 1:", kok1)
    print("Kök 2:", kok2)
elif delta == 0:
    kok = -b / (2*a)
    print("Kök 1 ve Kök 2:", kok)
else:
    kok1 = (-b + cmath.sqrt(delta)) / (2*a)
    kok2 = (-b - cmath.sqrt(delta)) / (2*a)
    print("Kök 1:", kok1)
    print("Kök 2:", kok2)
