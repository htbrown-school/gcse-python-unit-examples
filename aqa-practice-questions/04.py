# Write a Python program that plays the following number guessing game.
# Your program should:
#  • randomly generate a 2 digit numeric code (ie numbers between 10 and 99)
#  • allow the user 10 turns to guess the code as follows:
#    o prompt the user to enter a 2 digit number (validation is not required)
#    o calculate the number of correct digits in the correct place
#    o output a suitable message followed by the number of correct digits in the correct
#      place
#  • output a suitable message if the user has guessed the 2 digit code correctly within 10 turns
#  • output a suitable message along with the correct code if the user has had 10 turns and
#    failed to guess the code correctly.
# You should use meaningful variable name(s), correct syntax and indentation in your answer. 

import random

num = str(random.randrange(10, 100))
guess = str(input("Enter your guess (from 10 to 99): "))

count = 1
while num != guess and count <= 10:
    correct = 0
    for i in range(0, len(num)):
        if num[i] == guess[i]:
            correct += 1
    if num != guess:
        print("You got " + str(correct) + " digits in the correct place.")
        guess = input("Enter your guess: ")
        count += 1

if num == guess:
    print("You guessed correctly!")
else:
    print("You failed! The number was " + str(num))
