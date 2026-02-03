"""
This is a multi-lined comment
This is if you want to write things in multiple lines instead 
of having do do # for every other line
"""

# examples of using """ """ as a string

# this example here is using two print statements to create a new line
print("Hi, it is nice meeting you.")
print("The weather is nice.")

# here we have a multi-line where we entered that new line
print("""Hi, it is nice meeting you.
The weather is nice.""")

# \b Backspace
print("Hello\b\b\b World!\b:D") # He World:D

# \n Newline
print("Hi, it is nice meeting you.\nThe weather is nice")
# the \n creates a new line, then continues the string

# \t Horizontal Tab
print("Hello \t World") # creates the tab space like using tab on a keyboard

# \\ \' \", these allow us to enter \,', and " character since they are reserved
# for other functionality (like strings or escape sequences)
print("He said, \"I like seals\" ")

# * operator on a string, repeats that strings however many times
print("ha"*10) #hahahahahahahahahaha

# variables
number = 1 
Number = 2
# number and Number are different! They are holding different values
# despite having the same name

# correction, ALL CAPS does not make these constant (a.k.a you can't change them)
# its just a naming convention
TAX = 0.10 # Tax rate
TAX = TAX + 0.20
print (round(TAX, 3))

# note how python writes this, not 0.00000000000000001 but 1e-17
print (0.00000000000000001)

# ord, follows from the ASCII table
print (ord('K'))

# - (negation), just gets the "opposite"
print (-(3 + 5))

# ** (exponentiation) or the power (^)
print (3 ** 5) # 3 ^ 5 = 243

# * (multiplication)
print (7 * 8) # 56 

# / (division, float division operator, this is the default operation)
print (35/4)

# // (quotient or integer division, this gives the quotient when dividing)
print (35 // 4)

# % modulo, this gives the remainder 
print (35 % 4)

# + addition and - subtraction
print (3 + 4)
print (3 - 4)

# orders of operation
print (3 * 4 / 2)
print (3 ** 2 ** 2)

# change the order using parenthesis
print (3 * 4 / 2 * 6 * 10) 
# ^this goes as follows:
# 12 / 2 * 6 * 10
# 6 * 6 * 10
# 36 * 10
# 360

# suppose you want multiplication to go first
print ((3 * 4) / (2 * 6 * 10)) 
# this becomes:
# 12 / 120
# 1 / 10 
# 0.1

# you can use \ to make a new line in the event that an equation is too long
# and you want to make it "look" more cleaner
print ((3 ** 2) \
       ** 2)

# help function
# help(print)

import math # important that all imports are at the top of your code!

# to use functions from math, call the math module folowed by a .
print (math.pi) # returns the value of pi
print (math.e) # returns the value of e
