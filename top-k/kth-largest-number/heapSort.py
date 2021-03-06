from numba.cpython import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            # Popping from the heap makes the algorithm much faster
            if (len(heap) > k):
                heapq.heappop(heap)

        return heap[0]
