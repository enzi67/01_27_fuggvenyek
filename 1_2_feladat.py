"""
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja,
hogy negatív, pozitív vagy nulla-e!
"""
def elso_feladat():

    szam = int(input("Adj meg egy számot: "))

    if szam > 0:
        print("Pozitiv")
    elif szam < 0:
        print("Negativ")
    else:
        print("Nulla avyg nincs megoldás.")

elso_feladat()