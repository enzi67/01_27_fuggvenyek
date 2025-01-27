"""
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja,
hogy negatív, pozitív vagy nulla-e!
"""
def elso_feladat(num):

    if num > 0:
        print("Pozitív")
    elif num < 0:
        print("Negatív")
    else:
        print("Nulla vagy nincs megoldás.")
        
num = int(input("Adj meg egy számot: "))

elso_feladat(num)