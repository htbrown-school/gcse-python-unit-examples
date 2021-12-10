# The OR logic gate outputs a 1 if either of the two inputs are 1, otherwise it will output a 0
# For example:
#  • if the two inputs are 0 and 1 then it will output a 1
#  • if the two inputs are both 0 then it will output a 0
# Write a Python program that will output the result of performing an OR logic gate.
#
# Your program should:
#  • keep asking the user to enter two values until they enter two values, each of which must be
#    either a 0 or a 1
#  • calculate the correct output from an OR gate using the two inputs that have been entered
#  • output the result of the OR gate.
# You should use meaningful variable name(s), correct syntax and indentation in your answer. 

input1 = int(input("Enter the first input: ")) # Whole number - integer
while input1 != 0 and input1 != 1: # Check to make sure it's a valid result
    input1 = int(input("Enter the first input: "))

input2 = int(input("Enter the second input: "))
while input2 != 0 and input2 != 1:
    input2 = int(input("Enter the second input: "))

if input1 == 1 or input2 == 1: # Logic gate functionality
    print("Output: 1")
else:
    print("Output: 0")