""" listele sunt colectii de obiecte si sunt mutabile si ordonate (deci indexabile). """
import math

var_list = []
var_list_a = list()

""" ordonare """

list_1 = [1, 2, 3, 4]
list_2 = [2, 1, 3, 4]

print(list_1 == list_2)
print(list_1 is list_2)

""" pot sa contina o varietate de elemente """

list_var = [1, 2.4, 'ana', True, None, ['1', 2, False], len, int, math]
print(list_var)

""" concatenare """

print([1, 2] + [3, 4])

""" multiplicare  """

print([1, 2] * 5)

""" lungimea len """



""" indexarea """

list_var = [1, 2.4, 'ana', True, None, ['1', 2, False], len, int, math]
print(list_var[2])

""" slicing """

print(list_var[2:4])

""" copiere """

list_var = [1, 2.4, 'ana', True, None]
list_copy = list_var[:]
print(list_copy)
print(list_copy is list_var)

list_copy_2 = list_var.copy()

list_copy_3 = list_var

print(list_copy_3 is list_var)

""" in si not in """
print(2.40 in list_var)

""" liste intrestesute (nested) """

list_var = [1, [2.4, 'ana', True, None, ['1', 2, False]], ['mere', [2], 'abc'], 0]
print(list_var[1][4][2])
print(list_var[2][1][0])

""" mutabilitate """

var_list = [1, 2.4, 'ana', True, None]
var_list[3] = False
print(var_list)

""" cateva metode """

list_m0 = [1, 3, 4, 2, 5, 1, 7 , 1]
print(list_m0.count(1))

#min si max

list_m1 = [45, 34.5, 2, 10 * 2, 88.88]
print(max(list_m1))
print(min(list_m1))

list_m4 = ['ana', 'are', 'mere', 'si', 'pere']
del list_m4[-2]
del list_m4[-1]
print(list_m4)

""" modificare liste """

list_m5 = ['ana', 'are', 'mere', 'si', 'pere']
list_m5[1:2] = ['nu', 'are', 'fructele']
print(list_m5)
list_m6 = [1, 2, 3]
list_m6[:1] = [11, 22, 33]
print(list_m6)

list_m7 = ['ana', 'are', 'mere', 'si', 'pere']
list_m7[3:4] = []
print(list_m7)

list_m8 = [1, 2.4, 'ana', True, None]
list_m8.append('ok')
print(list_m8)
list_m8 += ['Ion']
print(list_m8)
list_m8.extend([10000])
print(list_m8)
list_m9 = [1, 2.4, 'ana', True, None]
list_m9.insert(2, 'xxz')
print(list_m9)

list_m10 = [1, 2.4, 'ana', True, None, 'ana']
list_m10.remove('ana')
print(list_m10)

list_m11 = [1, 2.4, 'ana', True, None]
print(list_m11.pop())
print(list_m11)

list_m12 = [1, 2.4, 'ana', True, None]
#list_m12.clear()
print(list_m12)

list_m12.reverse()
print(list_m12)

list_13 = ['ana', 'are', 'mere', 'si', 'pere']
list_13.sort(reverse=True)
print(list_13)