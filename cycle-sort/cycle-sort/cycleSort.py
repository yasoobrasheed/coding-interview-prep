def cycleSort(arr):

    # Keep track of the number of writes
    writes = 0

    # Find all cycles from element starting at each index of arr
    for cycleStart in range(0, len(arr) - 1):

        # Element and index of element at cycleStart
        chosenElem = arr[cycleStart]
        index = cycleStart

        # Loop through all proceeding elements searching for those
        # which are smaller than the chosenElem
        for i in range(cycleStart + 1, len(arr)):
            elem = arr[i]
            # Find the position to place the element
            if (elem < chosenElem):
                index += 1

        # If there are no smaller numbers, continue
        if (index == cycleStart):
            continue

        # Put in front of a duplicate then write
        while chosenElem == arr[index]:
            index += 1

        # Write: swap elements while writing
        arr[index], chosenElem = chosenElem, arr[index]
        writes += 1

        # Start swapping until we reach the cycleStart of the list
        while index != cycleStart:
            index = cycleStart

            # Loop through all proceeding elements searching for those
            # which are smaller than the chosenElem
            for i in range(cycleStart + 1, len(arr)):
                elem = arr[i]
                # Find the position to place the element
                if (elem < chosenElem):
                    index += 1

            # Place item or put in front of a duplicate
            while chosenElem == arr[index]:
                index += 1

            # Swap elements
            arr[index], chosenElem = chosenElem, arr[index]
            writes += 1

    return arr, writes
