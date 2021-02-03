class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        lst = [float("-inf")] * (n + 1)

        for i in range(0, n):
            currNum = nums[i]
            lst[i + 1] = max(lst[i] + currNum, currNum)

        return max(lst)
