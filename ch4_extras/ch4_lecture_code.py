# fstring

name = "Alice"
age = 30
another_age = age + 5

# old way
print("You are %d years old, in 5 years you will be %d" % (age, another_age))

# the fstring way
print(f"You are {age} years old, in 5 years you will be {another_age}")

# len function
cookie_brand = "biscoff"
print(len(cookie_brand))

# subscript, get the o character
print(cookie_brand[4])

# using negative numbers
print(cookie_brand[-3])

# IndexError (accessing an index beyond the length)
# print(cookie_brand[-8])

# example
some_string = "12ab34"

count = 0
for ch in some_string:
    if not ch.isdigit():
        count += 1
print(count)

count = 0
for index in range(len(some_string)):
    if not some_string[index].isdigit():
        count += 1
print(count)

# substrings
print(cookie_brand[0:4])
print(cookie_brand[4:7])

# example
textfile = "myfile.txt"
print(textfile[-4:])

files = ["report.txt", "data.csv", "notes.txt", "script.py"]

count_txt = 0
for fname in files:
    if ".txt" in fname:
        count_txt += 1
print(f"Number of Text Files: {count_txt}")

import os

print(os.getcwd())
cwd = os.getcwd()

listOfFileNames = os.listdir(cwd)
print(listOfFileNames)

# make new folder
# os.mkdir(f"{cwd}/New_Folder")
os.rmdir(f"{cwd}/New_Folder")