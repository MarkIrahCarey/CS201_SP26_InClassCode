"""
File: decrypt.py
Decrypts an input string of lowercase letters and prints
the result. The other input is the distance value.
"""

# ask user for coded text
code = input("Enter the coded text: ")

# then the distance value
distance = int(input("Enter the distance value: "))
plainText = " "

# go through each character
for ch in code:
  # get the ord value of character
  ordvalue = ord(ch)

  # subtract this with the distance 
  cipherValue = ordvalue - distance

  # check if we are below our range from a - z
  if cipherValue < ord('a'):
    # if so, we need to "loop" around. This is simply starting from z, and subtracting
    # the distance and also how far the value was from a (96)

    # so for example, if we go from 100 - 5 = 95. 95 is the same as 121.
    # so we have 121 = 122 - (5 - (100 - 97) + 1) = 122 - 1
    cipherValue = ord('z') - ((distance % 26) - (ordvalue - ord('a') + 1))
  plainText += chr(cipherValue)
print(plainText)