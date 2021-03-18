from numba.cpython import heapq


class Solution(object):
    def frequencySort(self, s):
        numFreq = {}
        for i in range(len(s)):
            if s[i] in numFreq:
                numFreq[s[i]] += 1
            else:
                numFreq[s[i]] = 1

        heap = []
        for char, freq in numFreq.items():
            heapq.heappush(heap, (-1 * freq, char))

        finalStr = ''
        for i in range(len(heap)):
            val = heapq.heappop(heap)
            finalStr += (-1 * val[0] * val[1])

        return finalStr
