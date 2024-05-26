import tkinter as tk

def hesapla():
    try:
        sayi1 = float(entry_sayi1.get())
        sayi2 = float(entry_sayi2.get())
        sonuc = sayi1 + sayi2
        label_sonuc.config(text="Sonuç: " + str(sonuc))
    except ValueError:
        label_sonuc.config(text="Hatalı Giriş!")

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Hesap Makinesi")

# Giriş alanları
entry_sayi1 = tk.Entry(root, width=10)
entry_sayi1.grid(row=0, column=0, padx=5, pady=5)

entry_sayi2 = tk.Entry(root, width=10)
entry_sayi2.grid(row=0, column=1, padx=5, pady=5)

# Hesapla düğmesi
button_hesapla = tk.Button(root, text="Hesapla", command=hesapla)
button_hesapla.grid(row=1, column=0, columnspan=2, pady=5)

# Sonuç etiketi
label_sonuc = tk.Label(root, text="Sonuç: ")
label_sonuc.grid(row=2, column=0, columnspan=2)

# Pencereyi başlat
root.mainloop()
