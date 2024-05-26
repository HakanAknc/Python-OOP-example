import  tkinter as tk

pencere= tk.Tk()

pencere.title("İlk arayüz programı")
pencere.geometry("500x300")

etiket = tk.Label(text="Hakan Akıncı", font="Verdana 22 bold")
etiket1 = tk.Label(text="Yunus Ensar Günay", font="Verdana 25")
etiket.pack()
etiket1.pack()

pencere.mainloop()