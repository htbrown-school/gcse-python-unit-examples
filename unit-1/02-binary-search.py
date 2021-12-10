# Binary Search - Unit 1
# Below is an example of a binary search algorithm. It works on ordered arrays/lists.
# Using subroutines - see Unit 2: Example 01.

def binarySearch(arr, searchTerm, start, end):
    if (end < start):
        return False
    
    mid = 1 + (start + end) // 2
    if searchTerm == arr[mid]:
        return mid
    elif searchTerm < arr[mid]:
        return binarySearch(arr, searchTerm, start, mid - 1)
    else:
        return binarySearch(arr, searchTerm, mid - 1, end)

arr = [1, 2, 3, 6, 9, 11, 14, 18, 27]
searchTerm = int(input("Enter the value to search for: "))

result = binarySearch(arr, searchTerm, 0, len(arr) - 1)
if not result:
    print("Search term not found.")
else:
    print("Search term found at position " + str(result))


