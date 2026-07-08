from colorama import init, Style
init(autoreset=True)

print(Style.BRIGHT+"Exercise 1")
"Days to Years"
'''
1 year  = 365days 
1 day = 1/365 years

'''
days = int(input("Enter Days : "))
years = days/365
print(years)


print(Style.BRIGHT+"Exercise 10. Finding Extremes (Min/Max) in a List")
'''
Exercise 10. Finding Extremes (Min/Max) in a List

'''

nums = [45, 2, 89, 12, 7]
maxi = max(nums)
mini = min(nums)
print(maxi)
print(mini)

print(Style.BRIGHT+"Exercise 11. Removing Duplicates from a List")
data = [1, 2, 2, 3, 4, 4, 4, 5]
dataset = set(data)
datal = list(dataset)
print(datal)


print(Style.BRIGHT + "Exercise 12. List Comparison and Boolean Logic")
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [10, 20, 30, 40, 10]
res = True

if len(numbers_x) ==  len(numbers_y):
    for i in range(len(numbers_x)):
        if numbers_x[i] == numbers_y[i]:
            res = True
        else:
            res = False
else:
    res = False
    
    
print(res)

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [10, 20, 30, 40, 10]

print(numbers_x == numbers_y)


print(Style.BRIGHT+"Exercise 13. Filtering Lists with Conditional Logic")
num_list = [10, 20, 33, 46, 55]
lis = list()
for i in num_list:
    if i%5 == 0:
        print(i)




print(Style.BRIGHT+"Exercise 14. Substring Frequency Analysis")
str_x = "Emma is good developer. Emma is a writer"

print(str_x.count("Emma"))


print(Style.BRIGHT+"Exercise 15. Nested Loops for Pattern Generatio")
for i in range(1,6):
    for j in range(i):
        print(i ,end=" ")
    print("\n")

print(Style.BRIGHT+"Exercise 16. Numerical Palindrome Check")
number = 123
str_num = str(number)
if str_num == str_num[::-1]:
    print(True)
else:
    print(False)

print(Style.BRIGHT+"Exercise 17. Merging Lists with Parity Filtering")
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
res_lis = list()
for i in list1:
    if i%2 != 0:
        res_lis.append(i)


for i in list2:
    if i%2 == 0:
        res_lis.append(i)

print(res_lis)


print(Style.BRIGHT+"Exercise 18. Integer Digit Extraction and Reversal")
number = 7536
# num = str(number)
# print(num[::-1])

while number>0:
    dig = number%10
    number //=10
    print(dig,end="")



print(Style.BRIGHT+"Exercise 20. Nested Loops for Multiplication Tables")
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print("\n")


print(Style.BRIGHT+"Exercise 21. Downward Half-Pyramid Pattern")
for i in range(5,0,-1):
    for j in range(0,i):
        print("*", end=" ")
    print("\t")

for i in range(5,0,-1):
    print(i*"*", end=" ")
    print("\t")


print(Style.BRIGHT+"Exercise 19. Multi-Tiered Income Tax Calculation")
'''
Practice Problem: Calculate income tax for a given income based on these rules:

First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax
Exercise Purpose: This exercise introduces ΓÇ£Tax BracketsΓÇ¥ logic, a classic example of complex conditional branching. It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.

Given Input: income = 45000

Expected Output: Total income tax to pay is 6000
'''

income = int(input("Enter the input : "))
tax_pay = 0
if income > 10000:
    tax_pay+=(10000*0.10)
elif income>20000:
    remaining_amt = income-20000
    tax_pay +=remaining_amt*0.20
else:
    taxamt = income-10000
    tax_pay =  taxamt*0.10
    
print(tax_pay)    

print(Style.BRIGHT + "Exercise 22. Custom Exponentiation Function")
'''Practice Problem: Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

Exercise Purpose: Learn about ΓÇ£Accumulator Patterns.ΓÇ¥ Although Python has a built-in power operator (**), 
making your own version shows how repeated multiplication works and how functions return results to the main program.

Given Input: base = 2, exp = 5

Expected Output: 2 raises to the power of 5: 32'''

def expo(base,exp):
    num = exp
    res = 1
    while num>0:
        res = res*base
        num -=1
    print(res)

basen = int(input("Enter the base : "))
expn = int(input("Enter the exponent : "))
expo(basen,expn)


print(Style.BRIGHT+"Exercise 23. Check Palindrome Number")

num = 143
o_num = num
r_num = 0
while num>0:
    dig = num%10
    r_num = r_num*10+dig
    num //= 10
print("Original number",o_num)
if o_num==r_num:
    print(True)
else:
    print(False)


def fibo(num):
    if num <= 1:
        return num

    fibo1 = fibo(num - 1)
    fibo2 = fibo(num - 2)
    res = fibo1 + fibo2
    return res

res = fibo(15)
print(res)


print(Style.BRIGHT+"Exercise 25. Check Leap Year")
year = 2024
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    print("True Its a Leap Year")
else:
    print("not a Leap Year")

print(Style.BRIGHT+"Exercise 26. Merging Two Dictionaries")
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "job": "Engineer"}
res = dict1|dict2
dict1.update(dict2)
print(res)
print(dict1)

print(Style.BRIGHT + "Exercise 27. Finding Common Elements (Intersections)")
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

num = set(list_a)
num1 = set(list_b)

res = num.intersection(num1)
print(res)

print(Style.BRIGHT+ "Exercise 28. Odd/Even List Splitter")
numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]
odd_lis = list()
even_lis = list()
for i in numbers:
    if i%2==0:
        even_lis.append(i)
    else:
        odd_lis.append(i)
        
print("Even List : ",even_lis)
print("\nOdd List : ",odd_lis)


print(Style.BRIGHT+ "Exercise 29. Word Length Analysis")
words = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for i in words:
    length = len(i)
    print(f"{i} - {length}")


print(Style.BRIGHT+"Exercise 30. Word Frequency Counter (The Histogram)")
text = "apple banana apple cherry banana apple"
lis = text.split()
print(lis)
contain = {}
for i in lis:
    if i in contain:
        contain[i] += 1
    else:
        contain[i] = 1
print(contain)

print(Style.BRIGHT+"Exercise 31. Print Alternate Prime Numbers")
def prime(start,end):
    primes = []
    
    for i in range(start,end):
        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    print(primes) 
    print(primes[::2])
prime(2,31)


print(Style.BRIGHT+"Exercise 32. Dictionary of Squares (Mapping Logic)")
contain = {}
for i in range(1,11):
    contain[i] = i**2
    
print(contain)

print(Style.BRIGHT+"Exercise 32. Dictionary of Squares (Mapping Logic)")
given_Input = "I love coding in Python"
res = given_Input.replace(" ","_")
print(res)


print(Style.BRIGHT+"Exercise 34. Print Reverse Number Pattern")
rows = 5
for i in range(rows,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("")    



print(Style.BRIGHT+"Exercise 35. Digit Detection in Strings")
input_string = "Python3"
for char in input_string:
    if char.isdigit():
        print(char, True)
    else:
        print(char, False)

print(Style.BRIGHT+"Exercise 36. Capitalize First Letter (Title Case)")
text = "hello world from python"
print(text.title())

text = "hello world from python"
lis = text.split()
cap = []
for word in lis:
    cap.append(word.capitalize())

res = " ".join(cap)
print(res)

print(Style.BRIGHT+"Exercise 37. Simple Countdown Timer")
num = 15
while num >0:
    print(num, end=" ")
    num-=1
print("Blast OFf...")
