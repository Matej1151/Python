import customtkinter as ctk
from PIL import Image


root = ctk.CTk()
root.title("The bean society")
root.geometry("1920x1080")
root.iconbitmap(r"C:\Users\Matej Grochal\Downloads\favicon.ico")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

obrazok = ctk.CTkImage(
    dark_image=Image.open(r"C:\Users\Matej Grochal\Downloads\tapeta.jpg"),
    light_image=Image.open(r"C:\Users\Matej Grochal\Downloads\tapeta.jpg"), 
    size=(1920, 1080)
)

etiopia = ctk.CTkImage(
    dark_image=Image.open(r"C:\Users\Matej Grochal\Downloads\etiopia.jpg"),
    light_image=Image.open(r"C:\Users\Matej Grochal\Downloads\etiopia.jpg"), 
    size=(300, 300)
)

kolumbia = ctk.CTkImage(
    dark_image=Image.open(r"C:\Users\Matej Grochal\Downloads\kolumbia.jpg"),
    light_image=Image.open(r"C:\Users\Matej Grochal\Downloads\kolumbia.jpg"), 
    size=(300, 300)
)

kostarika = ctk.CTkImage(
    dark_image=Image.open(r"C:\Users\Matej Grochal\Downloads\kostarika.jpg"),
    light_image=Image.open(r"C:\Users\Matej Grochal\Downloads\kostarika.jpg"), 
    size=(300, 300)
)

origin = ctk.CTkImage(
    dark_image=Image.open(r"C:\Users\Matej Grochal\Downloads\origin.jpg"),
    light_image=Image.open(r"C:\Users\Matej Grochal\Downloads\origin.jpg"), 
    size=(300, 300)
)

desighn = ctk.CTkImage(
    dark_image=Image.open(r"C:\Users\Matej Grochal\Downloads\desighn.jpg"),
    light_image=Image.open(r"C:\Users\Matej Grochal\Downloads\desighn.jpg"), 
    size=(300, 300)
)

flavor = ctk.CTkImage(
    dark_image=Image.open(r"C:\Users\Matej Grochal\Downloads\flavor.jpg"),
    light_image=Image.open(r"C:\Users\Matej Grochal\Downloads\flavor.jpg"), 
    size=(300, 300)
)






tapeta = ctk.CTkLabel(root, image=obrazok, text="")
tapeta.grid(row=0, column=0, sticky="nsew")

def strana_coffe():
    cat1.configure(fg_color="#9D6C34")
    cat2.configure(fg_color="#222222")
    cat3.configure(fg_color="#222222")
    txt1.configure(text="Ancient Roots, Bold Flavor")
    txt2.configure(text="Mountain Grown, Smooth Soul")
    txt3.configure(text="Pure Heights, Golden Balance")
    kv1.configure(image=etiopia)
    kv2.configure(image=kolumbia)
    kv3.configure(image=kostarika)
    knh1.configure(image="")
    knh2.configure(image="")
    knh3.configure(image="")
    txt1.place_configure(y=650)
    txt2.place_configure(y=650)
    txt3.place_configure(y=650)








def strana_books():
    cat1.configure(fg_color="#222222")
    cat2.configure(fg_color="#9D6C34")
    cat3.configure(fg_color="#222222")
    txt1.configure(text="Old stories shaping how\ntodays coffee truly feels.")
    txt2.configure(text="Simple ideas turning coffee\nbranding into clean beauty.")
    txt3.configure(text="Different beans showing how\n taste change with place.")
    kv1.configure(image=origin)
    kv2.configure(image=desighn)
    kv3.configure(image=flavor)
    txt1.place_configure(y=630)
    txt2.place_configure(y=630)
    txt3.place_configure(y=630)



def strana_coffee_machines():
    cat1.configure(fg_color="#222222")
    cat2.configure(fg_color="#222222")
    cat3.configure(fg_color="#9D6C34")
    txt1.configure(text="Coffe machine1")
    txt2.configure(text="Coffe machine2")
    txt3.configure(text="Coffe machine3")
    kv1.configure(image="")
    kv2.configure(image="")
    kv3.configure(image="")
    knh1.configure(image="")
    knh2.configure(image="")
    knh3.configure(image="")
    






buy1 = ctk.CTkButton(root, text="ADD TO CART",font=("Segoe UI Black", 20),fg_color="#DD831C",text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30)
buy1.place(x=375, y=700)
buy2 = ctk.CTkButton(root, text="ADD TO CART",font=("Segoe UI Black", 20),fg_color="#DD831C",text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30)
buy2.place(x=870, y=700)
buy3 = ctk.CTkButton(root, text="ADD TO CART",font=("Segoe UI Black", 20),fg_color="#DD831C",text_color="#532F07", hover_color="#362512", width=300, height=50, corner_radius=30)
buy3.place(x=1370, y=700)


kv1 = ctk.CTkLabel(root, image="", text="")
kv1.place(x=375, y=330)
kv2 = ctk.CTkLabel(root, image="", text="")
kv2.place(x=865, y=330)
kv3 = ctk.CTkLabel(root, image="", text="")
kv3.place(x=1365, y=330)

knh1 = ctk.CTkLabel(root, image="", text="")
knh1.place(x=375, y=330)
knh2 = ctk.CTkLabel(root, image="", text="")
knh2.place(x=865, y=330)
knh3 = ctk.CTkLabel(root, image="", text="")
knh3.place(x=1365, y=330)



txt1 = ctk.CTkLabel(root, text="", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222")
txt1.place(x=375, y=650)
txt2 = ctk.CTkLabel(root, text="", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222")
txt2.place(x=845, y=650)
txt3 = ctk.CTkLabel(root, text="", font=("Century Gothic", 24), text_color="#949494", fg_color="#222222")
txt3.place(x=1350, y=650)




cat1 = ctk.CTkButton(root, text="Coffee",font=("Century Gothic", 30),fg_color="#222222",text_color="#949494", hover=False, width=500, height=80, corner_radius=30, command=strana_coffe)
cat1.place(x=210, y=173)
cat2 = ctk.CTkButton(root, text="Books",font=("Century Gothic", 30),fg_color="#222222",text_color="#949494", hover=False, width=500, height=80, corner_radius=30, command=strana_books)
cat2.place(x=730, y=173)
cat3 = ctk.CTkButton(root, text="Coffee machines",font=("Century Gothic", 30),fg_color="#222222",text_color="#949494", hover=False, width=500, height=80, corner_radius=30, command=strana_coffee_machines)
cat3.place(x=1280, y=173)









root.mainloop()