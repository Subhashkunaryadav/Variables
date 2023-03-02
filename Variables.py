# Integer variables
x = 10
y = 20
z = x + y
print("The sum of {} and {} is {}".format(x, y, z))

# Float variables
a = 1.5
b = 2.5
c = a * b
print("The product of {} and {} is {}".format(a, b, c))

# String variables
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))

# Boolean variables
is_true = True
is_false = False
print("is_true is {} and is_false is {}".format(is_true, is_false))

# List variables
fruits = ["apple", "banana", "cherry"]
print("All fruits: {}".format(fruits))
print("First fruit: {}".format(fruits[0]))
fruits.append("orange")
print("All fruits after appending: {}".format(fruits))

# Tuple variables
numbers = (1, 2, 3, 4, 5)
print("All numbers: {}".format(numbers))
print("First number: {}".format(numbers[0]))

# Set variables
colors = {"red", "green", "blue"}
print("All colors: {}".format(colors))
colors.add("yellow")
print("All colors after adding: {}".format(colors))

# Dictionary variables
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print("Person's name is {}".format(person["name"]))
print("Person's age is {}".format(person["age"]))
print("Person's city is {}".format(person["city"]))

# Type conversion
x = 10
y = 2.5
z = "5"
print(type(x), type(y), type(z))
x = float(x)
y = int(y)
z = int(z)
print(type(x), type(y), type(z))

# Global and local variables
global_var = "I am a global variable"

def my_func():
    local_var = "I am a local variable"
    print(global_var)
    print(local_var)

my_func()

# 11. Constant variables
PI = 3.14159
GRAVITY = 9.81
print("The value of PI is {}".format(PI))
print("The value of GRAVITY is {}".format(GRAVITY))

# 12. Variable naming conventions
my_variable = 10
myVariable = 20
_my_variable = 30
MY_VARIABLE = 40

# Deleting variables
x = 10
del x


#  Multiple assignment
x, y, z = 10, 20, 30
print(x, y, z)

# Swapping variables
x, y = 10, 20
print("Before swapping: x = {} and y = {}".format(x, y))
x, y = y, x
print("After swapping: x = {} and y = {}".format(x, y))

# Using variables in strings
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")

#  Assigning variables with arithmetic operators
x = 10
x += 5
print(x)
x -= 2
print(x)
x *= 3
print(x)
