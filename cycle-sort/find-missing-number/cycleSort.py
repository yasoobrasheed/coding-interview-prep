class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        # Loop through the nums
        for i in range(n):
            # If the number equals the index continue, else start swapping
            while nums[i] != i:
                num = nums[i]
                # If the number is outside of the bounds of the array, there's nothing you can do, break
                # This number will keep shifting until it reaches the missing number's index
                if num == n:
                    break
                nums[i], nums[num] = nums[num], nums[i]

        # Look for the place where the index is messed up
        for i in range(n):
            if (nums[i] != i):
                return i

        # Return the length of the list
        return n
