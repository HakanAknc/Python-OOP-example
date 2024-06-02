# Bir metindeki harf sayısını bulan bir for döngüsü:

metin = "Merhaba Dünya"
harfSayisi = 0
for harf in metin:
    if harf.isalpha():   # bir karakterin alfabetik bir karakter olup olmadığını sınar
        harfSayisi += 1

print("Toplam harf sayısı : ",harfSayisi)