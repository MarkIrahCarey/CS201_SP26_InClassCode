# Decimal to Binary

value = int(input("Enter a decimal value: "))
binary = " "
quotient = value
while quotient > 0:
  # record the remainder
  remainder = quotient % 2
  # add to binary_representation (place it infront)
  binary = str(remainder) + binary 
  # update the value by dividing by 2
  quotient = quotient // 2
  # print each iteration
  print(f"Quotient: {quotient} \t Remainder: {remainder} \t Binary: {binary} \t")

print(f"{value} = {binary}")

# Binary to Decimal
binary = input("Enter binary value: ")
operations = " "
decimal_value = 0
# start from the highest place
for i in range(len(binary)):
  # since this starts at the highest place, that is the highest power
  # which means power decrements from the max length
  power = len(binary) - i - 1
  # then we want to add each by the power of 2
  operation = int(binary[i]) * 2 ** power
  decimal_value += int(binary[i]) * 2 ** power

  # then also show the operations
  operations = f"{operation}" if i == 0 else f"{operations} + {operation}"
  print(f"Operation: {operations}")

print(f"{operations} = {decimal_value}")

# Decimal to Octal
value = int(input("Enter a decimal value: "))
octal = ""
quotient = value
while quotient > 0:
  # check remainder by dividing by 8
  remainder = quotient % 8

  # add that to the octal
  octal = str(remainder) + octal

  # then divide by 8
  quotient = quotient // 8

  print(f"Quotient: {quotient} \t Remainder: {remainder} \t Binary: {octal} \t")

print(f"{value} = {octal}")

# Octal to Decimal
octal = input("Enter octal value: ")
decimal_value = 0
operations = ""
for index in range(len(octal)):
  # similar process to binary where we take each place value and multiply
  # by the power
  power = len(octal) - index - 1
  operation = int(octal[index]) * 8 ** power
  decimal_value += operation

  # show operations
  operations = f"{operation}" if index == 0 else f"{operations} + {operation}"
  print(f"Operation: {operations}")
print(f"{operations} = {decimal_value}")