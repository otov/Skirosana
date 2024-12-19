import tkinter as tk
from tkinter import messagebox


def skir(veidi):
    kategorijas={"plastmasas pudele":"Plastmasa",
                "stikla pudele": "Stikls",
                "kartona iepakojums":"Papīrs",
                "dators":"E-atkritumi",
                "augļi":"Organiskie atkritumi",
                "telefons":"E-atkritumi",
                "opelis":"Tolmets"
                }

    veidi=veidi.lower().strip()

    if veidi in kategorijas:
        return f"{veidi.capitalize()} jāliek {kategorijas[veidi]} konteinerā!" 
    else:
        return "Atkritumu veids nav sarakstā!"

def skirosanas_button():
    ievade=entrayy.get()

    result=skir(ievade)

    messagebox.showinfo("Rezultāts", result)

logs= tk.Tk()
logs.title("Atkritumu šķirošanas sistēma")

logs.geometry("250x200")
label=tk.Label(logs,text="Ievadiet atkritumu veidu: ")
label.pack(pady=10)

entrayy=tk.Entry(logs,width=30)
entrayy.pack(pady=10)

botton1 = tk.Button(logs, text="Šķirot",command=skirosanas_button)
botton1.pack(pady=10)



logs.mainloop()












