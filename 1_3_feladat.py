"""
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza,
és a képernyőre kiírja, melyik a legrövidebb szó!
"""

def longest_word(words):
    shortest = min(words, key=len)
    print(f"A legrövidebb szó: {shortest}")

words = []
for db in range(3):
    szó = input(f"Add meg a {db+1}. szót: ")
    words.append(szó)

longest_word(words)