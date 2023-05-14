import random
import sympy
from additionChainsFunctions import *


print("------- Lanturi Aditive -------")
# Numere pe 700 de biti
p = sympy.nextprime(random.getrandbits(700))
q = sympy.nextprime(random.getrandbits(700))
r = sympy.nextprime(random.getrandbits(700))
# Numere mici
# p = 3
# q = 5
# r = 7


if verificare_pqr(p, q, r) == True:
    print("P, Q, R au fost generate corect.")
else:
    print("P, Q, R nu au fost generate corect.")


print("p =", p)
print("q =", q)
print("r =", r)


n = get_n(p, q, r)
print("n =", n)


phi_n = phi(p, q, r)
print("phi(n) =", phi_n)


# Numar pe 17 biti
e = random.getrandbits(17)
# Numar mic
# e = 5
print("e =", e)


d = invers_modular(e, phi_n)
print("d =", d)


# un numar prim n
x = sympy.prime(30)  


# print("y = enc(x) =", encryption())
y = exp_modulara(x, e, n)


calcul_lant_aditiv, timp = calcul_additionChains(p, q, r, n, d, y)
print("Rezultat Lant Aditiv:", calcul_lant_aditiv)
print("Timp rulare Lant Aditiv:", timp)