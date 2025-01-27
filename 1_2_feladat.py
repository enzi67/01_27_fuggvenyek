"""
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja,
hogy negatív, pozitív vagy nulla-e és addig lehessen számokat megadni,
amíg a felhasználó nem ad meg üres sztringet!
"""

def masodik_feladat(num):

    if num > 0:
        print("Pozitív")
    elif num < 0:
        print("Negatív")
    else:
        print("Nulla vagy nincs megoldás.")
        
num = int(input("Adj meg egy számot: "))

run = True

while run:
    num = int(input("Adj meg egy számot: "))
    if num == " ":
        run = False
        break

masodik_feladat(num)