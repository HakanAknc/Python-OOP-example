# class Calisan:
#     person_sayisi = 0
#     def __init__(self,isim,maas):
#         self.isim = isim
#         self.maas = maas
#         Calisan.person_sayisi += 1

# print(Calisan.person_sayisi)
# calisan1 = Calisan("Hakan", 7850)
# print(Calisan.person_sayisi)
# calisan2 = Calisan("Mehmet", 4590)
# print(Calisan.person_sayisi



class Araba:
    yakit_tipi = "Benzin"

    def __init__(self,marka,model):
        self.marka = marka
        self.model = model

print(Araba.yakit_tipi)

araba1 = Araba("Toyoto","Corolla")
araba2 = Araba("Honda","Civic")

print(araba1.marka,araba1.model)
print(araba2.marka,araba2.model)