import customtkinter as ctk
from PIL import Image

# =====================================================================
# POLYMORFIZMUS (Triedy a výpočet DPH)
# =====================================================================
class Produkt:
    def __init__(self, cena):
        self.cena = cena
    def daj_cenu_bez_dph(self):
        pass

class StandardnyProdukt(Produkt):
    def daj_cenu_bez_dph(self):
        return self.cena / 1.20

class KnihaProdukt(Produkt):
    def daj_cenu_bez_dph(self):
        return self.cena / 1.10

kosik_produkty = []

# =====================================================================
# NASTAVENIE OKNA A OBRÁZKOV
# =====================================================================
root = ctk.CTk()
root.title("The bean society")
root.geometry("1920x1080")
root.iconbitmap(r"C:\Users\Matej Grochal\Documents\Škola\Programovanie\Python\eshop\favicon.ico")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

folder = r"C:\Users\Matej Grochal\Documents\Škola\Programovanie\Python\eshop"
zoznam_obrazkov = [
    "tapeta", "tapeta2", "tapeta3", "tapeta4",
    "etiopia", "kolumbia", "kostarika", "origin", "desighn", "flavor", "kavovar",
    "info", "home", "cart"
]

img = {}
for nazov in zoznam_obrazkov:
    if "tapeta" in nazov:
        velkost = (1920, 1080)
    elif nazov in ["info", "home", "cart"]:
        velkost = (50, 50)
    else:
        velkost = (300, 300)
    img[nazov] = ctk.CTkImage(dark_image=Image.open(f"{folder}\\{nazov}.jpg"), size=velkost)

hlavny_frame = ctk.CTkFrame(root, fg_color="transparent")
hlavny_frame.place(x=0, y=0, relwidth=1, relheight=1)

# =====================================================================
# POZADIE A LIŠTA S MENU (Zjednodušený štýl)
# =====================================================================
def vyčisti_a_menu(bg_img, aktívna_kat):
    for widget in hlavny_frame.winfo_children():
        widget.destroy()
        
    ctk.CTkLabel(hlavny_frame, image=img[bg_img], text="").place(x=0, y=0, relwidth=1, relheight=1)
    
    if aktívna_kat >= 0:
        if aktívna_kat == 0:
            farba_coffee = "#9D6C34" 
        else:
            farba_coffee = "#222222"     
        ctk.CTkButton(hlavny_frame, text="Coffee", command=strana_coffe, fg_color=farba_coffee, font=("Century Gothic", 30), width=500, height=80, corner_radius=30, text_color="#949494", hover=False).place(x=210, y=173)

        if aktívna_kat == 1:
            farba_books = "#9D6C34"
        else:
            farba_books = "#222222"
        ctk.CTkButton(hlavny_frame, text="Books", command=strana_books, fg_color=farba_books, font=("Century Gothic", 30), width=500, height=80, corner_radius=30, text_color="#949494", hover=False).place(x=730, y=173)

        if aktívna_kat == 2:
            farba_machines = "#9D6C34"
        else:
            farba_machines = "#222222"
        ctk.CTkButton(hlavny_frame, text="Coffee machines", command=strana_coffee_machines, fg_color=farba_machines, font=("Century Gothic", 30), width=500, height=80, corner_radius=30, text_color="#949494", hover=False).place(x=1250, y=173)

# =====================================================================
# STRÁNKY PRODUKTOV
# =====================================================================
def strana_coffe():  
    vyčisti_a_menu("tapeta", 0)
    
    ctk.CTkLabel(hlavny_frame, image=img["etiopia"], text="").place(x=375, y=330)
    ctk.CTkLabel(hlavny_frame, text="Ancient Roots, Bold Flavor", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222").place(x=375, y=650)
    ctk.CTkButton(hlavny_frame, text="10.99€", font=("Segoe UI Black", 20), fg_color="#DD831C", text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30, command=lambda: pridaj_do_kosika(StandardnyProdukt(10.99))).place(x=375, y=700)
    
    ctk.CTkLabel(hlavny_frame, image=img["kolumbia"], text="").place(x=865, y=330)
    ctk.CTkLabel(hlavny_frame, text="Mountain Grown, Smooth Soul", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222").place(x=845, y=650)
    ctk.CTkButton(hlavny_frame, text="9.99€", font=("Segoe UI Black", 20), fg_color="#DD831C", text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30, command=lambda: pridaj_do_kosika(StandardnyProdukt(9.99))).place(x=870, y=700)
    
    ctk.CTkLabel(hlavny_frame, image=img["kostarika"], text="").place(x=1365, y=330)
    ctk.CTkLabel(hlavny_frame, text="Pure Heights, Golden Balance", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222").place(x=1350, y=650)
    ctk.CTkButton(hlavny_frame, text="12.99€", font=("Segoe UI Black", 20), fg_color="#DD831C", text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30, command=lambda: pridaj_do_kosika(StandardnyProdukt(12.99))).place(x=1370, y=700)

def strana_books():   
    vyčisti_a_menu("tapeta", 1)
    
    ctk.CTkLabel(hlavny_frame, image=img["origin"], text="").place(x=375, y=330)
    ctk.CTkLabel(hlavny_frame, text="Old stories shaping how\ntodays coffee truly feels.", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222").place(x=375, y=630)
    ctk.CTkButton(hlavny_frame, text="25.99€", font=("Segoe UI Black", 20), fg_color="#DD831C", text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30, command=lambda: pridaj_do_kosika(StandardnyProdukt(25.99))).place(x=375, y=700)
    
    ctk.CTkLabel(hlavny_frame, image=img["desighn"], text="").place(x=865, y=330)
    ctk.CTkLabel(hlavny_frame, text="Simple ideas turning coffee\nbranding into clean beauty.", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222").place(x=845, y=630)
    ctk.CTkButton(hlavny_frame, text="25.99€", font=("Segoe UI Black", 20), fg_color="#DD831C", text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30, command=lambda: pridaj_do_kosika(KnihaProdukt(25.99))).place(x=870, y=700)
    
    ctk.CTkLabel(hlavny_frame, image=img["flavor"], text="").place(x=1365, y=330)
    ctk.CTkLabel(hlavny_frame, text="Different beans showing how\n taste change with place.", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222").place(x=1350, y=630)
    ctk.CTkButton(hlavny_frame, text="25.99€", font=("Segoe UI Black", 20), fg_color="#DD831C", text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30, command=lambda: pridaj_do_kosika(KnihaProdukt(25.99))).place(x=1370, y=700)

def strana_coffee_machines():
    vyčisti_a_menu("tapeta4", 2)

    ctk.CTkLabel(hlavny_frame, image=img["kavovar"], text="").place(x=865, y=330)
    ctk.CTkLabel(hlavny_frame, text="Precision in every cup.", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222").place(x=845, y=650)
    ctk.CTkButton(hlavny_frame, text="120.99€", font=("Segoe UI Black", 20), fg_color="#DD831C", text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30, command=lambda: pridaj_do_kosika(StandardnyProdukt(120.99))).place(x=870, y=700)

def strana_info():
    vyčisti_a_menu("tapeta2", -1)

# =====================================================================
# STRÁNKA KOŠÍKA
# =====================================================================
def strana_cart():
    vyčisti_a_menu("tapeta3", -1)
    
    # OPRAVA: Lokálne počítadlá nastavené na nulu pri každom otvorení košíka
    celkova_cena = 0
    cena_bez_dph = 0
    
    for p in kosik_produkty:
        celkova_cena = celkova_cena + p.cena
        cena_bez_dph = cena_bez_dph + p.daj_cenu_bez_dph()
    
    global crt
    crt = ctk.CTkLabel(hlavny_frame, text=f"Number of items: {len(kosik_produkty)}\n\nTotal price without DPH: {round(cena_bez_dph, 2)}€\n\nTotal price: {round(celkova_cena, 2)}€", font=("Century Gothic", 30), text_color="#949494", fg_color="#222222")
    crt.place(x=805, y=450)
    
    ctk.CTkButton(hlavny_frame, text="Clear Cart", font=("Segoe UI Black", 20), fg_color="#9D6C34", text_color="white", hover_color="#990000", width=300, height=50, corner_radius=30, command=vyprázdni_košík).place(x=870, y=650)

def pridaj_do_kosika(produkt_objekt):
    kosik_produkty.append(produkt_objekt)

def vyprázdni_košík():
    kosik_produkty.clear()
    crt.configure(text="Number of items: 0\n\nTotal price without DPH: 0.00€\n\nTotal price: 0.00€")

# =====================================================================
# FIXNÉ BOČNÉ MENU
# =====================================================================
ctk.CTkButton(root, image=img["info"], text="", fg_color="#222222", width=15, hover=False, command=strana_info).place(x=35, y=405)
ctk.CTkButton(root, image=img["home"], text="", fg_color="#222222", width=15, hover=False, command=strana_coffe).place(x=35, y=555)
ctk.CTkButton(root, image=img["cart"], text="", fg_color="#222222", width=15, hover=False, command=strana_cart).place(x=30, y=710)

strana_coffe()
root.mainloop()