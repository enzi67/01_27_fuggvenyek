"""
5.1 Feladat
A "Próbáld ki!" gombra kattintva elérhető egy program, ami egy eljárás segítségével kirajzol a képernyőre egy 6x3-as mezőt.
Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott pozícióba
'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)

    O O O O + O
    O O O O O O
    O O O O O O
  
"""

def mezot_rajzol(sor, oszlop):
    mező = [['O' for vmi in range(6)] for sumn in range(3)]
    
    mező[sor][oszlop] = '+'
    
    for sor in mező:
        print(' '.join(sor))

mezot_rajzol(1, 1)
