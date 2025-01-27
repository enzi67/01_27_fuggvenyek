"""
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja,
hogy negatív, pozitív vagy nulla-e!
"""
def elso_feladat():

    if szam > 0:
        print("Pozitív")
    elif szam < 0:
        print("Negatív")
    else:
        print("Nulla vagy nincs megoldás.")
        
szam = int(input("Adj meg egy számot: "))

elso_feladat()