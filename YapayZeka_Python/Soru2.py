# 2. Klavyeden bir işçinin maaşı ve zam oranı girilerek yeni maaşını ekrana yazdıran

maas = int(input("Maşınızı giriniz: "))
zamOrani = float(input("Zam Oranını(%) giriniz: "))
yeniMaas = 0

yeniMaas = maas + ((maas)*(zamOrani)/100)

print("Yeni zamlı maaşınız ", yeniMaas, "TL Hayırlı olsun :)")