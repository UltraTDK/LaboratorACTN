import random
import sympy
from multiPowerFunctions import *


print("------- MULTI-POWER RSA -------")
# Numere pe 700 de biti
p = sympy.nextprime(random.getrandbits(700))
q = sympy.nextprime(random.getrandbits(700))
# Numere mici
# p = 3
# q = 5


print("\n------- Initializare -------")


if verificare_pq(p, q) == True:
    print("\nP, Q au fost generate corect.")
else:
    print("\nP, Q nu au fost generate corect.")


print("\np =", p)
print("\nq =", q)


n = get_n(p, q)
print("\nn =", n)


phi_n = phi(p, q)
print("\nphi(n) =", phi_n)


# Numar pe 17 biti
e = random.getrandbits(17)
# Numar mic
# e = 5
print("\ne =", e)


d = invers_modular(e, phi_n)
print("\nd =", d)


# un numar prim n
x = sympy.prime(10)  


# print("y = enc(x) =", encryption())
y = exp_modulara(x, e, n)


calcul_tcr_x_imp, timp_x_imp = tcr_hensel(p, q, n, e, d, y)
print("\n------- Hensel cu exp mod implementata -------")
print("Rezultat TCR-HENSEL implementat:", calcul_tcr_x_imp)
print("Timp rulare TCR-HENSEL implementat:", timp_x_imp)

# print("\n------- Hensel cu exp mod din librarie -------")
# print("Rezultat TCR-HENSEL librarie:", calcul_tcr_x_imp)
# print("Timp rulare TCR-HENSEL librarie:", timp_x_imp)

print("\n------- Exponentiere modula librarie -------")
start = time.time()
exp_mod_rez = exp_modulara_lib(y, d, n)
finish = time.time()

# Timpul final x_lib
timp_x_lib = finish - start

print("Rezultat Exp mod lib:", exp_mod_rez)
print("Timp rulare Exp mod lib:", timp_x_lib)


if timp_x_imp > timp_x_lib:
    print("\nHensel TCR este mai bun")
else:
    print("\nExponentierea modulara este mai buna")
