import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
p1 = []
p2 = []
print(len(p1), file=sys.stderr)
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    p1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    p2.append(cardp_2)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
print("p1 : {}".format(p1), file=sys.stderr)
print("p2 : {}".format(p2), file=sys.stderr)

nbTurn = 0
pat = False
while len(p1) > 0 and len(p2) > 0:
    asidep1 = [p1[0]]
    asidep2 = [p2[0]]
    del p1[0]
    del p2[0]

    # BATAILLE :
    # Tant qu'il n'y a pas de superiorité et que tout le monde peut jouer
    while len(p1) > 0 and len(p2) > 0 and asidep1[-1][:-1] == asidep2[-1][:-1]:
        for i in range(4):
            if (len(p1) == 0 or len(p2) ==  0):
                pat = True
                break
            asidep1.append(p1[0])
            asidep2.append(p2[0])
            del p1[0]
            del p2[0]

    if VALUES.index(asidep1[-1][:-1]) > VALUES.index(asidep2[-1][:-1]):
        p1.extend(asidep1)
        p1.extend(asidep2)
    else:
        p2.extend(asidep1)
        p2.extend(asidep2)
    nbTurn += 1
    print("---{}---".format(nbTurn), file=sys.stderr)
    print("p1 : {}".format(p1), file=sys.stderr)
    print("p2 : {}".format(p2), file=sys.stderr)
    if pat:
        break

if pat:
    print("PAT")
elif len(p2) == 0:
    print("1 {}".format(nbTurn))
elif len(p1) == 0 and not pat:
    print("2 {}".format(nbTurn))
