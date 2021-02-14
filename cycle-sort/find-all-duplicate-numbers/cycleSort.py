class Solution(object):
    def findDuplicates(self, nums):
        # Cycle Sort
        n = len(nums)
        for i in range(n):
            while (nums[i] != (i + 1)):
                num = nums[i]
                # If there is a duplicate let that duplicate accumulate
                if (num == nums[num - 1]):
                    break
                    # Swap number with the index of that number
                nums[i], nums[num - 1] = nums[num - 1], nums[i]

        # Complex way of deleting the numbers that are in the right place
        # (you could also use a filter instead of this)
        # Replaces the indexes that are duplicates with the number
        # that was supposed to be there
        currIndex = 0
        i = 0
        while (i < n):
            if (nums[currIndex] == (i + 1)):
                del nums[currIndex]
            else:
                currIndex += 1
            i += 1

        return nums
