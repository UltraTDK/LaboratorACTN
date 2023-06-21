import random


# Aceasta tema nu este completa si trebuie revizuita si terminata


def is_prime(n):
    """Verificare primalitate"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_prime():
    """Generare numar prim pe 32 bits"""
    while True:
        p = random.randint(2**31, 2**32 - 1)
        if is_prime(p):
            return p


def gcd(a, b):
    """Calcul cmmdc"""
    while b:
        a, b = b, a % b
    return a


def shanks_algorithm(p, alpha, beta):
    """Calcul folosid Algoritmul lui Shanks"""
    m = int(p**0.5) + 1
    table = {pow(alpha, j, p): j for j in range(m)}
    gamma = pow(alpha, m * (p - 2), p)
    y = beta
    for i in range(m):
        if y in table:
            return i * m + table[y]
        y = (y * gamma) % p
    return None
