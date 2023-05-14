# Algoritm dezvoltat de:
# Ciobotariu Andrei & Nedelcu Denis


def extendedBinary(a, b):
    r = []
    s = []
    q = [0]
    r.append(a)
    r.append(b)
    s.append(1)
    s.append(0)
    i = 1


    while r[i] > 0:
        q.append(r[i - 1] // r[i])
        print("Q[", i, "] = ", q[i], sep='')
        r.append(r[i - 1] - (q[i] * r[i]))
        print("R[", i + 1, "] = ", r[i + 1], sep='')
        s.append(s[i - 1] - (q[i] * s[i]))
        print("S[", i + 1, "] = ", s[i + 1], sep='')
        i += 1


    if i % 2 == 0:
        print("i - par")
        print("Rezultat:", b - abs(s[i - 1]))
        
    else:
        print("i - impar")
        print("Rezultat:", abs(s[i - 1]))
        

    print("Verificare:", pow(a, -1, b))