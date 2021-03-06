class Solution(object):
    def subsets(self, nums):
        self.subsets = []
        self.recurse(nums, [], 0)
        return self.subsets

    def recurse(self, nums, currArray, currIndex):
        self.subsets.append(currArray[:])
        for i in range(currIndex, len(nums)):
            self.recurse(nums, currArray + [nums[i]], i + 1)
