import customtkinter as ctk
from backend import spamer

def feature(ignore=None):
    if drop.get() != "Default":
        try:
            if entry.get() == "":
                output_lable.configure(text="Enter Something")
                return
            if entry_int.get() == "":
                output_lable.configure(text="Enter number")
                return
            
            if entry_adv.get() != "":
                spamer(entry.get(), int(entry_int.get()), int(entry_adv.get()))
            else:
                spamer(entry.get(), int(entry_int.get()))
        except ValueError:
            output_lable.configure(text="Something went wrong")
    else:
        output_lable.configure(text="Select an option")

def menu_val(ingnore=None):
    output_lable.configure(text=drop.get())

def adv_clicked():
    if entry_adv.winfo_viewable():
        entry_adv.place_forget()
    else:
        entry_adv.place(relx=0.55, rely=0.35, anchor="center", relheight=0.1, relwidth=0.1)

root = ctk.CTk()
root.title("AutoText")
root.geometry("450x200")

title_lable = ctk.CTkLabel(root, text="TextTools", font=("calibre", 24))
title_lable.place(relx=0.2, rely=0.5, anchor="center")

entry = ctk.CTkEntry(root, placeholder_text="Enter Text")
entry.place(relx=0.55, rely=0.5, anchor="center", relwidth=0.3, relheight=0.1)
entry_int = ctk.CTkEntry(root, placeholder_text="Reps")
entry_int.place(relx=0.55, rely=0.65, anchor="center", relheight=0.1, relwidth=0.1)
button = ctk.CTkButton(root, text="Run!", command=feature)
button.place(relx=0.55, rely=0.91, anchor="center",relwidth=0.2)

drop = ctk.CTkOptionMenu(
    root, values=["Default", "Regular Spam", "Generative Spam"], command=menu_val
)

button_adv = ctk.CTkButton(root, text="Advanced", command=adv_clicked)
button_adv.place(relx=0.85, rely=0.5, anchor="center", relwidth=0.2)

drop.place(relx=0.05, rely=0.15)

output_lable = ctk.CTkLabel(root, font=("helvita", 15), text="")
output_lable.place(relx=0.5, rely=0.15, anchor="center")

entry_adv = ctk.CTkEntry(root, placeholder_text="Delay")

root.mainloop()
