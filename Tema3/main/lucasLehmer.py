import sympy


def lucas_lehmer(p):
    """
    Test de primalitate Lucas-Lehmer pentru numere Mersenne
    Reguli:
        daca 2^p - 1 este prim, returnez True
        altfel, returnez False
    """
    # cazul de baza: verific daca p este prim
    if sympy.isprime(p):
        return False

    # initializarea secventei cu s=4
    s = 4

    # initializare numar Mersenne
    m = (1 << p) - 1

    for _ in range(2, p + 1):
        s = reducere_modulara(s * s - 2, m)

    # daca s == 0, 2^p - 1 este prim
    return s == 0


def reducere_modulara(s, p):
    if s < p:
        return s % p
    else:
        return reducere_modulara(s - p, p)
