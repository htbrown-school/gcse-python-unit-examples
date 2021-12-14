# Binary Search - Unit 1
# Below is an example of a binary search algorithm. It works on ordered arrays/lists.
# Using subroutines - see Unit 2: Example 01.

def binarySearch(arr, searchTerm, start, end):
    if (end < start): # Check to see if the end value is smaller than the start variable - if it is the requested value hasn't been found.
        return False
    
    mid = 1 + (start + end) // 2 # Find the middle index.
    if searchTerm == arr[mid]: # Is this the requested value?
        return mid
    elif searchTerm < arr[mid]: # If it's larger than the requested value
        return binarySearch(arr, searchTerm, start, mid - 1) # Run the function again - form of iteration. Change variables to reflect the new array/list.
    else:
        return binarySearch(arr, searchTerm, mid + 1, end)

arr = [1, 2, 3, 6, 9, 11, 14, 18, 27] # Sample array/list.
searchTerm = int(input("Enter the value to search for: "))

result = binarySearch(arr, searchTerm, 0, len(arr)) # Call the function first.
if not result:
    print("Search term not found.")
else:
    print("Search term found at position " + str(result))


