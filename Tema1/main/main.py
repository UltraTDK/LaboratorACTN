import random
from functions import *
import sympy
import random


print("------- Pasul 1: initializare -------")


# initializare input
input = 29
print("Input:", input)


# initializare p 
baza_random = sympy.nextprime(random.getrandbits(161))
p = baza = 11
print("baza:", baza)


# # initializare naiva pentru p
# baza_random = random.randint(2, 11)
# verificare_primalitate = False
# while verificare_primalitate != True:
#     if is_prime(baza_random):
#         verificare_primalitate = True
#     else:
#         baza_random = random.randint(2, 11)