"""
Girilen bir sayının asal olup olmadığını bulunuz.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir. 
"""
sayi = int(input("Sayı : "))
asalMi = True

for i in range(2, sayi):
    if(sayi % i == 0):
        break

if asalMi:
    print("Sayı asaldır.")
else:
    print("Sayı asal değildir.")