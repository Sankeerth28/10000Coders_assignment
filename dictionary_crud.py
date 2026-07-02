# ==========================================
# Dictionary CRUD Operations
# ==========================================

# Create an empty dictionary to store employee information
employee = {}

# -------------------------------
# CREATE
# -------------------------------
employee["employee_id"] = 101
employee["name"] = "Rahul"
employee["age"] = 25
employee["department"] = "IT"

print("Employee Added Successfully")
print(employee)

print("\n" + "=" * 40)

# -------------------------------
# READ
# -------------------------------
print("Employee Information")

for key, value in employee.items():
    print(f"{key}: {value}")

print("\n" + "=" * 40)

# -------------------------------
# UPDATE
# -------------------------------
employee["age"] = 26
employee["department"] = "Software Development"

print("Employee Details Updated")
print(employee)

print("\n" + "=" * 40)

# -------------------------------
# DELETE
# -------------------------------
del employee["department"]

print("After Deleting Department")
print(employee)

print("\n" + "=" * 40)

# Final Dictionary
print("Final Employee Record")
print(employee)