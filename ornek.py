sesli_harfler = "aeıioöuü"
sayaç = 0

kelime = input("Bir kelime giriniz: ")

for harf in kelime:
    if harf in sesli_harfler:
        sayaç += 1

mesaj = "{} kelimesinde {} sesli harf var."
print(mesaj.format(kelime,sayaç))

