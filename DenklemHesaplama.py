# İkinci dereceden denklem hesaplama

import math

a = int(input("a değerini giriniz: "))
b = int(input("b değerini giriniz: "))
c = int(input("c değerini giriniz: "))

delta = b**2-4*a*c
print("Delta: ",delta)

if delta > 0:
    print("Denklemin iki farklı kökü vardır.")
    x1 = (-b - math.sqrt(delta))/2*a
    x2 = (-b + math.sqrt(delta))/2*a
    print("x1: ",x1)
    print("x2: ",x2)
elif delta == 0:
    print("Denklemin aynı iki kökü vardır.")
    x1 = (-b/2*a)
    print("x1=x2: ",x1)
else:
    print("Denklemin kökü yoktur")