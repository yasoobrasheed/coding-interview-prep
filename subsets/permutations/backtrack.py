class Solution(object):
    def permute(self, nums):
        # Set global array to store permutations
        self.permutations = []
        # Start recursion
        self.recurse(nums, 0)
        return self.permutations

    def recurse(self, currArray, swapIndex):
        # Base Case: If we've made all possible swaps, add the array and return out
        if (len(currArray) == swapIndex):
            self.permutations.append(currArray)

        # If not, keep looping through the array
        for i in range(swapIndex, len(currArray)):
            # Duplicate array to avoid shallow copy overwriting
            copyArray = currArray[:]
            # Swap
            copyArray[swapIndex], copyArray[i] = copyArray[i], copyArray[swapIndex]
            # Recurse to swap combinations of the other indices
            self.recurse(copyArray, swapIndex + 1)
