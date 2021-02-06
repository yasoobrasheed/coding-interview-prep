class Solution(object):
    def longestOnes(self, A, K):
        count1s = 0
        count0s = 0
        maxLen = 0

        i = 0
        for j in range(0, len(A)):
            if A[j] == 1:
                count1s += 1
            else:
                count0s += 1

            while (count0s > K):
                if A[i] == 1:
                    count1s -= 1
                else:
                    count0s -= 1
                i += 1

            maxLen = max(maxLen, count1s + count0s)

        return maxLen
