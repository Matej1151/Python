import customtkinter as ctk
import time
import threading

# Nastavenie vzhľadu CustomTkinter
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")

class KavovarGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Nastavenia hlavného okna
        self.title("Smart Kávovar")
        self.geometry("550x650")
        self.resizable(False, False)

        # Naše kávovary (dáta umiestnené bezpečne vnútri objektu okna)
        self.voda_delonghi = 300
        self.voda_barista = 100

        # Vytvorenie GUI prvkov
        self.vytvor_rozhranie()

    def vytvor_rozhranie(self):
        # Hlavný nadpis
        self.nadpis = ctk.CTkLabel(self, text="☕ Smart Kaviareň", font=ctk.CTkFont(size=26, weight="bold"))
        self.nadpis.pack(pady=20)

        # Rámček pre štatistiky vody
        self.ramcek_status = ctk.CTkFrame(self)
        self.ramcek_status.pack(pady=10, fill="x", padx=40)

        self.lbl_delonghi = ctk.CTkLabel(self.ramcek_status, text=f"DeLonghi: {self.voda_delonghi} ml (spotreba 30ml/káva)", font=ctk.CTkFont(size=14))
        self.lbl_delonghi.pack(pady=5)

        self.lbl_barista = ctk.CTkLabel(self.ramcek_status, text=f"Barista: {self.voda_barista} ml (spotreba 10ml/káva)", font=ctk.CTkFont(size=14))
        self.lbl_barista.pack(pady=5)

        # Rámček pre tlačidlá
        self.ramcek_tlacidla = ctk.CTkFrame(self, fg_color="transparent")
        self.ramcek_tlacidla.pack(pady=20)

        self.btn_delonghi = ctk.CTkButton(self.ramcek_tlacidla, text="Objednať DeLonghi (30ml)", command=self.klik_delonghi, width=200, height=40)
        self.btn_delonghi.grid(row=0, column=0, padx=10)

        self.btn_barista = ctk.CTkButton(self.ramcek_tlacidla, text="Objednať Barista (10ml)", command=self.klik_barista, width=200, height=40)
        self.btn_barista.grid(row=0, column=1, padx=10)

        self.btn_neviem = ctk.CTkButton(self, text="💡 Neviem si vybrať", fg_color="gray", hover_color="#555555", command=self.klik_neviem)
        self.btn_neviem.pack(pady=5)

        # Textové pole pre stav a ASCII Art kávu
        self.txt_displej = ctk.CTkTextbox(self, width=470, height=320, font=ctk.CTkFont(family="Courier", size=12))
        self.txt_displej.pack(pady=20)
        self.txt_displej.insert("1.0", "Vitajte! Vyberte si svoju kávu...")
        self.txt_displej.configure(state="disabled")

    def aktualizuj_displej(self, text):
        self.txt_displej.configure(state="normal")
        self.txt_displej.delete("1.0", "end")
        self.txt_displej.insert("1.0", text)
        self.txt_displej.configure(state="disabled")

    def aktualizuj_vodu(self):
        self.lbl_delonghi.configure(text=f"DeLonghi: {self.voda_delonghi} ml (spotreba 30ml/káva)")
        self.lbl_barista.configure(text=f"Barista: {self.voda_barista} ml (spotreba 10ml/káva)")

    def klik_delonghi(self):
        if self.voda_delonghi >= 30:
            threading.Thread(target=self.priprav_kavu, args=("DeLonghi", 30)).start()
        else:
            self.aktualizuj_displej("Chyba: V kávovare DeLonghi už nie je dostatok vody!")

    def klik_barista(self):
        if self.voda_barista >= 10:
            threading.Thread(target=self.priprav_kavu, args=("Barista", 10)).start()
        else:
            self.aktualizuj_displej("Chyba: V kávovare Barista už nie je dostatok vody!")

    # OPRAVENÉ: Správne zapísaná klasická funkcia bez lambda syntax-chyby
    def klik_neviem(self):
        text_napovedy = (
            "- DeLonghi: Káva obsahuje viac vody, je jemnejšia a sladšia.\n"
            "- Barista: Káva obsahuje menej vody, je veľmi silná a horká.\n\n"
            "Kliknite na jedno z vrchných tlačidiel pre objednávku."
        )
        self.aktualizuj_displej(text_napovedy)

    def priprav_kavu(self, znacka, spotreba):
        # Zablokujeme tlačidlá
        self.btn_delonghi.configure(state="disabled")
        self.btn_barista.configure(state="disabled")
        
        if znacka == "DeLonghi":
            self.voda_delonghi -= spotreba
            aktualna_voda = self.voda_delonghi
            zostava = self.voda_delonghi // 30
        else:
            self.voda_barista -= spotreba
            aktualna_voda = self.voda_barista
            zostava = self.voda_barista // 10

        self.aktualizuj_vodu()
        self.aktualizuj_displej(f"({znacka} káva sa pripravuje, prosím čakajte...)")
        
        time.sleep(2)  # Simulácia varenia

        # ASCII Art pohára
        ascii_art = (
            f"      ==== {znacka} ====\n"
            f"        \\          /  |\n"
            f"         \\________/___|\n"
            f"        (__________)\n\n"
            f"Tu je tvoja káva značky {znacka}.\n"
            f"V kávovare zostáva {aktualna_voda}ml vody.\n"
            f"Môžeš urobiť ešte {zostava} káv."
        )
        
        self.aktualizuj_displej(ascii_art)
        
        # Opäť povolíme tlačidlá
        self.btn_delonghi.configure(state="normal")
        self.btn_barista.configure(state="normal")

# Spustenie aplikácie
if __name__ == "__main__":
    app = KavovarGUI()
    app.mainloop()