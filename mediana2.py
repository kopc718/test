data = [3, 5, 13, 55, 44, 75, 21, 54, 43, 53, 11, 111, 223, 12312]


def mediana(x):
    s = sorted(x)
    if (len(s)) % 2 != 0:
        print(s[(len(s) - 1)/2])
    elif (len(s)) % 2 == 0:
        print((s[len(s)//2-1] + s[len(s)//2])/2)

mediana(data)
