class Solution(object):
    def searchRange(self, nums, target):
        leftBound = 0
        rightBound = len(nums) - 1
        leftSearch = self.binarySearch(
            nums, leftBound, rightBound, target, 'left')
        rightSearch = self.binarySearch(
            nums, leftBound, rightBound, target, 'right')
        return [leftSearch, rightSearch]

    def binarySearch(self, nums, left, right, target, direction):
        if (left > right):
            return -1
        mid = (left + right) / 2
        if (nums[mid] == target):
            if (direction == 'left'):
                if (mid == 0 or nums[mid - 1] != target):
                    return mid
                else:
                    return self.binarySearch(nums, left, mid - 1, target, direction)
            elif (direction == 'right'):
                if (mid == len(nums) - 1 or nums[mid + 1] != target):
                    return mid
                else:
                    return self.binarySearch(nums, mid + 1, right, target, direction)

        if (nums[mid] > target):
            return self.binarySearch(nums, left, mid - 1, target, direction)
        else:
            return self.binarySearch(nums, mid + 1, right, target, direction)
