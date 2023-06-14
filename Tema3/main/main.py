import sympy
from solovayStrassen import *
from lucasLehmer import *


print("------- Solovay-Strassen -------")
n = 5
n_mare = sympy.nextprime(random.getrandbits(100))
# print("\nn =", n)
# solovay_strassen(n, 100)
print("\nn =", n)
if solovay_strassen(n, 20) == True:
    print(n, "este prim.")
else:
    print(n, "este compus.")


print("\n------- Lucas-Lehmer -------")
nr = 6
nr_mare = sympy.nextprime(random.getrandbits(10))
print("\nnr:", nr)
if lucas_lehmer(nr):
    print(nr, "este prim.")
else:
    print(nr, "este compus.")

# print("\n------- Lucas-Lehmer cu librarie -------")
# print("\nnumarul:", nr)
# lucas_lehmer_lib(nr)
