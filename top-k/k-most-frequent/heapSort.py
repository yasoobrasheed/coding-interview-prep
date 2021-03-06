from numba.cpython import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        topK = {}
        for i in range(len(nums)):
            if (nums[i] in topK):
                topK[nums[i]] += 1
            else:
                topK[nums[i]] = 1

        heap = []
        for num, freq in topK.items():
            heapq.heappush(heap, (freq, num))
            if (len(heap) > k):
                heapq.heappop(heap)

        return [elem[1] for elem in heap]
