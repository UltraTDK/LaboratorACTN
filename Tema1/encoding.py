from main import *
from functions import *


print("------- Pasul 2: codificare -------")


# mesajul sub forma de vector in Zp
# de tip string
mesaj_baza_x = conversie_baza_x(input, baza)
print("mesajul:", input, "in baza", baza, "este:", mesaj_baza_x)


# creare vector de mesaj in Zp
mesaj = vector_mesaj(mesaj_baza_x)
print("------- Vectorul de mesaj in Zp -------")
print("P(X) =", mesaj)


# initializare k, s, n, y
k = len(mesaj) + 1
s = 1
n = k + 2 * s
y = []


mesaj_prim = mesaj.copy()
mesaj_prim.append(0)
for indice in range(1, n + 1):
    y.append(horner(indice, mesaj_prim) % baza)


print("------- Mesajul codificat -------")
print("y:", y)
print("k:", k, "\ns:", s, "\nn:", n)