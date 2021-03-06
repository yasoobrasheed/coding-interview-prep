class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        self.subsets = []
        self.recurse(nums, [], 0)
        return self.subsets

    def recurse(self, nums, currentArray, currIndex):
        self.subsets.append(currentArray)
        for i in range(currIndex, len(nums)):
            if i > currIndex and nums[i-1] == nums[i]:
                continue
            self.recurse(nums, currentArray + [nums[i]], i + 1)
