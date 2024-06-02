class Calisanlar:  # class tanımı yapıldı obje
    def __init__(self,name,surname,age):   # Constructor yapıldı == __init__(self)
        self.name = name
        self.surname = surname   # değişkenler tanımlandı  attribute
        self.age = age

    def show_info(self):  # metot fonksiyon tanımlama
        print(f"Ad : {self.name} Soyad : {self.surname} Yaş : {self.age}")
        # print("Merhaba ben {} {} {} yaşındayım.".format(self.name,self.surname,self.age))  # format ile yazım


calisan1 = Calisanlar("Hakan","Akncı",22)   
print(calisan1.name,calisan1.surname,calisan1.age)

calisan2 =  Calisanlar("Yunus","Ensar",25)
print(calisan2.name,calisan2.surname,calisan2.age)

calisan3 = Calisanlar("Atıf","Bistami",23)



calisan1.show_info()
calisan2.show_info()
calisan3.show_info()