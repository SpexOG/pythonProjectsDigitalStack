import os

def citeste_categorii():
    if not os.path.exists("categorii.txt"):
        return []
    with open("categorii.txt", "r") as f:
        return [linie.strip() for linie in f.readlines() if linie.strip()]

def salveaza_categorii(categorii):
    with open("categorii.txt", "w") as f:
        for c in categorii:
            f.write(c + "\n")

def citeste_taskuri():
    if not os.path.exists("taskuri.txt"):
        return []
    with open("taskuri.txt", "r") as f:
        linii = [linie.strip().split(";") for linie in f.readlines() if linie.strip()]
        return [{"task": t[0], "data": t[1], "persoana": t[2], "categorie": t[3]} for t in linii]

def salveaza_taskuri(taskuri):
    with open("taskuri.txt", "w") as f:
        for t in taskuri:
            f.write(f"{t['task']};{t['data']};{t['persoana']};{t['categorie']}\n")

def adauga_categorie(categorii):
    categorie = input("Introduceți o categorie noua: ").strip()
    if categorie in categorii:
        print("Categoria exista deja!")
    else:
        categorii.append(categorie)
        salveaza_categorii(categorii)
        print("Categorie adaugata cu succes!")

def adauga_task(taskuri, categorii):
    task = input("Introduceti taskul: ").strip()
    if any(t["task"] == task for t in taskuri):
        print("Taskul exista deja!")
        return
    data = input("Introduceti data limita (ex: 22.01.2025 21:30): ").strip()
    persoana = input("Introduceti persoana responsabila: ").strip()
    categorie = input("Introduceti categoria: ").strip()

    if categorie not in categorii:
        print("Categoria nu exista! Adaugați-o mai intai.")
        return

    taskuri.append({
        "task": task,
        "data": data,
        "persoana": persoana,
        "categorie": categorie
    })
    salveaza_taskuri(taskuri)
    print("Task adaugat cu succes!")

def afiseaza_taskuri(taskuri):
    if not taskuri:
        print("Nu exista taskuri salvate.")
        return
    taskuri_sortate = sorted(taskuri, key=lambda x: x["categorie"])
    for i, t in enumerate(taskuri_sortate, start=1):
        print(f"{i}. {t['task']} | {t['data']} | {t['persoana']} | {t['categorie']}")

def sorteaza_taskuri(taskuri):
    print("""
Alegeți criteriul de sortare:
1. task ascendent        2. task descendent
3. data ascendent        4. dată descendent
5. persoana ascendent    6. persoana descendent
7. categorie ascendent   8. categorie descendent
""")
    opt = input("Alegeti optiunea: ").strip()
    criterii = {
        "1": ("task", False),
        "2": ("task", True),
        "3": ("data", False),
        "4": ("data", True),
        "5": ("persoana", False),
        "6": ("persoana", True),
        "7": ("categorie", False),
        "8": ("categorie", True)
    }
    if opt not in criterii:
        print("Optiune invalida!")
        return
    camp, desc = criterii[opt]
    taskuri_sortate = sorted(taskuri, key=lambda x: x[camp], reverse=desc)
    afiseaza_taskuri(taskuri_sortate)

def filtreaza_taskuri(taskuri):
    print("""
Filtrați dupa:
1. Task
2. Data
3. Persoana responsabila
4. Categorie
""")
    opt = input("Alegeti campul: ").strip()
    campuri = {"1": "task", "2": "data", "3": "persoana", "4": "categorie"}
    if opt not in campuri:
        print("Optiune invalida!")
        return
    text = input("Introduceti textul de filtrare: ").strip().lower()
    camp = campuri[opt]
    filtrate = [t for t in taskuri if text in t[camp].lower()]
    afiseaza_taskuri(filtrate)

def editeaza_task(taskuri, categorii):
    afiseaza_taskuri(taskuri)
    try:
        nr = int(input("Introduceti numarul taskului de editat: ")) - 1
        if nr < 0 or nr >= len(taskuri):
            print("⚠️ Task invalid!")
            return
        t = taskuri[nr]
        print(f"Editați taskul (lasati gol pentru a pastra valoarea actuala):")
        nou_task = input(f"Task ({t['task']}): ").strip() or t['task']
        noua_data = input(f"Dată ({t['data']}): ").strip() or t['data']
        noua_persoana = input(f"Persoana ({t['persoana']}): ").strip() or t['persoana']
        noua_categorie = input(f"Categorie ({t['categorie']}): ").strip() or t['categorie']

        if noua_categorie not in categorii:
            print("Categoria nu exista!")
            return

        taskuri[nr] = {
            "task": nou_task,
            "data": noua_data,
            "persoana": noua_persoana,
            "categorie": noua_categorie
        }
        salveaza_taskuri(taskuri)
        print("Task editat cu succes!")
    except ValueError:
        print("Introduceti un numar valid!")

def sterge_task(taskuri):
    afiseaza_taskuri(taskuri)
    try:
        nr = int(input("Introduceti numarul taskului de sters: ")) - 1
        if nr < 0 or nr >= len(taskuri):
            print("Task invalid!")
            return
        del taskuri[nr]
        salveaza_taskuri(taskuri)
        print("Task sters cu succes!")
    except ValueError:
        print("Introduceti un numar valid!")

# --- Program principal ---
def main():
    categorii = citeste_categorii()
    taskuri = citeste_taskuri()

    print("=== BUN VENIT LA TO-DO LIST ===")
    if not categorii:
        print("Introduceti categoriile dorite (scrieți 'stop' pentru a opri):")
        while True:
            cat = input("Categorie: ").strip()
            if cat.lower() == "stop":
                break
            if cat and cat not in categorii:
                categorii.append(cat)
        salveaza_categorii(categorii)

    while True:
        print("""
=== MENIU PRINCIPAL ===
1. Listare taskuri
2. Sortare taskuri
3. Filtrare taskuri
4. Adaugare task
5. Editare task
6. Stergere task
7. Adaugare categorie
0. Iesire
""")
        opt = input("Alegeti o optiune: ").strip()
        if opt == "1":
            afiseaza_taskuri(taskuri)
        elif opt == "2":
            sorteaza_taskuri(taskuri)
        elif opt == "3":
            filtreaza_taskuri(taskuri)
        elif opt == "4":
            adauga_task(taskuri, categorii)
        elif opt == "5":
            editeaza_task(taskuri, categorii)
        elif opt == "6":
            sterge_task(taskuri)
        elif opt == "7":
            adauga_categorie(categorii)
        elif opt == "0":
            print("La revedere! 👋")
            break
        else:
            print("Optiune invalida!")

if __name__ == "__main__":
    main()
