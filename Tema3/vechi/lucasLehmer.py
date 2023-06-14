import time

def reducere_modulara_lib(s, p):
    """
    Computes x modulo p using modular reduction formula.
    """
    return s - p * (s // p)


def reducere_modulara(s, p):
    """
    Reducere modulara
    """

    s1 = s // p


    s0 = s % p


    if s1 + s0 == p:
        return 0
    elif s1 + s0 < p:
        return s1 + s0
    else:
        return s1 + s0 - p


def lucas_lehmer(nr):
    """
    Test primalitate Lucas-Lehmer folosind reducere modulara
    pentru numere Mersenne

    nr: numarul pentru care se face testul de primalitate
    """

    start = time.time()
    # initializarea secventei Lucas-Lehmer
    s = 4


    # calcul constanta reducerii modulare
    mrsn = 2 ** nr - 1


    #  realizez n - 2 iteratii 
    for _ in range(nr - 2):
        s = reducere_modulara(s * s - 2, mrsn)


    # Verificare primalitate
    if s == 0:
        print(" este numar Mersenne prim.")
    else:
        print(" este numar Mersenne compus.")

    final = time.time()

    print("\nLucas-Lehmer:", final - start)



def lucas_lehmer_lib(nr):
    """
    Test primalitate Lucas-Lehmer folosind reducere modulara
    pentru numere Mersenne

    nr: numarul pentru care se face testul de primalitate
    """

    start = time.time()
    # initializarea secventei Lucas-Lehmer
    s = 4


    # calcul constanta reducerii modulare
    mrsn = 2 ** nr - 1


    #  realizez n - 2 iteratii 
    for _ in range(nr - 2):
        s = reducere_modulara_lib(s * s - 2, mrsn)


    # Verificare primalitate
    if s == 0:
        print(" este numar Mersenne prim.")
    else:
        print(" este numar Mersenne compus.")

    final = time.time()

    print("\nLucas-Lehmer cu librarie:", final - start)
