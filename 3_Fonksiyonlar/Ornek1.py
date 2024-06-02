# def hello():
#     print("Merhaba")

# hello()


# def hello(name):
#     print("Merhaba "+ name)

# hello("Hakan")


# def hello():
#     return "Merhaba"

# print(hello())


# def hello(name):
#     return "Merhaba " + name

# print(hello("Hakan"))

def yasHesapla(dogumYili):
    return 2023 - dogumYili

hakan = yasHesapla(2001)
print("Yaşınız : " , hakan)

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"emekliliğinize {emeklilik} yıl kaldı {isim} bey")
    else:
        print("zaten emekli oldunuz")

emekliligeKacYilKaldi(2001,"Hakan")