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
