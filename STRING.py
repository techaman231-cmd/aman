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
