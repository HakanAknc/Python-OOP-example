# 9. Basit bir (1-3-5) sayı tutma oyunu yazın. Kullanıcıdan seçim alın, bilgisayarın seçimini 
# rastgele belirleyin ve kazananı ilan edin. (Açıklama: 5, 3’ü yener. 3, 1’i yener. 1 ise 5’i 
# yener. Aynı değerler tutulursa berabere kalınır)

import random

kullanici_secimi = int(input("1, 3 veya 5'i seçin: "))

bilgisayar_secimi = random.choice([1, 3, 5])

print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

if kullanici_secimi == bilgisayar_secimi:
    print("Berabere")
elif (kullanici_secimi == 1 and bilgisayar_secimi == 5) or \
     (kullanici_secimi == 3 and bilgisayar_secimi == 1) or \
     (kullanici_secimi == 5 and bilgisayar_secimi == 3):
    print("Kazandınız!")
else:
    print("Kaybettiniz... İyi günler")