# Write a Python program that will calculate the volume of a rectangular swimming pool with a depth
# of two metres. The formula for calculating the volume is: volume = length x width x depth
# Your program should:
#  • prompt the user to enter the length in metres (the value should be a whole number)
#  • prompt the user to enter the width in metres (the value should be a whole number)
#  • calculate the correct volume
#  • output the volume.
# You should use meaningful variable name(s), correct syntax and indentation in your answer.

length = int(input("Enter the length of the pool (metres): ")) # Whole number - integer
width = int(input("Enter the width of the pool (metres): "))

volume = length * width * 2 # Using volume formula
print("The pool has a volume of " + str(volume) + " metres cubed.")