# 🐍 Python Code for Functions (Day 07)

# 🧩 1. Basic Function
def greet():
    print("👋 Hello, welcome to Day 7 of Python!")

greet()

# 🧠 2. Function with Parameters
def add(a, b):
    return a + b

print("Addition:", add(5, 3))

# 🔄 3. Function with Default Parameter
def greet_user(name="Guest"):
    print(f"Hello, {name}! 👋")

greet_user("Alice")
greet_user()

# ⚡ 4. Function Returning a Value
def multiply(x, y):
    result = x * y
    return result

print("Multiplication:", multiply(4, 6))

# 🎯 5. Function Returning Another Function
def outer():
    def inner():
        print("This is an inner function!")
    return inner

inner_func = outer()
inner_func()
