import tkinter as tk
from tkinter import colorchooser

def renk_sec():
    renk_kodu, renk = colorchooser.askcolor(title="Renk Seçin")
    if renk:
        canvas.config(bg=renk)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Renk Değiştirici")

# Renk seç düğmesi
button_renk_sec = tk.Button(root, text="Renk Seç", command=renk_sec)
button_renk_sec.pack(pady=20)

# Renk değiştirilecek alan
canvas = tk.Canvas(root, width=200, height=200, bg="white")
canvas.pack(padx=20, pady=20)

# Pencereyi başlat
root.mainloop()
