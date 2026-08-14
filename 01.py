# A variable is just a label for a value
name = "Ali Khan"
print(name)

# Dynamically Typed 
name = "Amanpreet Singh"
print(name)

# Today it can point to string
x= "Hello World"
print(type(x))

# Tomorrow it can point to an integer
x = 20
print(type(x))

# Updation of variable
name = "Aman Singh"
print(name)
name = "Karan Singh"
print(name)

a = 10
b = 20
c = a + b
print(c)

# Data types in Python
a = 10 # int
b = 10.5 # float
c = "Kajal" # string
d = True # boolean (True or False)
e = None # NoneType

# Dyanamic - Python re-detects
a = "Aman"
# Built in Functions
print(type(a)) 

# Primitive - one value
x = 20
y = "Aman"
z = None

# Collection - multiple values
nums = [1, 2, 3, 4, 5] # list
pair = (1, 2) # tuple
unique_nums = {1, 2, 3, 4, 5} # set
info = {"name": "Aman", "age": 20} # dictionary
print(type(nums))

# Working with Quotes
# 1. Escape Character
print("Hello \"World\"")
# 2. Mixed Quotes
print('Hello "World"')
# 3. Triple Quotes
print("""Hello
World""")

# Functions in Python
# Built-in Functions
print(len("Hello World"))
# External(after import)
import math
print(math.sqrt(16))
# User-defined Functions
def greet(name):
    return "Hello " + name
print(greet("Aman"))

# Built-in Functions
name = input("Enter your name: ")
print(name)

# Read text
name = input("Enter your name: ")
print("Hello,", name)
# Read number
age = int(input("Enter your age: "))
print("Next year:", age + 1)

# Functions vs Methods
text = "Aman"
num =80

# Function - work on either
print(len(text))
print(type(text))

# Method - work on specific data type
print(text.upper())
print(num.bit_length())
