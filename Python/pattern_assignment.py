# Pattern 1 : Letter A

for i in range(6):
    for j in range(8):
        if (j == 0 and i != 0) or \
           (j == i and i != 0) or \
           (i == 3 and j <= 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 2 : Letter B

for i in range(5):
    for j in range(5):
        if j == 0 or \
           (i == 0 and j < 4) or \
           (i == 2 and j < 4) or \
           (i == 4 and j < 4) or \
           (j == 4 and i != 0 and i != 2 and i != 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 3 : Letter C

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 4 : Letter D

for i in range(5):
    for j in range(5):
        if j == 0 or \
           (i == 0 and j < 4) or \
           (i == 4 and j < 4) or \
           (j == 4 and i != 0 and i != 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 5 : Letter E

for i in range(5):
    for j in range(5):
        if j == 0 or i == 0 or i == 2 or i == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 6 : Letter F

for i in range(5):
    for j in range(5):
        if j == 0 or i == 0 or i == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 7 : Letter G

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or \
           (i >= 2 and j == 4) or \
           (i == 2 and j >= 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 8 : Letter H

for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or i == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 9 : Letter I

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 10 : Letter J

for i in range(5):
    for j in range(5):
        if j == 4 or (i == 4 and j < 4) or (j == 0 and i == 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 11 : Letter K

for i in range(5):
    for j in range(5):
        if j == 0 or i + j == 3 or i == j - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 12 : Letter L

for i in range(5):
    for j in range(5):
        if j == 0 or i == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 13 : Letter M

for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or \
           (i == j and i < 3) or \
           (i + j == 4 and i < 3):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 14 : Letter N

for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 15 : Letter O

for i in range(5):
    for j in range(5):
        if ((i == 0 or i == 4) and j > 0 and j < 4) or \
           ((j == 0 or j == 4) and i > 0 and i < 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 16 : Letter P

for i in range(5):
    for j in range(5):
        if j == 0 or \
           (i == 0 and j < 4) or \
           (i == 2 and j < 4) or \
           (j == 4 and i == 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 17 : Letter Q

for i in range(5):
    for j in range(5):
        if ((i == 0 and j > 0 and j < 4) or
            (i == 3 and j == 3) or
            (i == 4 and j == 4) or
            (j == 0 and i > 0 and i < 3) or
            (j == 4 and i > 0 and i < 3)):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 18 : Letter R

for i in range(5):
    for j in range(5):
        if j == 0 or \
           (i == 0 and j < 4) or \
           (i == 2 and j < 4) or \
           (j == 4 and i == 1) or \
           (i == j + 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 19 : Letter S

for i in range(5):
    for j in range(5):
        if i == 0 or i == 2 or i == 4 or \
           (j == 0 and i < 2) or \
           (j == 4 and i > 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 20 : Letter T

for i in range(5):
    for j in range(5):
        if i == 0 or j == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 21 : Letter U

for i in range(5):
    for j in range(5):
        if (j == 0 or j == 4) and i < 4:
            print("*", end="")
        elif i == 4 and j > 0 and j < 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 22 : Letter V

for i in range(5):
    for j in range(5):
        if (i < 2 and (j == 0 or j == 4)) or \
           (i == 2 and (j == 1 or j == 3)) or \
           (i >= 3 and j == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 23 : Letter W

for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or \
           (i >= 2 and (i == j or i + j == 4)):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 24 : Letter X

for i in range(5):
    for j in range(5):
        if i == j or i + j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 25 : Letter Y

for i in range(5):
    for j in range(5):
        if (i < 3 and (i == j or i + j == 4)) or \
           (i >= 2 and j == 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()


# Pattern 26 : Letter Z

for i in range(6):
    for j in range(5):
        if i == 0 or i == 5 or j == 4 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()