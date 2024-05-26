"""
Klavyeden girilen üç sayıdan büyüklük sıralamasına göre ortadaki sayıyı ekrana yazdıran programın algoritmasını yazınız
1. Başla
2. A, B, C Oku
3. Eğer B > A ve A > C ise x. adıma Git
4. Eğer C > A ve A > B ise x. adıma Git
5. Eğer A > B ve B > C ise x. adıma Git
6. Eğer C > B ve B > A ise x. adıma Git
7. Eğer A > C ve C > B ise x. adıma Git
8. Eğer B > C ve C > A ise x. adıma Git
9. A Yaz
10. 14. adıma Git
11. B Yaz
12. 14. adıma Git
13. C Yaz
14. Bitir
"""

A = int(input("A değeri: "))
B = int(input("B değeri: "))
C = int(input("C değeri: "))

if B > A and A > C or C > A and A > B:
    print("Ortadaki değer A yani = ",A)
elif A > B and B > C or C > B and B > A:
    print("Ortadaki değer B yani = ",B)
else:
    print("Ortadaki değer C yani = ",C)