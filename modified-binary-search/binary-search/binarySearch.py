class Solution(object):
    def search(self, nums, target):
        return self.binarySearch(nums, 0, len(nums) - 1, target)

    def binarySearch(self, nums, left, right, target):
        if (left == right and nums[left] != target):
            return -1

        mid = (left + right) // 2

        if (nums[mid] == target):
            return mid
        elif (nums[mid] < target):
            return self.binarySearch(nums, mid + 1, right, target)
        elif (nums[mid] > target):
            return self.binarySearch(nums, left, mid, target)
