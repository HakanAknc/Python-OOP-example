"""
? Class Nedir?
Sınıf (Class), nesne tabanlı programlamada temel bir yapıdır ve nesnelerin (objects) şablonunu veya taslağını tanımlar.
Sınıfların temel amacı nesne oluşturmak ve bu nesnelerin davranışlarını belirlemektir. 
Her bir nesne, sınıfın bir örneğini oluşturarak sınıfın özelliklerini ve metodlarını miras alır.
"""

"""
? Constructor Nedir?
Constructor metod (yapıcı metod), nesne tabanlı programlamada bir sınıfın örneklemesi (nesnesi) oluşturulurken çağrılan özel bir metoddur. 
Aynı zamanda __init__ olarak adlandırılır. 
İlk parametre olarak self parametresi ve özellik parametrelerini alır.

class SinifAdi:
    def __init__(self, parametreler):
        self.ozellik1 = deger1
        self.ozellik2 = deger2
        # ...

__init__: Constructor metodun adıdır.
self: Bu, nesnenin kendisini temsil eder ve sınıfın diğer metotlarında olduğu gibi kullanılır.

class Araba:
    def __init__(self, marka, model, renk):
        self.marka = marka
        self.model = model
        self.renk = renk

# Araba sınıfından bir nesne oluşturma
araba1 = Araba("Toyota", "Corolla", "Mavi")
"""

"""
? Kalıtım (inheritance) nedir?
Kalıtım (inheritance), nesne tabanlı programlamada bir sınıfın başka bir sınıftan özelliklerini ve metodlarını miras almasıdır. 
Kalıtım, mevcut bir sınıfın özelliklerini ve davranışlarını kullanarak yeni bir sınıf oluşturmanın bir yoludur. 
"""

"""
? Self nedir
self, nesne tabanlı programlamada kullanılan özel bir kelime ve Python'da bir metodun nesneyi temsil etmek için kullanılan bir referanstır. 
self, o anki nesneyi ifade eder ve bu nesnenin özelliklerine veya metodlarına erişmek için kullanılır.
"""

# class Araba:
#     marka = ""
#     renk = ""
#     plaka = ""
#     hiz = 0

#     def hizArttir(self):
#         self.hiz += 10
#         return self.hiz
    

# araba = Araba()
# araba.marka = "FORD"
# araba.renk = "Siyah"
# araba.plaka = "34 P 148"

# print("-------------ARABA--------------")
# print("Marka: {} \nRenk: {} \nPlaka: {}".format(araba.marka,araba.renk,araba.plaka))
# araba.hizArttir()
# print("Hız : ",araba.hiz)


# class Araba:
#     def __init__(self,model,renk,beygir_gücü,silindir):
#         self.model = model
#         self.renk = renk
#         self.beygir_gücü = beygir_gücü
#         self.silindir = silindir

# araba1 = Araba("Peugeot 301","Beyaz",90,4) 

# araba2 = Araba("Renault Megane","Gümüş",110,4)

# print(araba1.model)



#  ---- İstersek init metodunu varsayılan değerlerle de yazabiliriz.
class Araba:
    def __init__(self,model = "Bilgi Yok", renk = "Bilgi Yok", beygir_gücü = 75, silindir = 4):
        self.model = model
        self.renk = renk
        self.beygir_gücü = beygir_gücü
        self.silindir = silindir

araba1 = Araba(beygir_gücü = 85, renk = "Siyah")

print(araba1.renk)
print(araba1.model)