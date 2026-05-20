import time

class kavovar:
    def __init__(self, znacka, voda):
        self.znacka = znacka
        self.voda = voda

    def barista(self):
        self.voda -= 10
        print("(Káva sa pripravuje...)")
        time.sleep(2)  
        print(f" ==== {self.znacka} ====\n   \\          /  |\n    \\________/___|\n   (__________)  ")
        print(f"Tu je tvoja káva značky {self.znacka}.\n(V kávovare {self.znacka} zostáva {self.voda}ml vody, teda počet zostávajúcich káv je {self.voda // 10}.)")

    def delonghi(self):
        self.voda -= 30
        print("(Káva sa pripravuje...)")
        time.sleep(2)
        print(f" ==== {self.znacka} ====\n   \\          /  |\n    \\________/___|\n   (__________)  ")
        print(f"Tu je tvoja káva značky {self.znacka}.\n(V kávovare {self.znacka} zostáva {self.voda}ml vody, teda počet zostávajúcich káv je {self.voda // 30}.)")
    
    def ano(self):
        kava = input(f"Super! Chceš kávu z kávovaru značky {kava_1.znacka} alebo {kava_2.znacka}?(Ak nevieš napíš 'neviem')\nTy: ")
        if kava == "neviem":
            kava = input(f"-{kava_1.znacka} 300ml je káva ktorá obsahuje viac vody, je jemnejšia a sladšia.\n-{kava_2.znacka} je 100ml káva ktorá obsahuje menej vody, je veľmi silná a horká.\n-Takže ktorú si dáš?\nTy: ")
        
        # TU JE OPRAVA: Voláme priamo kava_2 alebo kava_1 namiesto self
        if kava == "barista" or kava == "Barista":
            if kava_2.voda >= 10:
                kava_2.barista()  
            else:
                print(f"Prepáčte, ale v kávovare {kava_2.znacka} už došla voda.")
        else:
            if kava_1.voda >= 30:
                kava_1.delonghi()  
            else:
                print(f"Prepáčte, ale v kávovare {kava_1.znacka} už došla voda.")


# Vytvorenie objektov
kava_1 = kavovar("DeLonghi", 300)
kava_2 = kavovar("Barista", 100)

zakaznik = input("Chceš kávu?\nTy: ")

# Hlavná kontrola vody na začiatku programu
if kava_1.voda >= 30 or kava_2.voda >= 10:
    if "ano" in zakaznik or "Ano" in zakaznik or "áno" in zakaznik or "Áno" in zakaznik:
        if "barista" in zakaznik:
            if kava_2.voda >= 10:
                kava_2.barista()
            else:
                print("Prepáčte ale už nám došla.")
        elif "delonghi" in zakaznik:
            if kava_1.voda >= 30:
                kava_1.delonghi()
            else:
                print("Prepáčte ale už nám došla.")     
        else:
            kava_1.ano()
    else:
        print("Nevadí!")
else:
    print("Ospravedlňujeme sa, ale v kávovaroch nie je dostatok vody. Máme zatvorené.")
    