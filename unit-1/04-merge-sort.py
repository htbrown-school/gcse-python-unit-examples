# Merge Sort - Unit 1
# Below is an example of a merge sort. Works well for larger arrays/lists and is considered fairly efficient.
# Using subroutines - see Unit 2: Example 01.

def bubble(arr):
    done = False
    while not done: # First loop - continues until all have completed.
        done = True
        for i in range(0, len(arr) - 1): # Second loop - goes through the array/list.
            if arr[i] > arr[i + 1]: # Is the current item larger than the next in the array/list.
                temp = arr[i] # Store current item in temporary variable.
                arr[i] = arr[i + 1] # Set current item to next item.
                arr[i + 1] = temp # Set next item to temporary variable.
                done = False # Not finished sort.
        print(str(arr)) # Print array/list.

def split(arr):
    mid = (len(arr - 1)) // 2
    left = arr[0:mid]
    right = arr[mid + 1:len(arr)]

    return [left, right]

def join(arr):
    final = []
    for i in len(arr) - 1:
        final = final + arr[i]
    return final

arr = [12, 9, 13, 10, 2, 4, 8, 17, 13, 28, 1, 23, 7] # Sample array/list.
arrs = []

while len(arr) > 1:
    arrs.append(bubble(split(arr)))

final = join(arrs)
print(str(final))
