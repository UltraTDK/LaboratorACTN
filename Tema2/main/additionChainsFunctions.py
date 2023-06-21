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


def calcul_additionChains(p, q, r, n, d, y):

    # Timpul de start
    start = time.time()
    x_p = exp_modulara(y, d % (p - 1), p)
    x_q = exp_modulara(y, d % (q - 1), q)
    x_r = exp_modulara(y, d % (r - 1), r)

    x1 = exp_modulara(q * r * x_p, (d % ((p - 1) * (q - 1))) % ((p - 1) * (q - 1) - 1), n)
    x2 = exp_modulara(p * r * x_q, (d % ((q - 1) * (r - 1))) % ((q - 1) * (r - 1) - 1), n)
    x3 = exp_modulara(p * q * x_r, (d % ((r - 1) * (p - 1))) % ((r - 1) * (p - 1) - 1), n)

    x = x1 + x2 + x3

    # Timpul de finish
    finish = time.time()

    return x, (finish - start)