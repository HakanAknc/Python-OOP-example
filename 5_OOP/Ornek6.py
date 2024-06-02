# Nesne Tabanlı Programlama - Metodlar

class Yazilimci:
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim = isim
        self.soyisim = soyisim
        self.numara = numara
        self.maas = maas
        self.diller = diller
    
    def bilgileriniGöster(self):
        print("""
        Çalışan Bilgisi:
        
        İsim :  {}
        
        Soyisim : {}
        
        Şirket Numarası: {}
        
        Maaş :  {}
        
        Diller: {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))

    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyor.")
        self.diller.append(yeni_dil)

    def maas_yukselt(self,zam_miktari):
        print("Maaşa zam yapılyor...")
        self.maas += zam_miktari


yazilimci1 = Yazilimci("Hakan","Akıncı",12345,5000,["Java","Python","C"])
print(yazilimci1.isim,yazilimci1.soyisim,yazilimci1.numara,yazilimci1.maas,yazilimci1.diller)
print(yazilimci1.diller)

yazilimci2 = Yazilimci("Yunus","Ensar",54321,6000,["HTML","CSS","JavaScript"])
print(yazilimci2.isim,yazilimci2.soyisim,yazilimci2.numara,yazilimci2.maas,yazilimci2.diller)

yazilimci1.bilgileriniGöster()
yazilimci1.dil_ekle("HTML")
yazilimci1.bilgileriniGöster()

yazilimci1.maas_yukselt(600)
yazilimci1.bilgileriniGöster()