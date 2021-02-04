class Solution(object):
    def minSubArrayLen(self, s, nums):
        # Edge case
        n = len(nums)
        if (n == 0):
            return 0

        # Keep track of the minLen, the total sum, and a start and end pointer (i, j)
        minLen = float('inf')
        sumNumsSoFar = 0
        i = 0

        # Move end pointer through the list
        for j in range(0, n):

            # Add to the total sum
            sumNumsSoFar += nums[j]

            # If we've reached the 'recording' point, attempt to remove from the front
            # and see what minLen we can achieve
            if (sumNumsSoFar >= s):
                while (sumNumsSoFar >= s):
                    sumNumsSoFar -= nums[i]
                    i += 1

                # Maintain the successful length by adding back the last element and decrementing start
                # record the minLen that gives us the length we want
                i -= 1
                sumNumsSoFar += nums[i]
                minLen = min(minLen, j - i + 1)

        if (minLen == float('inf')):
            return 0
        return minLen
