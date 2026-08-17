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

# Without Variable
print("My name is Aman")
print("Aman Loves Python")

# With Variables
# using f string it provide 
name= "Aman"
language = "Python"
print(f"My name is {name}")
print(f"{name} loves {language}")

# Escape Sequence
print("Line1\nLine2")
print("Hi\tEveryone")
print("Path: C:\\Users")
print("She said\"Hi\"")

# Strings- Transformations
date= "2026/08/14"
print(date.replace("/","-"))
first= "Aman"; last="Kaushik"
print(f"{first} {last}")
csv = "Aman,21,UK"
print(csv.split(","))
print("="*20)

# Strings- Slicing & Indexing
code= "Aman-21"
print(code[0]) # A
print(code[-1]) #1
print(code[0:4]) # Aman
print(code[-2:]) # 21

date= "2026-08-14"
print(date[0:4], date[5:7], date[-2])
print(code[0:9:2]) # stride

# Strings- Cleaning
name= "  Aman "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

# Strip specific chars
print("$Aman$".strip("$"))

# case-insensitive compare
search= "EMAIL"
data= " email "
print(search.lower().strip()== data.lower().strip())

# String- Search
phone= "+91-9341914322"
print(phone.startswith("+91"))

file= "data_backup.csv"
print(file.endswith("csv"))

email= "techinfoaman9341@gmail.com"
print(email.find("@"))
print("@" in email)

# use find() to slice dynamically
print(phone[phone.find("-")+1:])

# String- Validate, Join, Format
# validation
print("USA".isalpha())
print("123456".isnumeric())

# join
parts= ["2026","08","14"]
print("-".join(parts))

# format
print("Hi{n}, order{o}".format(n="Sam",o=1))

# zfill
print("42".zfill(10))

x = 20
y = 3.14
z = 3+2j
print(type(x))
print(type(y))
print(type(z))

# Arithmetic Operations
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b) #float
print(a//b) #floor
print(a%b) #mod
print(a**b) #power

# comparison & logical
x=10; y=5
# Comparison
print(x==y)
print(x!=y)
print(x>y)
print(x<=y)

# Logical
print(x>5 and y<5)
print(x<5 or y>0)
print(not(x==y))

# Rounding(Math Module)
import math
x=10; y=3

# ceil()
print(math.ceil(4.2))
print(math.ceil(4.8))
# floor()
print(math.floor(4.2))
print(math.floor(4.8))
# round()
print(round(4.5))
print(round(4.8))

# Data Structure
# Number
numbers= [10,20,30]
# String
names= ["Aman","Kajal","Pratap"]
# Booleans
status= [True,False,True]
# Mixed Data
data= ["Aman",21,True]
print(data)
print(data[1])

# List Operations

names= ["Aman","Kajal","Pratap"]
print("Original List:",names)
names.append("Rohit")
print("After append('Amit'):", names)
names.remove("Pratap")
print("After remove('Pratap'):", names)
removed_name = names.pop(1)
print("Removed using pop(1):", removed_name)
print("List after pop():", names)
print("Length of list:",len(names))

list = [10,20,30]
name = ["Aman","Kajal","Pratap"]
print(len(name))
print(len(list))
# Len() is a universal method
print("Is 'Aman'present?", "Aman" in names)
print("Is 'Kajal'present?", "Kajal" in names)
names.append("Zoya")
names.append("Ankit")
print("Before Sorting:", names)
names.sort()
print("After Sorting:", names)
names.reverse()
print("After Reverse:", names)
