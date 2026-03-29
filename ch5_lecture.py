# lists

# you can initialize a list
# var_name = [e1, e2, e3, ...]
# alternatively, you can create one without any elements
# var_name = []
numbers = [12, 9, 3, 6, 9, 15, 7, 10]

# print out list
print (len(numbers))

# accessing elements
print(numbers[5:7]) # you can access multiple elements using :
print(numbers[-1]) # you can also use negative numbers

# list of fruits
fruits = ['apples', 'oranges', 'cherries']
print(f"Mark likes {fruits[0]}") # getting the first element

# list of lists
coordinates = [[5, 9], [541, 78]]
print (coordinates[0][1]) # access the 1st element, within the first element (which is a list) access the 2nd element

# can also work with expressions
"""
import math
x = 2
numbers = [x, math.sqrt(x)]
print(numbers)
"""

# list() function converts any sequences into a list
numbers_1_to_100 = list(range(1, 101))
numbers_101_to_200 = list(range(101, 201))
print(numbers_1_to_100, numbers_101_to_200, sep = "\n")

# concatenation for lists combines the lists into a one bigger list
numbers_1_to_200 = numbers_1_to_100 + numbers_101_to_200

print(numbers_1_to_200)

# can also convert string into lists, each character is an element
string_example = list("Hello")
print(string_example)

# other operations like == also works
list_scores = [100, 90, 80]
list_scores_2 = [100, 90, 80]

print (list_scores == list_scores_2)

# to see if an element exists within the list, we use the in keyword
print (150 in numbers_1_to_200)
print (500 in numbers_1_to_200)
print ('cherries' in fruits)

# replace 7 in list of numbers
print (numbers)
numbers[6] = 1 # assign a different element in index 6
print (numbers)
numbers[3] = 100 # assign a different element for index 3
print(numbers)

# book example with for loops and lists
sentence = "Anyone know if the student center is open twenty four seven?"
words = sentence.split()
print(f"Before for loop: {words}")
for index in range(len(words)):
  words[index] = words[index].upper()
print(f"After for loop: {words}")

# book example with for loops and lists
numbers = [2, 3, 4, 5]
print(f"Before for loop: {numbers}")
for index in range(len(numbers)):
  numbers[index] = numbers[index] ** 2
print(f"After for loop: {numbers}")

# add 36 into numbers
numbers.append(36)
print(numbers)

# add another list into numbers
numbers.extend([49, 64, 81, 100])
print(numbers)

# add 30 between 25 and 36 
numbers.insert(4, 30)
print(numbers)

# cannot insert lists, only elements
# numbers.insert(7, [50, 51, 52]) # this doesn't work
# print(numbers)

# removing elements
numbers.pop()
print(numbers)

# removing at specific indicies
numbers.pop(3)
print(numbers)

aList = [34, 45, 67, 50, 13, 32, 90]
target = 13
if target in aList:
    print(aList.index(target))
else:
    print("Not found")

# using .sort(), works on strings as well
names = ["Maria", "mark", "Mark", "maria"]
names.sort()
print(names)

# some problems with mutable lists, aliasing
# since lists are mutable, assigning another variable with a list will have them
# point to the same list in memory. This is a problem because when you
# change something in either variable, they both reflect that change since they
# reference the same thing.
another_list = aList
aList[2] = 68
print(aList)
print(another_list)

# to avoid things like this, create a new list
# then put all the elements of the list into the new list
new_list = []
for element in aList:
   new_list.append(element)

aList[2] = 100
print(aList)
print(new_list)

# you can also use .copy()
# new_list = aList.copy()

# tuples, the immutable lists, I am not sure why you'd want to use this
coordinate = (-10, 10)
print(coordinate)

# creating simple methods/functions!
def square(x):
    """Return the square of x."""
    return x * x

# Test the function
print(square(5))
print(square(7))

# another method, takes in 4 parameters
def distance_formula(x_1, y_1, x_2, y_2):
   formula = (((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)) ** (0.5)
   slope = (y_2 - y_1) / (x_2 - x_1)
   return [formula, slope]

print(distance_formula(4, 5, 6, 7))

# dictionary
info = {'name': 'Sandy', 
        'occupation': 'manager'}
print(info["name"])

info['job'] = 'manager'
# Safe access with get
print(info.get("job", "Not found"))
print(info.get("name", "Not found"))

grades = {90: 'A', 80: 'B', 70: 'C'}
print (grades.items())
for key, value in grades.items():
    print(key, value)

# methods for dictonary
print(len(grades))

print(list(grades.values()))
print(list(grades.keys()))

grades.clear()
print(grades)
