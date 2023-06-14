import random


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


def mod_inv(a, m):
    """Calcul invers modular"""
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1, u2 - q * v2, u3 - q * v3, v1, v2, v3)
    return u1 % m


def find_primitive_root(p):
    """Gasirea unei radacini primitive"""
    factors = []
    phi = p - 1
    n = phi
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.append(n)
    for alpha in range(2, p):
        is_primitive = True
        for factor in factors:
            if pow(alpha, phi // factor, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            return alpha
    return None


def shanks_algorithm(p, alpha, beta):
    """Compute logarithm modulo p to the base alpha of beta using Shanks algorithm"""
    m = int(p**0.5) + 1
    table = {pow(alpha, j, p): j for j in range(m)}
    gamma = pow(alpha, m * (p - 2), p)
    y = beta
    for i in range(m):
        if y in table:
            return i * m + table[y]
        y = (y * gamma) % p
    return None


# Example usage:
p = generate_prime()
alpha = find_primitive_root(p)
beta = random.randint(1, p - 1)
log_beta_alpha = shanks_algorithm(p, alpha, beta)
print(f"p = {p}")
print(f"alpha = {alpha}")
print(f"beta = {beta}")
print(f"log_{alpha}({beta}) = {log_beta_alpha}")
