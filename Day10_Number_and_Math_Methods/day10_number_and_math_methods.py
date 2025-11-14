# 🐍 Python Code for Number and Math Methods (Day 10)

num = 25.6789

# 1. Rounding & Formatting
print("Round:", round(num))
print("Round to 2 decimals:", round(num, 2))
print("Convert to int:", int(num))
print("Convert to float:", float("45.67"))

# 2. Checking number properties
print("Is digit:", "123".isdigit())
print("Is numeric:", "50".isnumeric())

# 3. Math operations (using math module)
import math

print("Square root:", math.sqrt(49))
print("Power:", math.pow(2, 3))
print("Floor:", math.floor(4.9))
print("Ceil:", math.ceil(4.1))
print("Absolute:", abs(-10))

# 4. Random numbers
import random

print("Random (0-1):", random.random())
print("Random (1-10):", random.randint(1, 10))
print("Random choice:", random.choice([10, 20, 30, 40]))
