from numba.cpython import heapq
from math import sqrt


class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for point in points:
            # Multiply all the elements by -1 to get a Max-Heap
            # this is because you want to delete the maximum node each time
            dist = -1 * sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (dist, point))
            if (len(heap) > k):
                heapq.heappop(heap)

        return [heapPoint[1] for heapPoint in heap]
