judete = {
    "01": "Alba", "02": "Arad", "03": "Argeș", "04": "Bacău", "05": "Bihor",
    "06": "Bistrița-Năsăud", "07": "Botoșani", "08": "Brașov", "09": "Brăila",
    "10": "Buzău", "11"	: "Caraș-Severin", "12"	: "Cluj", "13"	: "Constanța",
    "14"	: "Covasna", "15" :	"Dâmbovița", "16" : "Dolj", "17" : "Galați",
    "18" : "Gorj", "19" : "Harghita", "20" : "Hunedoara", "21" : "Ialomița",
    "22" : "Iași", "23" : "Ilfov", "24" : "Maramureș", "25" : "Mehedinți",
    "26" : "Mureș", "27" :	"Neamț", "28" : "Olt", "29" : "Prahova",
    "30" : "Satu Mare", "31" : "Sălaj", "32" : "Sibiu", "33" : "Suceava",
    "34" : "Teleorman", "35" : "Timiș", "36" : "Tulcea", "37" : "Vaslui",
    "38" : "Vâlcea", "39" : "Vrancea", "40": "București", "41": "București - Sector 1",
    "42": "București - Sector 2", "43": "București - Sector 3", "44": "București - Sector 4",
    "45": "București - Sector 5", "46": "București - Sector 6"
}

while True:
    cnp = input("Introdu CNP-ul: ")

    # verificăm lungimea
    if len(cnp) != 13 or not cnp.isdigit():
        print("CNP invalid! Trebuie să conțină exact 13 cifre.")
        continue
    else:
        break

numar_control = "279146358279"
suma = 0
for i in range(12):
    suma += int(cnp[i]) * int(numar_control[i])

rest = suma % 11
cifra_control = 1 if rest == 10 else rest

if cifra_control != int(cnp[-1]):
    print("CNP invalid! Cifra de control nu corespunde.")
else:
    print("CNP valid!")

    s = int(cnp[0])
    if s in [1, 3, 5, 7]:
        sex = "Masculin"
    elif s in [2, 4, 6, 8]:
        sex = "Feminin"
    else:
        sex = "Necunoscut"

    aa = int(cnp[1:3])
    if s in [1, 2]:
        anul = 1900 + aa
    elif s in [3, 4]:
        anul = 1800 + aa
    elif s in [5, 6]:
        anul = 2000 + aa
    else:
        anul = 1900 + aa

    luna = cnp[3:5]
    zi = cnp[5:7]

    judet = cnp[7:9]
    locatie = judete.get(judet, "Județ necunoscut")

    print(f"Sex: {sex}")
    print(f"Data nașterii: {zi}-{luna}-{anul}")
    print(f"Locul nașterii: {locatie}")
