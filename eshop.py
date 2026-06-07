import customtkinter as ctk
from PIL import Image

logo = ctk.CTkImage(light_image=Image.open(r"C:\Users\Matej Grochal\Downloads\logo.png"), size=(120, 120))
brown = ctk.CTkImage(light_image=Image.open(r"C:\Users\Matej Grochal\Downloads\brown.png"), size=(1000, 150))

#Okno
app = ctk.CTk()
app.geometry("1000x700")
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)
ctk.set_appearance_mode("light")




#Strana1
def strana_2():
    f1.grid_forget()
    f3.grid_forget()
    f2.grid(row=0, column=0, sticky="nsew")
#Strana2
def strana_1():
    f2.grid_forget()
    f3.grid_forget()
    f1.grid(row=0, column=0, sticky="nsew")

def strana_3(hodnota):
    info_label.configure(text=f"Kupuješ produkt číslo: {hodnota}")
    f2.grid_forget()
    f1.grid_forget()   
    f3.grid(row=0, column=0, sticky="nsew")






#Tlačidla v strane1
f1 = ctk.CTkFrame(app)
f1.columnconfigure(0, weight=1)
f1.columnconfigure(1, weight=1)
horny_banner = ctk.CTkFrame(f1, height=150, fg_color="#795841", corner_radius=0)
horny_banner.grid(row=0, column=0, columnspan=2, sticky="ew")
horny_banner.grid_propagate(False)
btn1 = ctk.CTkButton(f1, image=logo, text="", fg_color="transparent",bg_color="#795841", hover=False, command=strana_2)
btn1.grid(row=0, column=0, sticky="w", padx=20, pady=20)
btn2 = ctk.CTkButton(f1, text="kupit", command=lambda: strana_3(1))
btn2.grid(row=1, column=1,pady=150)
btn3 = ctk.CTkButton(f1, text="kupit", command=lambda: strana_3(2))
btn3.grid(row=1, column=0,)
btn4 = ctk.CTkButton(f1, text="kupit", command=lambda: strana_3(3))
btn4.grid(row=2, column=1, pady=150)
btn5 = ctk.CTkButton(f1, text="kupit", command=lambda: strana_3(4))
btn5.grid(row=2, column=0,)



#Tlačidla v strane2
f2 = ctk.CTkFrame(app)
f2.columnconfigure(0, weight=1)
btn0 = ctk.CTkButton(f2, text="Nakupovať", command=strana_1)
btn0.grid(row=1, column=0,pady=400)
horny_banner = ctk.CTkFrame(f2, height=150, fg_color="#795841", corner_radius=0)
horny_banner.grid(row=0, column=0, columnspan=2, sticky="ew")
horny_banner.grid_propagate(False)
btn1 = ctk.CTkButton(f2, image=logo, text="", fg_color="transparent",bg_color="#795841", hover=False, command=strana_2)
btn1.grid(row=0, column=0, sticky="w", padx=20, pady=20)



f3 = ctk.CTkFrame(app)
f3.columnconfigure(0, weight=1)
info_label = ctk.CTkLabel(f3, text="", font=("Arial", 24))
info_label.grid(row=3, column=0, pady=100)
horny_banner = ctk.CTkFrame(f3, height=150, fg_color="#795841", corner_radius=0)
horny_banner.grid(row=0, column=0, columnspan=2, sticky="ew")
horny_banner.grid_propagate(False)
btn1 = ctk.CTkButton(f3, image=logo, text="", fg_color="transparent",bg_color="#795841", hover=False, command=strana_2)
btn1.grid(row=0, column=0, sticky="w", padx=20, pady=20)



#Stranka zobrazujuca po štarte
f1.grid(row=0, column=0, sticky="nsew")


app.mainloop()