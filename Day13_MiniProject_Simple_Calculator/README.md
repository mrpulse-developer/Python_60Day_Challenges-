# 🐍 Mini Project: Simple Calculator (Day 13)

## 📘 Description
This mini project is a simple command-line calculator built using Python.  
It supports addition, subtraction, multiplication, and division with proper input validation and error handling.  
The goal of this project is to practice functions, loops, and exception handling.

---

## 💻 Code
```python
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "5":
        print("Exiting...")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except:
        print("Invalid number!")
        continue

    if choice == "1": print("Result:", add(num1, num2))
    elif choice == "2": print("Result:", sub(num1, num2))
    elif choice == "3": print("Result:", mul(num1, num2))
    elif choice == "4": print("Result:", div(num1, num2))

### Out put
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
Enter choice: 1
Enter first number: 10
Enter second number: 5
Result: 15
