from encoding import *
import random
from itertools import combinations


print("------- Pasul 3: decodificare -------")


# crearea lui z
pozitie = random.randrange(len(y))
z = y.copy()
valoare = random.randrange(0, 100) % baza
while valoare == y[pozitie]:
    valoare = random.randrange(0, 100) % baza
z[pozitie] = valoare


# crearea lui A
pozitii_fara_eroare = []
pozitii_cu_eroare = []
for indice in range(0, len(z)):
    if z[indice] == y[indice]:
        pozitii_fara_eroare.append(indice + 1)
    else:
        pozitii_cu_eroare.append(indice + 1)


print("z:", z)
print("Pozitii fara eroare:", pozitii_fara_eroare)
print("Pozitii cu eroare:", pozitii_cu_eroare) 


k_inversari = []
for inversare in combinations(pozitii_fara_eroare, k):
    k_inversari.append(inversare)


coef_lib1 = calcul_coeficient_liber(k_inversari)


print("------- K inversari -------")
for i in range(len(k_inversari)):
    polinom_de_construit = k_inversari[i]
    print("CL:", coef_lib1[i], "pentru", k_inversari[i])


print("------- Evaluare polinom -------")
coeficienti = reconstructie_polinom(polinom_de_construit, z, baza)

