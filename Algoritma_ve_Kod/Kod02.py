"""
User
Klavyeden girilen iki sayı ve bir işlem operatörü (+, -, *, /) ne göre işlem yapıp sonucu ekrana yazdıran programın algoritmasını yazınız. 
1. Başla
2. A, B, Op Oku
3. Eğer Op = “+” ise x. adıma Git
4. Eğer Op = “-” ise x. adıma Git
5. Eğer Op = “*” ise x. adıma Git
6. Eğer Op = “/” ise x. adıma Git
7. Sonuc = A + B
8. 14. adıma Git
9. Sonuc = A - B
10. 14. adıma Git
11. Sonuc = A * B
12. 14. adıma Git
13. Sonuc = A / B
14. Sonuc Yaz 
15. Bitir
"""

A = float(input("A değeri: "))
B = float(input("B değeri: "))
Op = input("Operatör (+, -, *, /): ")

if Op == "+":
    Sonuc = A + B
elif Op == "-":
    Sonuc = A - B
elif Op == "*":
    Sonuc = A * B
elif Op == "/":
    Sonuc = A / B
else:
    print("Geçersiz operatör! Lütfen +, -, * veya / kullanın.")

# print("Sonuç:", Sonuc)

# print(f"Sonuç {A} {Op} {B} = ",Sonuc)

print("Sonuc {} {} {} =".format(A,Op,B),Sonuc)

