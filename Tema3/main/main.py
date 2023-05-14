import sympy
from solovayStrassen import *
from lucasLehmer import *


print("------- Solovay-Strassen -------")
n = 5
n_mare = sympy.nextprime(random.getrandbits(100))
# print("\nn =", n)
# solovay_strassen(n, 100)
print("\nn =", n)
solovay_strassen(n, 20)


print("\n------- Lucas-Lehmer -------")
nr = 5
nr_mare = sympy.nextprime(random.getrandbits(10))
print("\nnumarul:", nr)
lucas_lehmer(nr)


print("\n------- Lucas-Lehmer cu librarie -------")
print("\nnumarul:", nr)
lucas_lehmer_lib(nr)