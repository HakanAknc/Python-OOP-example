from tkinter import *

from tkinter import messagebox

pencere = Tk()

pencere.title("www.hakanakinci.com")
pencere.geometry("500x400")

uygulama = Frame(pencere)
uygulama.grid()

Lb1 = Listbox(uygulama)
Lb1.insert(1, "İstanbul")
Lb1.insert(2, "Edirne")
Lb1.insert(3, "Ağrı")
Lb1.insert(4, "Erzincan")
Lb1.insert(5, "Mersin")
Lb1.grid(padx=150, pady=10)

pencere.mainloop()