# Kütüphane Yönetim Sistemi

class Kitap:
    def __init__(self, kitap_id, ad, yazar):
        self.kitap_id = kitap_id
        self.ad = ad
        self.yazar = yazar
        self.durum = "Rafta"

    def kitap_bilgileri(self):
        # print(f"Kitap ID: {self.kitap_id} Ad: {self.ad} Yazar: {self.yazar} Durum: {self.durum}")
        return f"Kitap ID: {self.kitap_id} Ad: {self.ad} Yazar: {self.yazar} Durum: {self.durum}"

kitap1 = Kitap(1,"Ateş ve Su","İmran Tohumcu")
print(kitap1.kitap_id,kitap1.ad,kitap1.yazar,kitap1.durum)

