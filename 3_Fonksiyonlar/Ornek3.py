"""
Python fonksiyonlarını kullanarak bankamatik uygulaması yapıyoruz.
"""

HakanHesap = {
    'ad' : 'Hakan Akıncı',
    'hesapNo' : '123456789',
    'bakiye' : 4000,
    'ekHesap' : 3000
}

EvrenHesap = {
    'ad' : 'Evren Akıncı',
    'hesapNo' : '987654321',
    'bakiye' : 3000,
    'ekHesap' : 2000
}

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")


def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabiliriniz iyi günler ... :) ")
        bakiyeSorgula(hesap)
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input("Ek hesap kullanılsın mı (e/h)")

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0  # Eğer ek hesap kullanılıyorsa, hesap bakiyesi sıfırlanır çünkü bakiyenin tamamı kullanılmıştır.
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print("Paranızı alabilirsiniz çok harcamayın iyi günler.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print("Üzgünüm bakiye yetersiz... :(")
            bakiyeSorgula(hesap)


print(paraCek(HakanHesap,9000))
