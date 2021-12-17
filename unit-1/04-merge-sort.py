# Merge Sort - Unit 1
# Below is an example of a merge sort. Works well for larger arrays/lists and is considered fairly efficient.
# Using subroutines - see Unit 2: Example 01.

def mergeSort(arr): # Main function
    if len(arr) > 1: # Check the array/list to begin - if the length is 1 then it doesn't need to split
        mid = len(arr) // 2  # Find the midpoint
        left = arr[:mid] # Define the left side
        right = arr[mid:] # Define the right side

        mergeSort(left) # Sort the left side (iteration with functions)
        mergeSort(right) # Sort the right side (iteration with functions)

        i = 0 # Iteration initialisation
        j = 0
        k = 0

        while i < len(left) and j < len(right): # While statement to sort both arrays/lists together.
            if left[i] < right[j]: # Sorting
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
            k = k + 1
            print(arr)
        while i < len(left): # While statement to sort single array/list.
            arr[k] = left[i]
            i = i + 1
            k = k + 1
        while j < len(right):
            arr[k] = right[j]
            j = j + 1
            k = k + 1

    return arr

arr = [12, 15, 32, 12, 5, 2, 4, 3, 9, 14]
sortedArr = mergeSort(arr)
print("Final array/list:", str(sortedArr))