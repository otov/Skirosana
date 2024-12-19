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

def main():
    print("Sveicināti atkritumu šķirošanas sistēmā!")
    while True:
        inputw=input("Ievadiet atkritumu veidu!: ").strip()

        if inputw.lower()=="exit":
            print("Paldies ka izmantojāt šķirošanas sistēmu!")
            break

        result = skir(inputw)
        print(result)

if __name__=="__main__":
    main()
