# Validation - Unit 2

# Example of simple range validation.
var1 = int(input("Please enter a value: ")) # Input expecting an integer between 1 and 10.
if var1 > 10 or var1 < 1: # Validation stage with selection - check whether var1 is in the range.
    print("Invalid input.")
else:
    print("Valid input.")
    print("Var 1:", var1)

# Example of type validation in Python
try:
    var2 = int(input("Please enter a value: ")) # Input expecting an integer.
    print("Var 2:", var2)
except ValueError: # Try-except statements check for specific and general exceptions.
    print("Invalid input.")
except:
    print("An error occurred.")