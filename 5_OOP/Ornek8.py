# Overriding (İptal Etme)

# Eğer biz miras aldığımız metodları aynı isimle kendi sınıfımızda tekrar tanımlarsak , 
# artık metodu çağırdığımız zaman miras aldığımız değil kendi metodumuz çalışacaktır.
# Buna Nesne Tabanlı Programlamada bir metodu override etmek denmektedir


class Calisan:
    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri......")
        print("İsim : {} \nmaas : {} \ndepartman : {}".format(self.isim,self.maas,self.departman))
    
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor...")
        self.departman = yeni_departman

class Yonetici(Calisan):
    def __init__(self, isim, maas, departman,kisi_sayisi):  # Sorumlu olduğu kişi sayısı
        print("Yönetici sınıfının init fonksiyonu...")
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayisi = kisi_sayisi   # Yeni eklenen özellik
    
    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri......")
        print("İsim : {} \nmaas : {} \ndepartman : {} \nSorumlu kişi sayısı: {}".format(self.isim,self.maas,self.departman,self.kisi_sayisi))

    def zam_yap(self,zam_miktari):
        print("Maaşınıza zam yapıldı....")
        self.maas += zam_miktari


yonetici1 = Yonetici("Hakan",7500,"Aşçı",7)
yonetici1.bilgileri_goster()

print("*+/*+/*+/*+/*+/*+/+/+/*+/*+/*+/*+/*+/*+/")

calisan1 = Calisan("Yunus",4550,"İmam")
calisan1.bilgileri_goster()


# super Anahtar Kelimesi

# super anahtar kelimesi özellikle override ettiğimiz bir metodun içinde aynı zamanda miras aldığımız bir metodu kullanmak istersek kullanılabilir. 
# Yani super en genel anlamıyla miras aldığımız sınıfın metodlarını alt sınıflardan kullanmamızı sağlar. 
# Hemen örnek üzerinden anlamaya çalışalım.

class Çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim = isim
        self.maaş = maaş
        self.departman = departman
    def bilgilerigoster(self):
        
        print("Çalışan sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\n".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor....")
        self.departman = yeni_departman
class Yönetici(Çalışan):
    
    def __init__(self,isim,maaş,departman,kişi_sayısı): # Sorumlu olduğu kişi sayısı
        super().__init__(isim,maaş,departman) # 3 tane özelliği Çalışan fonksiyonunun init fonksiyonuyla hallediyoruz.
        
        print("Yönetici sınıfının init fonksiyonu")
        
        self.kişi_sayısı = kişi_sayısı # Ekstra özelliği de kendimiz yazıyoruz.
    def bilgilerigoster(self):
        
        print("Yönetici sınıfının bilgileri.....")
        
        print("İsim : {} \nMaaş: {} \nDepartman: {}\nSorumlu kişi sayısı: {}".format(self.isim,self.maaş,self.departman,self.kişi_sayısı))
    def zam_yap(self,zam_miktarı):
        print("Maaşa zam yapılıyor....")
        self.maaş += zam_miktarı

    
# yonetici2 = Yönetici("Ali",7500,"Öğretmen",8)
# yonetici2.bilgileri_goster()
