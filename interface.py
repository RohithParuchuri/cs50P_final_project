import tkinter as tk
from backend import spamer
from tkinter import ttk


def printer(event=None):
    if entry_adv.get() != "":
        time.set(entry_adv.get())
    num.set(entry_int.get())
    text.set(entry.get())
    if selected_option.get() == "Default":
        error_text.set("Select any of the above options")
    elif text.get() == "":
        error_text.set("Enter Something")
    elif time.get() != 0:
        spamer(entry.get(), num.get(), time.get())
    elif selected_option.get() == "Regular Spam":
        spamer(entry.get(), num.get())


def adv_clicked():
    entry_adv.forget()
    entry_adv.place(relx=0.55, rely=0.35, anchor="center", relheight=0.1, relwidth=0.1)


root = tk.Tk()
root.title("AutoText")
root.geometry("450x200")

error_text = tk.StringVar()
text = tk.StringVar()
num = tk.IntVar()
selected_option = tk.StringVar()
time = tk.IntVar()

title_lable = ttk.Label(root, text="TextTools", font="calibri 24 bold")
title_lable.place(relx=0.2, rely=0.5, anchor="center")

input_frame = ttk.Frame(root)

entry = ttk.Entry(root)
entry.place(relx=0.55, rely=0.5, anchor="center", relwidth=0.3, relheight=0.1)
entry_int = ttk.Entry(root)
entry_int.place(relx=0.55, rely=0.65, anchor="center", relheight=0.1, relwidth=0.1)
button = ttk.Button(root, text="Run!")

button.bind("<Leave>", func=lambda e: button.config(background="white"))
button.place(relx=0.85, rely=0.5, anchor="center")

root.bind("<Return>", printer)

output_lable = ttk.Label(textvariable=error_text, font="helvita 15 bold")
output_lable.place(relx=0.5, rely=0.95, anchor="center")

button_adv = ttk.Button(text="Advanced", command=adv_clicked)
button_adv.place(relx=0.55, rely=0.1, anchor="center")

entry_adv = ttk.Entry(text="label adv")

# r1 = ttk.Radiobutton(root, text="Regular Spam", value=1, command=lambda: option(1)).place(relx=0.05, rely=0.15)
# r2 = ttk.Radiobutton(root, text="Generative Spam", value=2, command=lambda: option(2)).place(relx = 0.05, rely = 0.25)

drop = ttk.OptionMenu(
    root, selected_option, "Default", "Regular Spam", "Generative Spam"
)
drop.place(relx=0.05, rely=0.15)

input_frame.pack()
root.mainloop()
