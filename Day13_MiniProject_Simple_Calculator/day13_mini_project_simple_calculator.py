# 🐍 Python code for Mini Project: Simple Calculator (Day 13)

print("📘 Welcome to Simple Python Calculator (Day 13)")

# Function for each operation
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "❌ Cannot divide by zero!"
    return a / b

# Main program loop
while True:
    print("\nChoose an operation:")
    print("1️⃣ Add")
    print("2️⃣ Subtract")
    print("3️⃣ Multiply")
    print("4️⃣ Divide")
    print("5️⃣ Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("👋 Exiting Calculator… Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("❌ Invalid choice! Try again.")
        continue

    # Taking user inputs
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ Please enter valid numbers!")
        continue

    # Performing operations
    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", sub(num1, num2))
    elif choice == "3":
        print("Result:", mul(num1, num2))
    elif choice == "4":
        print("Result:", div(num1, num2))
