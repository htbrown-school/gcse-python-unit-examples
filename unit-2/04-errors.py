# Errors - Unit 2

# This file contains three errors. It is meant to output even numbers multiplied together

num = int(input("Enter a start number: "))

for i in rage(num, 10): # Syntax error - "rage" should be "range". 
    if i % 2 == 0:
        num = num * i # Logic error - it should be "i * i"
        print(num)
    else:
        print("num") # Logic error - this is printing the string "num" rather than the variable.