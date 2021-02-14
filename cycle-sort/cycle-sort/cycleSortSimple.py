# Where positions are equal to the numbers in the array
def cyclicSort(arr):
    # Loop through each position
    for i in range(len(arr)):
        # If the position and the number are the same, then continue
        # Otherwise keep swapping until they are the same
        while (arr[i] != i):
            val = arr[i]
            swapVal = arr[val]
            arr[val] = val
            arr[i] = swapVal

    return arr
