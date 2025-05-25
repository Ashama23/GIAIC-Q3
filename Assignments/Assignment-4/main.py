# Basic if-else
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# elif (multiple conditions)
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")  # This will execute
elif grade >= 70:
    print("C")
else:
    print("F")

# Ternary operator (one-liner)
status = "Adult" if age >= 18 else "Minor"
print(status)  # "Adult"

# Iterate through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())
# Output: APPLE BANANA CHERRY

# With range()
for i in range(5):  # 0 to 4
    print(i, end=" ")  # 0 1 2 3 4

# With enumerate (index + value)
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# Basic while loop
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1
# Output: Count: 0, Count: 1, Count: 2

# Break and continue
num = 0
while True:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
    if num >= 5:
        break  # Exit loop
# Output: 1 3 5


def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # "Hello, Alice!"


def power(base, exponent=2):  # exponent defaults to 2
    return base ** exponent

print(power(3))     # 9 (3^2)
print(power(3, 3))  # 27 (3^3)

def sum_all(*args):  # Accepts any number of positional args
    return sum(args)

print(sum_all(1, 2, 3))  # 6

def print_info(**kwargs):  # Accepts any number of keyword args
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
# name: Alice
# age: 25

square = lambda x: x ** 2
print(square(5))  # 25

# Used with filter() and map()
numbers = [1, 2, 3, 4]
even = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]
squared = list(map(lambda x: x ** 2, numbers))      # [1, 4, 9, 16]


import math

print(math.sqrt(16))    # 4.0
print(math.factorial(5)) # 120
print(math.pi)          # 3.141592653589793

import random

print(random.randint(1, 10))  # Random integer between 1-10
print(random.choice(["a", "b", "c"]))  # Random choice
random.shuffle([1, 2, 3])     # Shuffles list in-place


from datetime import datetime

now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # e.g., "2023-05-20 14:30:00"


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("No errors occurred")
finally:
    print("This always runs")


# Basic comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Nested comprehension
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]  # [1, 2, 3, 4]


def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Returns value without exiting function
        count += 1

counter = count_up_to(3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3

