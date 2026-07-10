
# Pattern 1 : Letter A
print("Pattern 1 : Letter A")
for i in range(6):
    for j in range(8):
        if (j == 0 and i != 0) or (j == i and i != 0) or (i == 3 and j <= 4):
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# Pattern 2 : Letter B
print("Pattern 2 : Letter B")
for i in range(5):
    for j in range(5):
        if j == 0 or (i == 0 and j < 4) or (i == 2 and j < 4) or (i == 4 and j < 4) or (j == 4 and i not in [0,2,4]):
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# Pattern 3 : Letter C
print("Pattern 3 : Letter C")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# Pattern 4 : Letter D
print("Pattern 4 : Letter D")
for i in range(5):
    for j in range(5):
        if j == 0 or (i == 0 and j < 4) or (i == 4 and j < 4) or (j == 4 and i not in [0,4]):
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# Pattern 5 : Letter E
print("Pattern 5 : Letter E")
for i in range(5):
    for j in range(5):
        if j == 0 or i in [0,2,4]:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# Pattern 6 : Letter F
print("Pattern 6 : Letter F")
for i in range(5):
    for j in range(5):
        if j == 0 or i in [0,2]:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# Pattern 7 : Letter G
print("Pattern 7 : Letter G")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or (i >= 2 and j == 4) or (i == 2 and j >= 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# Pattern 8 : Letter H
print("Pattern 8 : Letter H")
for i in range(5):
    for j in range(5):
        if j == 0 or j == 4 or i == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# Pattern 9 : Letter I
print("Pattern 9 : Letter I")
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

letters = [
("10","J"),("11","K"),("12","L"),("13","M"),("14","N"),("15","O"),
("16","P"),("17","Q"),("18","R"),("19","S"),("20","T"),
("21","U"),("22","V"),("23","W"),("24","X"),("25","Y"),("26","Z")
]

# Remaining patterns (same logic as your original submission)
# J
print("Pattern 10 : Letter J")
for i in range(5):
    for j in range(5):
        print("*" if (j==4 or (i==4 and j<4) or (j==0 and i==3)) else " ", end="")
    print()
print()

print("Pattern 11 : Letter K")
for i in range(5):
    for j in range(5):
        print("*" if (j==0 or i+j==3 or i==j-1) else " ", end="")
    print()
print()

print("Pattern 12 : Letter L")
for i in range(5):
    for j in range(5):
        print("*" if (j==0 or i==4) else " ", end="")
    print()
print()

print("Pattern 13 : Letter M")
for i in range(5):
    for j in range(5):
        print("*" if (j==0 or j==4 or (i==j and i<3) or (i+j==4 and i<3)) else " ", end="")
    print()
print()

print("Pattern 14 : Letter N")
for i in range(5):
    for j in range(5):
        print("*" if (j==0 or j==4 or i==j) else " ", end="")
    print()
print()

print("Pattern 15 : Letter O")
for i in range(5):
    for j in range(5):
        print("*" if (((i==0 or i==4) and 0<j<4) or ((j==0 or j==4) and 0<i<4)) else " ", end="")
    print()
print()

print("Pattern 16 : Letter P")
for i in range(5):
    for j in range(5):
        print("*" if (j==0 or (i==0 and j<4) or (i==2 and j<4) or (j==4 and i==1)) else " ", end="")
    print()
print()

print("Pattern 17 : Letter Q")
for i in range(5):
    for j in range(5):
        print("*" if (((i==0 and 0<j<4) or (i==3 and j==3) or (i==4 and j==4) or (j==0 and 0<i<3) or (j==4 and 0<i<3))) else " ", end="")
    print()
print()

print("Pattern 18 : Letter R")
for i in range(5):
    for j in range(5):
        print("*" if (j==0 or (i==0 and j<4) or (i==2 and j<4) or (j==4 and i==1) or (i==j+1)) else " ", end="")
    print()
print()

print("Pattern 19 : Letter S")
for i in range(5):
    for j in range(5):
        print("*" if (i in [0,2,4] or (j==0 and i<2) or (j==4 and i>2)) else " ", end="")
    print()
print()

print("Pattern 20 : Letter T")
for i in range(5):
    for j in range(5):
        print("*" if (i==0 or j==2) else " ", end="")
    print()
print()

print("Pattern 21 : Letter U")
for i in range(5):
    for j in range(5):
        print("*" if (((j==0 or j==4) and i<4) or (i==4 and 0<j<4)) else " ", end="")
    print()
print()

print("Pattern 22 : Letter V")
for i in range(5):
    for j in range(5):
        print("*" if ((i<2 and (j==0 or j==4)) or (i==2 and (j==1 or j==3)) or (i>=3 and j==2)) else " ", end="")
    print()
print()

print("Pattern 23 : Letter W")
for i in range(5):
    for j in range(5):
        print("*" if (j==0 or j==4 or (i>=2 and (i==j or i+j==4))) else " ", end="")
    print()
print()

print("Pattern 24 : Letter X")
for i in range(5):
    for j in range(5):
        print("*" if (i==j or i+j==4) else " ", end="")
    print()
print()

print("Pattern 25 : Letter Y")
for i in range(5):
    for j in range(5):
        print("*" if (((i<3 and (i==j or i+j==4)) or (i>=2 and j==2))) else " ", end="")
    print()
print()

print("Pattern 26 : Letter Z")
for i in range(6):
    for j in range(5):
        print("*" if (i==0 or i==5 or j==4-i) else " ", end="")
    print()
