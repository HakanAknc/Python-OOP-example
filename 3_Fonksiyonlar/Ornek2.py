# def yazdir(kelime,adet):
#     return kelime * adet

# print(yazdir("hakan\n",5))


"""
2- Gönderilen 2 sayı arasındaki tüm asal sayıları bulan python fonksiyon uygulamasını yapınız.
"""

def asalBulma(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1): # sondaki sayıyı almıyor +1 diyerek sondaki sayıyı da aldırdık
        if sayi > 1:
            for i in range(2,sayi):
                if sayi % i == 0:
                    break
            else:
                print(sayi)

sayi1 = int(input("sayi1 : "))
sayi2 = int(input("sayi2 : "))

asalBulma(sayi1,sayi2)



