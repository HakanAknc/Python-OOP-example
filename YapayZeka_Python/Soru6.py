# 6. Kullanıcıdan ad, vize ve final notunu alan, sonuçta ad, başarı notu ve “Geçti/Kaldı” 
# yazan program. (Başarı notu hesaplamada ölçüt: Vize: % 40 – Final: % 60)

isim = input("İsminizi giriniz: ")

vize = int(input("Vize notunuz: "))
final = int(input("Final notunuz: "))

sonuc = (vize * 0.4) + (final * 0.6)

print(f"\nAd: {isim}")
print(f"Başarı Notu: {sonuc}")

if sonuc >= 50:
    print("Durum: Geçti")
else:
    print("Durum: Kaldı")