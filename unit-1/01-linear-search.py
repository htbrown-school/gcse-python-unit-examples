# Linear Search - Unit 1
# Below is an example of a linear search algorithm. It works for any array/list.

arr = [2, 6, 2, 3, 5, 9] # Sample short array/list.
searchTerm = int(input("Enter the value to search for: ")) # Store the term required in a variable.

# Iteration initialisation (while loop).
found = False
count = 0

while not found and count < len(arr): # While loop to check through until the term is found or we reach the end of the array/list.
    if arr[count] == searchTerm: # Check the search term against the array.
        found = True
    else:
        count += 1

if found: # Finalise by printing a result.
    print("Search term found at position " + str(count))
else:
    print("Search term not found.")
