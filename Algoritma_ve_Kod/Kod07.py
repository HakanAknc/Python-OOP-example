"""
Dışarıdan girilen saniye değerini saat, dakika ve saniyeye çevirerek sa:dk:sn biçiminde gösteren programın algoritmasını yazınız. 
1. Başla
2. sn  Oku
3. sa = Tam(sn / 3600)
4. sn = sn – (sa x 3600)
5. dk = sn DIV / 60
6. sn = sn MOD 60
7. sa ‘:’ dk ‘:’ sn Yaz
8. Bitir
"""

# Kullanıcıdan saniye değerini al
sn = int(input("Saniye değeri: "))

# Saat, dakika ve saniyeyi hesapla
sa = sn // 3600
sn -= sa * 3600

dk = sn // 60
sn %= 60

# Sonucu ekrana yazdır
print(f"{sa}:{dk}:{sn}")
