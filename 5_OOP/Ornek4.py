class Calisan:
    def __init__(self, ad, maas):
        self.ad = ad
        self.maas = maas

    def zam_yap(self, yuzde):
        zam_miktari = self.maas * (yuzde / 100)
        self.maas += zam_miktari
        print(f"{self.ad}'ın maaşı %{yuzde} zamla arttırıldı. Yeni maaşı: {self.maas} TL")

calisan1 = Calisan("Hakan", 5000)
calisan2 = Calisan("Evren", 6500)

calisan1.zam_yap(10)
calisan1.zam_yap(20)