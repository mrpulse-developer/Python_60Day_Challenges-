# 🐍 Python code for Function Parameters and Scope (Day 08)

# 🧩 1. Function with Parameters
def greet(name):
    print(f"👋 Hello, {name}! Welcome to Python Day 8.")

greet("Alice")
greet("Bob")

# 🧠 2. Function with Multiple Parameters
def add_numbers(a, b):
    result = a + b
    print(f"➕ The sum of {a} and {b} is {result}")

add_numbers(5, 3)
add_numbers(10, 20)

# ⚙️ 3. Function with Default Parameter
def greet_user(name="Guest"):
    print(f"Hello, {name}! 👋")

greet_user("John")
greet_user()  # uses default value

# 🎯 4. Function Returning a Value
def multiply(x, y):
    return x * y

product = multiply(4, 6)
print("🧮 Product:", product)

# 🌍 5. Understanding Variable Scope
global_var = "I am a global variable"

def show_scope():
    local_var = "I am a local variable"
    print(local_var)        # accessible inside the function
    print(global_var)       # global variables can be read inside functions

show_scope()

# ❌ Uncommenting below line will cause an error because local_var is not accessible here
# print(local_var)

# 🧩 6. Modifying Global Variable
count = 0

def increment():
    global count  # allows us to modify the global variable
    count += 1
    print("Count inside function:", count)

increment()
increment()
print("Count outside function:", count)
