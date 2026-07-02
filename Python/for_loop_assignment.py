from colorama import init, Style
init(autoreset=True)

print(Style.BRIGHT+"Countdown Timer")

for i in range(10, 0, -1):
    print(i)

print("Boom!")


print(Style.BRIGHT+"2. Find Lucky Number (Divisible by 7)")

for i in range(1, 51):
    if i % 7 == 0:
        print(i)


print(Style.BRIGHT+"Add all game scores")

scores = [50, 65, 70]
total = 0
for score in scores:
    total = total + score
print("Total Score:", total)


print(Style.BRIGHT+"4. Multiplication Table of 5")
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)


print(Style.BRIGHT+"5. Count Vowels")

word = "education"
count = 0
for letter in word:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        count = count + 1
print("Number of vowels:", count)


print(Style.BRIGHT+"6. Swap Two Numbers")

a = 10
b = 20

print("Before Swapping")
print("a =", a)
print("b =", b)

temp = a
a = b
b = temp

print("After Swapping")
print("a =", a)
print("b =", b)

print(Style.BRIGHT+"7. ATM Withdrawal Simulation")

balance = 1000
withdrawals = [100, 200, 150]
for amount in withdrawals:
    balance = balance - amount
    print("Remaining Balance:", balance)
print("Final Balance:", balance)



print(Style.BRIGHT+"8. Find Highest Marks")

marks = [45, 78, 89, 66]

highest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

print("Highest Marks:", highest)


print(Style.BRIGHT+"9. Number Guess Check")

number = 25

for i in range(1, 51):
    if i == number:
        print("Number Found:", i)



print(Style.BRIGHT+"10. Even Number Counter")
count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1

print("Total Even Numbers:", count)


print(Style.BRIGHT+"11. Reverse a String Using For Loop")

word = "python"

reverse = ""

for letter in word:
    reverse = letter + reverse

print("Reversed String:", reverse)