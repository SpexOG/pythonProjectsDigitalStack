# Siruri de caractere imutabile si indexabile

var = "Sebi's name" # "" """ """
# sau var = 'Sebi\'s name'

""" concatenare """

print('pro' + 'gram' + 'are')

""" multuiplicare """

var1 = 'pro'

var2 = str()

multip = 4
print(multip * var1)

""" lungimea unui string len() """

var = 'programare'
     #0123456789
print(len(var))

""" operator de apartenenta: in si not in """

print('gr' in var)
print('gr' not in var)

""" indexare """ # indexare de la 0 ---- var[0] ---- nume_variabila[index]

print(var[3])
print(var[-1])
print(var[-len(var)])

""" slicing """ # [:]  - [start:stop:pas]

print(var[1:10:2])
print(var[-5::2])
print(var[-5:-8])

"""" interpolarea variabilelor in stringuri """

# Grupa de python de la Digital Stack by Orange
var_1 = 'Python'
var_2 = 'Digital Stack'
var_3 = 'Orange'

#caz1 concatenare

print("Grupa de " + var_1 + " de la " + var_2 + ' by ' + var_3 + '!')

#caz2 .format
    # cu acolade goale
print("Grupa de {} de la {} by {}!".format(var_1, var_2, var_3))
    # cu index la acolade
print("Grupa de {0} de la {1} by {2}!".format(var_1, var_2, var_3))
    # cu denumire variabila in acolade
print("Grupa de {str_1} de la {str_2} by {str_3}!".format(str_1 = 'Python', str_2 = var_2, str_3 = var_3))

#caz3 cu f'string

print(f"Grupa de {var_1} de la {var_2} by {var_3}!")

#varianta veche din Python 2.0

print('Grupa de %s de la %s by %s!' %(var_1, var_2, var_3))

""" cateva metode la stringuri """

var_1 = 'programare'
print(var_1.capitalize())
print(var_1.upper())
var_1 = 'PROGRAMARE'
print(var_1.lower())

var_2 = 'Ana banana'
print(var_2.count('na'))

var_3 = 'Metode folosite pentru stringuri'
print(var_3.find('folosite'))
print(var_3.find('zzzzzzzzz'))
print(var_3.index('folosite'))
#print(var_3.index('zzzzzzzz'))

var_4 = ['Ana', 'are', 'mere', '!']
print(' '.join(var_4))

var_5 = "Ana are mere !"
print(var_5.split())

var_6 = "Ana, are mere, are pere, si, are struguri !"
print(var_6.split(", "))

var_7 = '  programare  '
print(var_7.lstrip())
print(var_7.rstrip())
print(var_7.strip())

var_8 = 'Ana are mere'
print(var_8.replace('mere', 'pere'))
