import random
import sympy
from multiPrimeFunctions import *


print("------- MULTI-PRIME RSA -------")
# Numere pe 700 de biti
p = sympy.nextprime(random.getrandbits(700))
q = sympy.nextprime(random.getrandbits(700))
r = sympy.nextprime(random.getrandbits(700))
# Numere mici
# p = 3
# q = 5
# r = 7


print("\n------- Initializare -------")


if verificare_pqr(p, q, r) == True:
    print("\nP, Q, R au fost generate corect.")
else:
    print("\nP, Q, R nu au fost generate corect.")


print("\np =", p)
print("\nq =", q)
print("\nr =", r)


n = get_n(p, q, r)
print("\nn =", n)


phi_n = phi(p, q, r)
print("\nphi(n) =", phi_n)


# Numar pe 17 biti0
e = random.getrandbits(17)
# Numar mic
# e = 5
print("\ne =", e)


d = invers_modular(e, phi_n)
print("\nd =", d)


# un numar prim n
x = n -100  
print("\nx =", x)


# print("y = enc(x) =", encryption())
y = exp_modulara(x, e, n)
print("\ny =", y)


# calcul_tcr_fermat_imp, timp_x_imp, calcul_tcr_fermat_lib, timp_x_lib = tcr_fermat(p, q, r, n, d, y)
# print("\n------- Fermat cu exp mod implementata -------")
# print("Rezultat TCR-FERMAT implementat:", calcul_tcr_fermat_imp)
# print("Timp rulare TCR_FERMAT implementat:", timp_x_imp)

# print("\n------- Fermat cu exp mod din librarie -------")
# print("Rezultat TCR-FERMAT librarie:", calcul_tcr_fermat_lib)
# print("Timp rulare TCR_FERMAT librarie:", timp_x_lib)


print("\n------- Garner cu exp mod implementata -------")
calcul_tcr_garner_imp, timp_x_imp = tcr_garner(p, q, r, n, d, y)
print("Rezultat TCR-GARNER implementat:", calcul_tcr_garner_imp)
print("Timp rulare TCR_GARNER implementat:", timp_x_imp)

print("\n------- Exponentiere modula librarie -------")
start = time.time()
exp_mod_rez = exp_modulara_lib(y, d, n)
finish = time.time()

# Timpul final x_lib
timp_x_lib = finish - start

print("Rezultat Exp mod lib:", exp_mod_rez)
print("Timp rulare Exp mod lib:", timp_x_lib)


if timp_x_imp > timp_x_lib:
    print("\nGarner implementat este mai bun")
else:
    print("\nGarner cu librarie este mai bun")