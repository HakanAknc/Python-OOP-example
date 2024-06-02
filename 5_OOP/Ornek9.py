# Nesne Tabanlı Programlama - Özel Metodlar

# init metodu
class Kitap:
    def __init__(self,isim,yazar,sayfa_sayisi,tür):
        print("Kitap objesi oluşuyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tür = tür

# kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye") # Kendi metodumuz "


# str metodu
class Kitap:
    def __init__(self,isim,yazar,sayfa_sayisi,tür):
        print("Kitap objesi oluşuyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim : {}\nYazar : {}\nSayfa Sayıs : {}\nTür : {}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tür)
    
# kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
# print(kitap1)


# len metodu
class Kitap:
    def __init__(self,isim,yazar,sayfa_sayisi,tür):
        print("Kitap objesi oluşuyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim : {}\nYazar : {}\nSayfa Sayıs : {}\nTür : {}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tür)
    def __len__(self):
        return self.sayfa_sayisi

# kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
# print(len(kitap1))



# del metodu
class Kitap:
    def __init__(self,isim,yazar,sayfa_sayisi,tür):
        print("Kitap objesi oluşuyor...")   
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tür = tür
    def __str__(self):
        # Return kullanmamız gerekli
        return "İsim : {}\nYazar : {}\nSayfa Sayıs : {}\nTür : {}".format(self.isim,self.yazar,self.sayfa_sayisi,self.tür)
    def __len__(self):
        return self.sayfa_sayisi
    def __len__(self):
        return self.sayfa_sayisi
    def __del__(self):
        print("Kitap objesi siliniyor.......")


kitap1 = Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")
del(kitap1)
