import tkinter as tk
from tkinter import scrolledtext

def kaydet():
    icerik = entry_not.get("1.0", tk.END)
    with open("not_defteri.txt", "w") as dosya:
        dosya.write(icerik)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Not Defteri")

# Metin alanı
entry_not = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
entry_not.pack(padx=10, pady=10)

# Kaydet düğmesi
button_kaydet = tk.Button(root, text="Kaydet", command=kaydet)
button_kaydet.pack(pady=5)

# Pencereyi başlat
root.mainloop()
