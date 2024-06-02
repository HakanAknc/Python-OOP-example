# Yukarıdaki örnekte kullanıcıdan vize1, vize2 ve final notları isteniyor. 
# Genel ortalama, vize1 ile vize2 nin ortalamasının %40’ı, finalin ise %60’ı alınarak bulunuyor.

vize1 = float(input("Vize 1 notunu giriniz : "))
vize2 = float(input("Vize 2 notunu giirniz  : "))
final = float(input("Final notunu giriniz : "))

ortalama = (((vize1 + vize2)/2)*0.4) + (final*0.6)

print("Not ortalamaniz : ",ortalama)

if (final >= 50):
    if ortalama > 85 and final > 50:
        print("Harf Notunuz AA")
    elif ortalama > 75 and  ortalama< 85:
        print("Harf Notunuz BA")
    elif ortalama >= 70 and ortalama < 75:
        print("Harf Notunuz BB")
    elif ortalama >= 65 and ortalama < 70:
        print("Harf Notunuz CB")
    elif ortalama >= 60 and ortalama < 65:
        print("Harf Notunuz CC")
    elif ortalama >= 55 and ortalama < 60:
        print("Harf Notunuz DC")
    elif ortalama >= 50 and ortalama < 55:
        print("Harf Notunuz DD")

else:
    print("Harf Notunuz FF kaldınız...")

