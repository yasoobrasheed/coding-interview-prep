class Solution(object):
    def maxSubArray(self, nums):
        return self.maxSubArrayRecursive(nums, 0, len(nums) - 1)

    def maxSubArrayRecursive(self, nums, left, right):
        if (left == right):
            return nums[left]
        middle = (left + right) / 2
        return max(self.maxCrossingSum(nums, left, middle, right),
                   self.maxSubArrayRecursive(nums, left, middle),
                   self.maxSubArrayRecursive(nums, middle + 1, right))

    def maxCrossingSum(self, nums, left, middle, right):
        maxLeftSum = float('-inf')
        leftSum = 0
        for i in range(middle, left - 1, -1):
            leftSum += nums[i]
            maxLeftSum = max(maxLeftSum, leftSum)

        maxRightSum = float('-inf')
        rightSum = 0
        for i in range(middle + 1, right + 1):
            rightSum += nums[i]
            maxRightSum = max(maxRightSum, rightSum)

        return max(maxLeftSum + maxRightSum,
                   maxLeftSum,
                   maxRightSum)
