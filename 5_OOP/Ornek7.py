# Nesne Tabanlı Programlama - Kalıtım (Inheritance)

# Bu konuda Nesne Tabanlı Programlamadaki inheritance(kalıtım veya miras alma) konseptini öğrenmeye çalışacağız. 
# Inheritance veya kalıtım bir sınıfın başka bir sınıftan özelliklerini(attribute ) ve metodlarını miras almasıdır.

class Calisan:
    def __init__(self,isim,maas,departman):
        print("Çalışan sınıfının init fonksiyonu çalıştı.")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileriGoster(self):
        print("Çalışan sınıfının bilgileri ...... ")
        print("İsim : {} \nmaas : {} \ndepartman : {}\n".format(self.isim,self.maas,self.departman))

    def departman_degistir(self,yeni_departman):
        print("Departman değişiyor...")
        self.departman = yeni_departman

class Yonetici(Calisan):  # Çalışan sınıfından miras alıyoruz.
    def zam_yap(self,zam_miktari):
        print("Maaşınıza zam yapılıyor.")
        self.maas += zam_miktari

# calisan1 = Calisan("Hakan",5000,"Yazılımcı")
# print(calisan1.isim,calisan1.maas,calisan1.departman)
# calisan1.bilgileriGoster()

yonetici1 = Yonetici("Ali",8500,"İnsan Kaynakları")
print(yonetici1.isim,yonetici1.maas,yonetici1.departman)
yonetici1.bilgileriGoster()

yonetici1.departman_degistir("Polis")
yonetici1.bilgileriGoster()  # bütün özellikleri ve metodları Çalışan sınıfından miras aldığımız için kullanabiliyoruz.

print("************************************")


# Peki biz Yönetici sınıfına ekstra fonksiyonlar ve özellikler ekleyebiliyor muyuz? Örnek zam_yap isimli bir metod ekleyelim.
yonetici2 = Yonetici("Adnan",9000,"Mühendis")
yonetici2.bilgileriGoster()

yonetici2.zam_yap(800)
yonetici2.bilgileriGoster()

print("************************************")


