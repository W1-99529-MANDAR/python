num = int(input("Enter a 4-digit integer: "))


digit1 = num // 1000          # Gets the thousands digit
digit2 = (num // 100) % 10    # Gets the hundreds digit
digit3 = (num // 10) % 10     # Gets the tens digit
digit4 = num % 10             # Gets the units digit


digit_sum = digit1 + digit2 + digit3 + digit4


print("The sum of the digits is:", digit_sum)