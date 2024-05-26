# 8. "başla" yazıldığında "araba harekete geçti", "dur" yazıldığında "araba durdu", "çıkış" 
# yazıldığında programdan çıkıldığı, "yardım yazıldığında başla, dur ve çıkış komutlarının 
# açıklamasının yapıldığı, başka bir ifade yazıldığında "yazdığını anlayamadım" yazan 
# Python programı

while True:
    komut = input("Komut girim ('başla', 'dur', 'çıkış', 'yardım'): ")

    if komut == "başla":
        print("Araba harekete geçti")
    elif komut == "dur":
        print("Araba durdu")
    elif komut == "çıkış":
        print("Programdan çıkış yapılıyor...")
    elif komut == "yardım":
        print("Komutlar:\n"
              "'başla' - Araba harekete geçer.\n"
              "'dur' - Araba durur.\n"
              "'çıkış' - Programdan çıkılır.\n"
              "'yardım' - Komut açıklamalarını gösterir.")
    else:
        print("Yazdığınızı anlayamadım. Lütfen geçerli bir komut girin: ")