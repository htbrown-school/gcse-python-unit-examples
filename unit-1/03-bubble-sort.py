# Bubble Sort - Unit 1
# Below is an example of a bubble sort algorithm. Works well for a small list, but not considered very efficient.

arr = [12, 9, 13, 10, 2, 4, 8] # Sample array/list.
done = False # Have all the passes completed?

while not done: # First loop - continues until all have completed.
    done = True
    for i in range(0, len(arr) - 1): # Second loop - goes through the array/list.
        if arr[i] > arr[i + 1]: # Is the current item larger than the next in the array/list.
            temp = arr[i] # Store current item in temporary variable.
            arr[i] = arr[i + 1] # Set current item to next item.
            arr[i + 1] = temp # Set next item to temporary variable.
            done = False # Not finished sort.
    print(str(arr)) # Print array/list.
    