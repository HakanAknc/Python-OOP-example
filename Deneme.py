"""
range(bitis_degeri) [0,50]
range(baslanhıc_degeri, bitis_degeri)
range(baslangıc_degeri,bitis_degeri,artıs_miktarı)
"""

# for eleman in range(10):
#     print(eleman)


# for x in range(25,30):
#     print("Hello")


# for i in range(0,91,9):
#     print(i)


# for x in range(1500,49000):
#     if x%3==0 and x%7==0 and x%5==0:
#         print(x)


"""
Üçgen çizdirme
*
**
***
****
*****
"""
# Çözüm1
# n = int(input("Üçgenin yüksekliğini girin: "))

# for i in range(1, n+1):
#     print('*' * i)


# Çözüm2
# satir=int(input("Lutfen kac satirlik ucgen cizmek istedigini giriniz:"))

# for x in range(1,satir+1):
#     for y in range(x):
#         print("*",end="")
#     print()


#fibonacci yazdırma
x,y=0,1

while y<100:
    print(y,end=" ")
    x,y=y, x+y


"""
Kullanıcı yüksek güvenlikli bir sistemde şifre oluşturacaktır.
Şifree kesinlikle 2 adet büyük harf, a adet küçük harf
2 adet rakam ve 2 adet özel sembol olmalıdır.
"""

