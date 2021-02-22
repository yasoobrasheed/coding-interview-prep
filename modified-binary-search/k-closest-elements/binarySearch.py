class Solution(object):
    def findClosestElements(self, arr, k, x):
        return self.binarySearch(arr, 0, len(arr) - k - 1, k, x)

    def binarySearch(self, arr, left, right, k, x):
        if (left > right):
            return arr[left:(left + k)]

        mid = (left + right) // 2

        if (x - arr[mid] <= arr[mid + k] - x):
            return self.binarySearch(arr, left, mid - 1, k, x)
        else:
            return self.binarySearch(arr, mid + 1, right, k, x)
