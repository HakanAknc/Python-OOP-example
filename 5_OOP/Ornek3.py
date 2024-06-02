class Kisi:
    def __init__(self,ad,yas):
        self.ad = ad
        self.yas = yas

    def tanit(self):
        print(f"Merhaba, benim adım {self.ad} ve {self.yas} yaşındayım.")

# Kisi sınıfından nesneler oluşturma
kisi1 = Kisi("Hakan",22)
kisi2 = Kisi("Evren",5)
print(kisi1.ad,kisi1.yas)

# Nesnelerin özelliklerini kullanarak metodu çağırma
kisi1.tanit()
kisi2.tanit()
