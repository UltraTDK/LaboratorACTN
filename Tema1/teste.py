from functions import modulo_p

print(modulo_p(-15, 11))
# print(modulo_p(6*5*4, 11))
# print(modulo_p(5*8*7, 11))

print(pow(4-1, -1, 11))
print(pow(4-3, -1, 11))

def calcul_x(polinom, x):
    suma = 0
    for index, i in enumerate(polinom):
        suma += i * x**((len(polinom) - 1) - index)
    return suma