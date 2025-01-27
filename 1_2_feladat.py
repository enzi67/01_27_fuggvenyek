"""
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja,
hogy negatív, pozitív vagy nulla-e és addig lehessen számokat megadni,
amíg a felhasználó nem ad meg üres sztringet!
"""

def masodik_feladat(szam):
    if szam > 0:
        print("A szám pozitív.")
    elif szam < 0:
        print("A szám negatív.")
    else:
        print("A szám nulla.")

def main():
    while True:
        num = input("Adj meg egy számot: ")

        if num == '':
            break
        
        try:
            szam = float(num)
            masodik_feladat(szam)
        except ValueError:
            print("Hibás bemenet! Kérlek, adj meg egy számot!")

main()