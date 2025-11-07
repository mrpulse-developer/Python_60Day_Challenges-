# 🐍 Python Code for Operators (Day 04)

# 🧮 1. Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# 🔁 2. Assignment Operators
x = 5
x += 3   # same as x = x + 3
print("Assignment (+=):", x)

# ⚖️ 3. Comparison Operators
print("Equal (==):", a == b)
print("Not Equal (!=):", a != b)
print("Greater Than (>):", a > b)
print("Less Than or Equal To (<=):", a <= b)

# 🧠 4. Logical Operators
is_adult = True
has_id = False

print("AND (and):", is_adult and has_id)
print("OR (or):", is_adult or has_id)
print("NOT (not):", not is_adult)

# 🧩 5. Ternary (Conditional) Operator
age = 18
message = "Eligible to vote 🗳️" if age >= 18 else "Not eligible to vote ❌"
print("Ternary Result:", message)
