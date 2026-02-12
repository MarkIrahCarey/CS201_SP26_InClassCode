
for eachPass in range(4): # eachPass in this case is a dummy variable (we don't use it)
    print("It's Alive", end="\n")
"""
The code above is the same as the following

print("It's Alive")
print("It's Alive")
print("It's Alive")
print("It's Alive")
"""
# exponentiation example
print (2 ** 10) # 1024

# we can create a for loop to do the same operation
exponent = 10 # the number of times we multiply
product = 1 # the product, or result
number = 2 # the base
for eachPass in range(exponent):
    product = number * product

print (product)

# count-controlled for loops, we use the variable part of the for loop
# for <variable> in range(<integer-expressions>)
# here we have code that sums each increment per iteration
# we go from 0, 1, 2 for 3 iterations, so the sum becomes 0 + 1 + 2 = 3
sum = 0
for count in range(3):
    # each iteration prints Hello, followed by the sum at each iteration
    print ("Hello ") 
    sum = sum + count
    print (sum)

print ("="*20, "range(start, end)", "="*20)
# 2nd way to use range is using two parameters, start and end
# the following code sums the numbers from 1 - 100 (not counting 101 or end point)
other_sum = 0
for count in range(1, 101): 
    other_sum = other_sum + count

print (other_sum)

# due note that range(1, 13) gives the numbers from 1 - (13 - 1)
# this is just a logic error explained through while loops (Later on )
print(list(range(1, 13)))

# this for loops gets the range of values from 4 - 10 and prints out its perfect square
for i in range (4, 11):
    print (i ** 2)

print ("="*20, "Augmented Assignment", "="*20)
# shortcuts (on operations)
sum_number = 3
sum_number += 4 # is the same as sum_number = sum_number + 4
print (sum_number)

sub_num = 12
sub_num -= 3 # is the same as sub_num = sub_num - 3
print (sub_num)

mult_num = 3
mult_num *= 9 # is the same as mult_num = mult_num * 9
print (mult_num)

greeting = "Hello "
greeting += "World" # is the same as greeting = greeting + "World"
print(greeting)

# characters can also be used as your "range" of values, except each iteration
# is each character of the string
# the following for loop runs through the string "abcde"
# this will have 5 iterations because the string length is 5
# and for each iteration is each letter
alphabet = "abcde"
for char in alphabet:
    print (char, end=" ")

print ('\n', '='*20, "The step value")

"""
The 3rd parameter is called step value, it changes how much the variable
of a for loop increments per iteration
general structure is range(start, end, step)
So if you have range(0, 10, 3), the range of values are [0, 3, 6, 9]
"""
# step value
for i in range(0, 101, 5):
    print (i, end= " ")

print ("")
for i in range(100, -1, -5):
    print (i, end= " ")

print ("")

# before we learned formatting, we had two ways to combine not strings like floats or integers
# the first way is concatenation, which is to convert
# the data values into strings, and combine all the strings
print ("I have " + str(8) + " apples.")

# the other way is using commas to seperate each value
print ("I have",8,"apples.")

# we can use formatting to add place holders, then by the end put the order of which each
# place holder will be replaced

# for integers we can use %d
print ("I have %d apples, %d oranges" % (8, 4))

# for float point, we use %<width>.<precision>f
print ("GPA: " + str(round(3.894444444444, 2)))
print ("GPA: %0.5f" % 3.894444444444)

# later on we will learn this
print (f"I have {8} apples.") # spoilers

# conditional statements

# this following code here is for two way if statements where if the 1st condition was not 
# true, we skip that body, and default to the else's body
""" 
value = int(input("Give me a even number: "))
if value % 2 == 0:
    print("You gave an even number: ")
else:
    print("You didn't give me an even number >:(")
"""

"""value2 = int(input("Give me a big number: "))
if value2 > 200:
    print ("You gave a big number!")
else:
    print ("Your number is too small :(")
"""

# there is also one way, which is simply if the condition is not met, then we just
# skip that body of code
"""
value3 = int(input("Give me a number: "))
if value3 < 50:
    print ("Your value is too small, we will increase by 50")
    value3 += 50
print (value3)
"""

# for multi-if statements, we use the elif keyword, 
"""
temp = int(input("What is the temperature of your porridge: "))

if temp > 100:
    print ("You die!")
elif temp > 30 and temp < 100:
    print ("Its too hot!")
elif temp > 0 and temp < 20:
    print ("Its too cold!")
elif temp <= 0:
    print ("Frozen 3")
else: # temp > 20 and temp < 30
    print ("Its just right!")
"""

"""
theSum = 0
data = input("Enter a number or just enter to quit: ")

while data != "":
    theSum += float(data)
    print ("The sum is", theSum)
    data = input("Enter another number: ")
"""

# for i in range(0, 13):

count = 0
while count < 13:
    print(count)
    count = count + 1 # count += 1

count = 13
while count > 0:
    print(count)

    if count == 5: break
    count = count - 1 # count -= 1

""" 
while True:
    number = float(input("Enter the numeric grade: "))

    if number >= 0 and number <= 100: 
        if number >= 95:
            print ("You got an A+")
        elif number >= 90:
            print ("You got an A")
        break
    else:
        print ("Not a valid grade!")
"""

import random

for i in range(5):
    print (random.randint(3, 10), end = " ")

print ("BIBA " + "UOG!")
print ("BIBA","UOG!","BIBA", sep = " ")