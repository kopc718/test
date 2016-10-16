import random


class GRA(object):

    def __init__(self, name="", score_g1 = [], score_g2 = []):
        self.name = name
        self.score_g1 = list(score_g1)
        self.score_g2 = list(score_g2)

    def rename(self):
        self.name = input("")

    def introduce(self):
        return self.name

    def throw(self):

        while True:
            rzut = []

            f = [1, 2, 3, 4, 5, 6]
            r = (random.choice(f))
            t = (random.choice(f))

            if True:
                rzut.append(r)

            if True:
                rzut.append(t)

            print("Gracz ", self.name, " wyrzucil ", rzut[0], " i ", rzut[1])

            if self.name == gracz1.introduce():
                self.score_g1.append(rzut[0])
                self.score_g1.append(rzut[1])
            elif self.name == gracz2.introduce():
                self.score_g2.append(rzut[0])
                self.score_g2.append(rzut[1])

            break

    def results(self):
        a = len(gracz1.score_g1)
        b = len(gracz2.score_g2)

        if a == b:
            ru = int((len(gracz1.score_g1))/2)

            print("             ", gracz1.introduce(), "      ", gracz2.introduce())
            for i in range(1, ru):
                if i < 10:
                    print("Gra ", i, "    ", gracz1.score_g1[i - 1], " , ", gracz1.score_g1[i], "     ",
                          gracz2.score_g2[i - 1], " , ", gracz2.score_g2[i])
                elif 10 <= i < 100:
                    print("Gra ", i, "   ", gracz1.score_g1[i - 1], " , ", gracz1.score_g1[i], "     ",
                          gracz2.score_g2[i - 1], " , ", gracz2.score_g2[i])
                elif i >= 100:
                    print("Gra ", i, "  ", gracz1.score_g1[i - 1], " , ", gracz1.score_g1[i], "     ",
                          gracz2.score_g2[i - 1], " , ", gracz2.score_g2[i])

        elif a != b:
            print("Ilosc rzutow nierowna, wcisnij enter by gracz", gracz2.introduce(), "rzucil/la")

        print("\n")
        p1 = sum(gracz1.score_g1)
        p2 = sum(gracz2.score_g2)
        g1w = p1 - p2
        g2w = p2 - p1

        print(gracz1.introduce(), " ", p1, " pkt.")
        print(gracz2.introduce(), " ", p2, " pkt.")

        if p1 > p2:
            print(gracz1.introduce(), " prowadzi przewaga", g1w)
        elif p2 > p1:
            print(gracz2.introduce(), " prowadzi przewaga", g2w)
        elif p2 == p1:
            print("jest remis", p1, " do ", p2)

        print("   ")
        input("Wcisnij enter by wrocic do gry")

    def play(self):
        print("Podaj nazwe gracza 1: ")
        gracz1.rename()
        print("Podaj nazwe gracza 2: ")
        gracz2.rename()

        while True:
            a = len(gracz1.score_g1)
            b = len(gracz2.score_g2)
            run = b/2

            print("Runda: ", int(run+1))
            if a < b or a == b:

                print("Rzuca ", gracz1.introduce())
                gracz1.throw()
                d = input("wcisnij enter by rzucic lub wpisz tab by zobaczyc tablice wynikow: ")
                if d == "":
                    continue
                elif d == "tab":
                    gracz1.results()
            elif a > b:
                print("Rzuca ", gracz2.introduce())
                gracz2.throw()
                d = input("wcisnij enter by rzucic lub wpisz tab by zobaczyc tablice wynikow: ")
                if d == "":
                    continue
                elif d == "tab":
                    gracz1.results()


gracz1 = GRA()
gracz2 = GRA()


gracz1.play()
