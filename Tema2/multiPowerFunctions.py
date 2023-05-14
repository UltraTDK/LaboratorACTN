import time
import sympy as sp


def verificare_pq(p, q):
    """
    Verificare primalitate si daca p, q sunt distincte
    """
    if p != q and sp.isprime(p) and sp.isprime(q):
        return True
    return False


def get_n(p, q):
    return p * p * q


def phi(p, q):
    """
    Formula phi:
        phi(n) = (p-1) * (q-1) * p
    """
    return (p**2 - p) * (q - 1)


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


def tcr_hensel(p, q, n, e, d, y):

    ########## Implementat ##########
    # Timpul de start
    start = time.time()

    x_q = exp_modulara_lib(y % q, d % (q - 1), q)

    # Hensel imp
    x0 = exp_modulara_lib(y % p, d % (p - 1), p)
    alpha = ((y - exp_modulara_lib(x0, e, p * p)) // p)
    x1 = (alpha * invers_modular(e * exp_modulara_lib(x0, e - 1, p * p), p)) % p

    x_p = int((x1 * p + x0) % (p * p))

    x1 = sp.mod_inverse(q, p * p)
    x2 = sp.mod_inverse(p * p, q)
    x_imp = ((x_p * x1 * q) + (x_q * x2 * (p * p))) % n

    # Timpul de finish
    finish = time.time()

    # Timpul final x_implementat
    timp_x_imp = finish - start

    return x_imp, timp_x_imp
