data = [3, 5, 13, 55, 44, 75, 21, 54, 43, 53, 11, 111, 223, 12312]


def mediana(x):
    s = sorted(x)
    if (int(len(s))) % 2 != 0:
        print(s[int((int(len(s)) - 1)/2)])
    elif (int(len(s))) % 2 == 0:
        print((s[int((int(len(s))/2-1))] + s[int(int(len(s))/2)])/2)

mediana(data)
