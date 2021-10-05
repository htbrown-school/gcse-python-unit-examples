# Trace Tables - Unit 2
# Use a trace table to work out the purpose of this algorithm.

amount = int(input("Enter amount: "))
total = 0
count = 0

for i in range(0, amount + 1):
    if i % 2 == 0:
        total = total + i**2
        count = count + 1

print("Average:", round(total / count, 2))
print("Total:", total)

# (outputs the average of squares of even numbers between 0 and a given number)