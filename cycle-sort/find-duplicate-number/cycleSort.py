class Solution(object):
    def findDuplicate(self, nums):
        # Cycle Sort
        n = len(nums)
        for i in range(n):
            while (nums[i] != i + 1):
                num = nums[i]

                # If duplicate return duplicate
                if (nums[num - 1] == num):
                    return num

                nums[num - 1], nums[i] = nums[i], nums[num - 1]
        return 0
