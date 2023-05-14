import string
import numpy as np 


# Pasul de initializare
# in acest pas verific daca baza si p sunt numere prime
def is_prime(numar):
    if numar >= 2:  
        for index in range(3, numar // 2, 2):  
            print(index)
            if (numar % index) == 0:  
                return False
        return True
    else:
        return False


# Pasul de codificare
def modulo_p(numar, p):
    # parametrul1: numar
    # parametrul2: un numar prim p din Zp
    # rezultat: numar modulo p

    return numar % p


# cifre + litere
cif_lit = string.digits + string.ascii_letters
def conversie_baza_x(mesaj, baza):
    # parametrul1: mesajul pe care il convertim
    # parametrul2: baza in care transformam
    # rezultat: mesajul de tip int in baza x

    if int(mesaj) < 0:
        semn = -1
    elif int(mesaj) == 0:
        return cif_lit[0]
    else:
        semn = 1

    mesaj *= semn
    cifre = []

    while mesaj:
        cifre.append(cif_lit[(int(mesaj % baza)) % len(cif_lit)])
        mesaj = int(mesaj / baza)

    if semn < 0:
        cifre.append('-')

    cifre.reverse()
    return cifre


# cifre: 0-9
# literele mici: 10-35
# litere mari: 36-62
def vector_mesaj(mesaj):
    # parametrul1: mesajul pe care il convertim
    # rezultat: vectorul mesaj

    rezultat = []
    for caracter in mesaj:
        if caracter >= '0' and caracter <= '9':
            rezultat.append(int(caracter))
        elif caracter >= 'a' and caracter <= 'z':
            # char - 87: pt a fi in intervalul (10-35)
            rezultat.append(ord(caracter) - 87) 
        elif caracter >= 'A' and caracter <= 'Z':
            # char - 29: pt a fi in intervalul (36-62)
            rezultat.append(ord(caracter) - 29) 

    return rezultat


def horner(mesaj, baza):
    # parametrul1: mesajul 
    # parametrul2: baza
    # rezultat: horner aplicat pe mesaj

    rezultat = 0
    for i in range(0, len(baza)):
        rezultat = baza[i] + (mesaj * rezultat)
    return rezultat


# Pasul de decodificare
def calcul_coeficient_liber(combinatii):
    # parametrul1: combinatiile pozitiilor fara eroare luate cate k
    # rezultat: combinatiile care au cel putin o suma egala cu 0

    coeficient_liber = []
    for i in range(len(combinatii)):
        suma = 0
        for j in range(i, len(combinatii)):
            suma += sum(np.subtract(combinatii[i], combinatii[j]))
            if suma == 0:
                coeficient_liber.append(suma)
                break
    return coeficient_liber


def reconstructie_polinom(polinom, z, baza):
    polinom_reconstruit = []
    inverse = []
    
    for i in polinom:
        p_x = []
        inversa = 1
        for j in polinom:
            if j != i:
                inversa *= pow(i - j, -1, baza)
                x = [1, - j]
                p_x.append(x)
            inverse.append(inversa)
        polinom_reconstruit.append(p_x)

    inverse_z_i = []
    for index, i in enumerate(polinom):
        inverse_z_i.append(modulo_p((inverse[index] * z[i-1]), baza))

    print("P(x): ", polinom_reconstruit)
    print("\nInversa: ", inverse_z_i)

    inm_pol = []
    for lista in polinom_reconstruit:
        lista_curenta = lista.copy()
        pol_final = modulo_p(np.polymul(lista_curenta[0], lista_curenta[1]), baza)
        inm_pol.append(pol_final)

    print("\nPolinom inm: ", inm_pol)

    rez_final = []
    for i in range(len(inm_pol)):
        produs = modulo_p((inm_pol[i] * inverse_z_i[i]), baza)
        rez_final.append(produs)

    print("\nRezultat: ", rez_final)

    adunare = sum(map(np.array, rez_final))
    print(adunare)
    for i in adunare:
        print(i%baza)

    return polinom_reconstruit



# verificare - i1: 7, i2: 8, i3: 9


# polinom_decodificat = []
#     for i in range(len(polinom_reconstruit)-1):
#         polinom_decodificat.append(polinom_reconstruit[i])