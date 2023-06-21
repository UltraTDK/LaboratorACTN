import time
import sympy as sp


def verificare_pqr(p, q, r):
    """
    Verificare primalitate si daca p, q, r sunt distincte
    """
    if p != q != r and sp.isprime(p) and sp.isprime(q) and sp.isprime(r):
        return True
    return False


def phi(p, q, r):
    """
    Formula phi:
        phi(n) = (p-1) * (q-1) * (r-1)
    """
    return (p - 1) * (q - 1) * (r - 1)


def get_n(p, q, r):
    """
    Formula n: n = pqr, 
        unde p, q si r sunt numere prime distincte pe 700 de biti
    """
    return p * q * r


def exp_modulara_lib(a, e, m):
    """
    Formula criptare:
        criptare(x) = a^e mod m
        Criptarea are loc folosind 'Exponentierea Modulara'
        Varianta mai simpla folosind pow din python
    """
    return pow(a, e, m)


def exp_modulara(a, e, m):
    """
    Formula:
        enc(x) = a ^ e mod m
    """

    rezultat = 1
    while e > 0:
        if e % 2 == 1:
            rezultat = (rezultat * a) % m
        e = e // 2
        a = (a * a) % m
    return rezultat


def invers_modular(a, m):
    """
    Formula invers modular:
        a * x = 1 (mod m)
        x - necunoscuta
    """
    x = sp.mod_inverse(a, m)
    return x


def tcr_fermat(p, q, r, n, d, y):
    """
    Teorema Chineza a Resturilor folosind:
        exponentiere modulara
        inversul modular
    """

    ########## Implementat ##########
    # Timpul de start
    start = time.time()

    # FERMAT imp
    x_p = exp_modulara(y % p, d % (p - 1), p)
    x_q = exp_modulara(y % q, d % (q - 1), q)
    x_r = exp_modulara(y % r, d % (r - 1), r)

    x1 = invers_modular(n // p, p)
    x2 = invers_modular(n // q, q)
    x3 = invers_modular(n // r, r)

    # calcul TCR
    x_implementat = ((x_p * x1 * (n // p)) + (x_q * x2 * (n // q)) + (x_r * x3 * (n // r))) % n

    # Timpul de finish
    finish = time.time()

    # Timpul final x_implementat
    timp_x_imp = finish - start


    ########## Librarie ##########
    # Timpul de start
    start = time.time()
    
    # Fermat lib
    x_p = exp_modulara_lib(y % p, d % (p - 1), p)
    x_q = exp_modulara_lib(y % q, d % (q - 1), q)
    x_r = exp_modulara_lib(y % r, d % (r - 1), r)

     # calcul TCR
    x_lib = ((x_p * x1 * (n // p)) + (x_q * x2 * (n // q)) + (x_r * x3 * (n // r))) % n

    # Timpul de finish
    finish = time.time()

    # Timpul final x_lib
    timp_x_lib = finish - start

    return x_implementat, timp_x_imp, x_lib, timp_x_lib


def tcr_garner(p, q, r, n, d, y):
    """
    Teorema Chineza a Resturilor folosind:
        exponentiere modulara
    """
    
    ########## Implementat ##########
    # Timpul de start
    start = time.time()
    # GARNER imp
    x_p = exp_modulara_lib(y % p, d % (p - 1), p)
    x_q = exp_modulara_lib(y % q, d % (q - 1), q)
    x_r = exp_modulara_lib(y % r, d % (r - 1), r)

    x1 = x_p
    alpha = ((x_q - x1) * invers_modular(p, x_r)) % x_r
    x2 = x1 + alpha * p
    alpha = ((x_q - x2) * invers_modular(p * r, x_q)) % x_q
    x_imp = x2 + alpha * p * q

    # Timpul de finish
    finish = time.time()

    # Timpul final x_implementat
    timp_x_imp = finish - start


    ########## Librarie ##########
    # Timpul de start
    start = time.time()

    return x_imp, timp_x_imp
