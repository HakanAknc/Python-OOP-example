import tkinter as tk

pencere1 = tk.Tk()
pencere1.title("Birinci Pencere")
pencere1.configure(bg="red")

pencere2 = tk.Tk()
pencere2.title("İkinci pencere")
pencere2.configure(bg="blue")

pencere3 = tk.Tk()
pencere3.title("Üçüncü pencere")
pencere3.configure(bg="yellow")

pencere3.mainloop()

pencere2.mainloop()

pencere1.mainloop()