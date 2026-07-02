# ==========================================
# Variables and Data Types in Python
# ==========================================

# 1. Declare variables of different data types
age = 22                  # int
height = 6.3              # float
name = "Lucky"            # string
is_student = True         # boolean

print("Different Data Types")
print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Student:", is_student, type(is_student))

print("\n" + "="*40)

# 2. Assign and reassign values
number = 100
print("Original Value:", number, type(number))

number = 150
print("After Reassigning:", number, type(number))

number = "One Hundred Fifty"
print("After Changing Data Type:", number, type(number))

print("\n" + "="*40)

# 3. Store personal information
person_name = "Lucky"
person_age = 22
person_height = 6.3
is_employed = False

print("Personal Information")
print("Name:", person_name)
print("Age:", person_age)
print("Height:", person_height)
print("Employed:", is_employed)

print("\n" + "="*40)

# 4. Arithmetic operations
num1 = 20
num2 = 7.5

print("Arithmetic Operations")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // 2)
print("Modulus:", num1 % 3)

print("\n" + "="*40)

# 5. Using id() function
a = 50
b = 50
c = 100

print("Memory Locations")
print("ID of a:", id(a))
print("ID of b:", id(b))
print("ID of c:", id(c))

print("a and b have same value:", a == b)
print("a and b have same memory:", id(a) == id(b))

print("\n" + "="*40)

# 6. Variable Scope
message = "I am outside the if block."

if True:
    inside_message = "I am inside the if block."
    print(inside_message)

print(message)
print(inside_message)

print("\nProgram Completed Successfully!")