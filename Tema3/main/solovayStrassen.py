import random


def exp_modulara(a, e, m):
    """
    Formula:
        enc(x) = a ^ e mod m
    """
    return pow(a, e, m)


def jacobi(a, n):
    """
    Simbolul Jacobi: (a / n)

    Reguli de calcul:
    1. daca a = 1, (a / n) = 1
    2. daca a = 0, (a / n) = 0
    3. daca a - par, (a / n) = (2 / n) * (a / 2)
    4. daca a - impar, (a / n) = (-1)^((n - i) / 2 * (a - i) / 2) * (n / a),
       n mod 8 apartine {3,5}
    5. (a / n) = (m / n) daca a mod 4 = 1, -(m / n) daca a mod 4 = 3
    """

    if n % 2 == 0:
        raise ValueError("n trebuie sa fie un numar impar pozitiv")
    
    jcb = 1
    
    # regula 1
    if a == 1:
        return 1


    # regula 2
    if a == 0:
        return 0


    while a != 0:
        # cand a este multiplu de 2
        while a % 2 == 0:
            a //= 2
            if n % 8 == 3 or n % 8 == 5:
                jcb *= -1

        if a < 0:
            a *= -1
            if n % 4 == 3:
                jcb *= -1

        if a < n:
            a = n
            n = a
        
        # regula 5: reciprocitate
        if a % 4 == 3 and n % 4 == 3:
            jcb *= -1

        # reducere
        a %= n

        if a > n // 2:
            a -= n

    if n == 1:
        return jcb
    else:
        return 0
                

def solovay_strassen(n, t):
    """
    Test probabilistic de primalitate Solovay-Strassen
    Acuratete:
        daca n este prim, atunci rezultatul 'prim' poate fi corect
        daca n este compus, atunci rezultatul 'prim' poate fi gresit
    unde n este numit pseudo-prim Euler-Jacobi

    n - numar impar intreg >= 3
    t - numarul de iteratii >= 1
    """

    prim = 1
    for _ in range(t):
        a = random.randint(2, n - 1)
        jcb = (n + jacobi(a, n)) % n

        if jcb == 0 or exp_modulara(a, int((n - 1) / 2), n) != jcb:
            prim = 0
    
    
    if prim == 1:
        print(" este prim")
    else:
        print(" nu este prim")