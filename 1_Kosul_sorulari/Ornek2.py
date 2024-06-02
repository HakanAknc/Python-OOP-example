# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol eden python uygulamasını yapınız.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.


isim = input("İsim giriniz : ")
egitim = input("Eğitim durumu : ")
yas = int(input("Yaşınız : "))

if(yas>=18):
    if(egitim=="lise" and egitim=="üniversite"):
        print("Ehliyet alabilitsiniz.")
    else:
        print("Eğitim yetersiz")
else:
    print("Yaşınız yetmiyor.")