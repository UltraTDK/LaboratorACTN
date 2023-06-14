import random


def jacobi_symbol(a, n):
    """
       Jacobi Symbol = (a/n)
       Calcul Jacobi Symbol folosind proprietatile specifice
    si legea reciprocitatii.
    """
    # regula in care: a = 1
    if n == 1:
        return 1

    rez = 1
    while a != 0:
        # regula in care: a este par
        while a % 2 == 0:
            a /= 2
            if n % 8 == 3 or n % 8 == 5:
                rez = -rez

        a, n = n, a
        # regula in care: a mod 4 = 3
        if a % 4 == 3 and n % 4 == 3:
            rez = -rez
        a %= n

    # verificare
    # print("Test Jacobi:", rez)

    if n == 1:
        return rez
    else:
        return 0


def solovay_strassen(n, k=10):
    """
       Test de primalitate Solovay Strassen folosind Jacobi Symbol
    pentru calculul simbolului Legendre pentru un numar random 'a'.
    """
    # cazul de baza
    if n == 2 or n == 3:
        return True
    # cazul in care numarul este par sau mai mic decat 2
    if n < 2 or n % 2 == 0:
        return False

    for _ in range(k):
        # a luat random
        a = random.randint(2, n - 1)
        # calcul Jacobi Symbol
        x = jacobi_symbol(a, n)
        # calcul Legendre folosing exponentierea modulara
        y = pow(a, (n - 1) // 2, n)
        if x == 0 or y != x % n:
            return False

    return True
