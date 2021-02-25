class Solution(object):
    def subsets(self, nums):
        self.subsets = []
        self.backtrack(nums, [], 0)
        return self.subsets

    def backtrack(self, nums, currArray, currIndex):
        self.subsets.append(currArray[:])
        for i in range(currIndex, len(nums)):
            self.backtrack(nums, currArray + [nums[i]], i + 1)
