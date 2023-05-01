import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
valeurcarte = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "J": 10, "Q": 11, "K": 12,
               "A": 13}
liste1 = []
liste2 = []

n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    liste1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    liste2.append(cardp_2)

tour = 0
cartenjeu1 = []
cartenjeu2 = []
pat = False

while True:

    tour += 1

    carte1 = liste1[0]
    carte2 = liste2[0]
    cartenjeu1.append(carte1)
    cartenjeu2.append(carte2)
    if len(liste1[0]) == 3:
        carte1tempo = liste1[0]
        carte1 = ''
        for i in carte1tempo:
            carte1 = carte1 + i
            if len(carte1) == 2:
                break
    else:
        carte1 = liste1[0][0]

    if len(liste2[0]) == 3:
        carte2tempo = liste2[0]
        carte2 = ''
        for i in carte2tempo:
            carte2 = carte2 + i
            if len(carte2) == 2:
                break
    else:
        carte2 = liste2[0][0]

    liste1.pop(0)
    liste2.pop(0)

    if valeurcarte[carte1] < valeurcarte[carte2]:
        for i in cartenjeu1:
            liste2.append(i)
        for i in cartenjeu2:
            liste2.append(i)
        cartenjeu1 = []
        cartenjeu2 = []
        if len(liste1) == 0:
            gagnant = 2
            break

    if valeurcarte[carte1] > valeurcarte[carte2]:
        for i in cartenjeu1:
            liste1.append(i)
        for i in cartenjeu2:
            liste1.append(i)
        cartenjeu1 = []
        cartenjeu2 = []
        if len(liste2) == 0:
            gagnant = 1
            break

    if valeurcarte[carte1] == valeurcarte[carte2]:
        if len(liste1) >= 4:
            if len(liste2) >= 4:
                cartenjeu1.append(liste1[0])
                cartenjeu1.append(liste1[1])
                cartenjeu1.append(liste1[2])
                cartenjeu2.append(liste2[0])
                cartenjeu2.append(liste2[1])
                cartenjeu2.append(liste2[2])
                liste1.pop(0)
                liste1.pop(0)
                liste1.pop(0)
                liste2.pop(0)
                liste2.pop(0)
                liste2.pop(0)
                tour = tour - 1
            else:
                gagnant = 'PAT'
                pat = True
                break
        else:
            gagnant = 'PAT'
            pat = True
            break
if pat:
    print(gagnant)
else:
    print(gagnant, tour)