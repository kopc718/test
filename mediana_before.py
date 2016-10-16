dane = [3, 5, 13, 55, 44, 75, 21, 54, 43, 53, 11, 111, 223, 12312]


def mediana(x):

    s = sorted(x)
    w = int(len(s))
    if w % 2 != 0:
        f = int((w - 1)/2)
        d = s[f]
        print(d)
    elif w % 2 == 0:
        f = int((w/2-1))
        g = int(w/2)
        d = (s[f] + s[g])/2
        print(d)

mediana(dane)
