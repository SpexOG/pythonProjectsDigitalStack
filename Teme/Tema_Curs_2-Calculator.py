rezultat_curent = None

while True:
    if rezultat_curent is not None:
        print(f"\nRezultat curent: {rezultat_curent}")
    else:
        print("\nNiciun rezultat în memorie.")

    expresie = input("Introdu expresia (ex: 5+3 sau +3 sau C/exit): ")

    if expresie.lower() == "exit":
        print("La revedere!")
        break

    if expresie.upper() == "C":
        rezultat_curent = None
        print("Memorie ștearsă.")
        continue

    expresie = expresie.replace(" ", "")

    caractere_permise = "0123456789+-*/"
    if not all(c in caractere_permise for c in expresie):
        print("Expresie invalidă! Folosește doar cifre și semnele +, -, *, /.")
        continue

    if rezultat_curent is None:
        operator = ""
        for op in "+-*/":
            if op in expresie:
                operator = op
                break

        if operator == "":
            print("Expresie invalidă! Adaugă un operator (+, -, *, /).")
            continue

        parti = expresie.split(operator)
        if len(parti) != 2 or parti[0] == "" or parti[1] == "":
            print("Expresie invalidă! Exemplu corect: 4+3")
            continue

        try:
            num1 = float(parti[0])
            num2 = float(parti[1])
        except ValueError:
            print("Expresie invalidă! Scrie doar cifre.")
            continue

        if operator == "+":
            rezultat_curent = num1 + num2
        elif operator == "-":
            rezultat_curent = num1 - num2
        elif operator == "*":
            rezultat_curent = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Eroare! Împărțirea la zero nu este permisă.")
                continue
            rezultat_curent = num1 / num2

    else:
        operator = expresie[0]
        try:
            num = float(expresie[1:])
        except ValueError:
            print("Expresie invalidă! Exemplu: +3 sau *2")
            continue

        if operator == "+":
            rezultat_curent += num
        elif operator == "-":
            rezultat_curent -= num
        elif operator == "*":
            rezultat_curent *= num
        elif operator == "/":
            if num == 0:
                print("Eroare! Împărțirea la zero nu este permisă.")
                continue
            rezultat_curent /= num
        else:
            print("Operator necunoscut!")
            continue

    print(f"Rezultatul este: {rezultat_curent}")