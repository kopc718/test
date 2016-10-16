#Dany jest ciąg imion uczestników pewnej grupy. Napisz
#program, który przeanalizuje zawartość spisu, tak by po jednokrotnym
#przejrzeniu znać listy mieć zbudowaną listę imion o maksymalnej liczbie
#6 znaków. Wskazówka: Założyć pustą listę na wyniki. Przeglądać spis za pomocą
#instrukcji for. Jeżeli dane imię jest dłuższe niż najdłuższe dotychczas
#spotkane, zapamiętać je i opróżnić listę wynikową. Następnie jeżeli
#dane imię jest tak długie jak najdłuższe dotychczas spotkane, dołączyć je
#do listy; w przeciwnym razie nic nie robić.

imiona = ["jarekkk", "pawel", "jagoda", "maksymilian", "bartosz", "bartlomiej", "tomasz", "euwenilia"]



x = len(imiona)
print(len(imiona))
l = []

while x > 0:
    x -= 1
    print(x)
    if len(imiona[x]) >= 6:
        l.append(imiona[x])
    elif len(imiona[x]) < 6:
        continue
print(l)
