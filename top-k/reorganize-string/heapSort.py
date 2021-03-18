from numba.cpython import heapq


class Solution(object):
    def reorganizeString(self, S):
        # Create list of character frequencies
        freqs = {}
        for i in S:
            if i in freqs:
                freqs[i] += 1
            else:
                freqs[i] = 1

        # Place all elements into heap
        heap = [(-v, k) for k, v in freqs.items()]
        heapq.heapify(heap)

        # final list
        stringList = [''] * len(S)
        i = 0
        while (heap):
            freq, char = heapq.heappop(heap)
            while (freq != 0):
                # alternate by one until reaching end
                if (i >= len(S)):
                    i = 1

                # set value in the array
                stringList[i] = char

                # check for duplicates
                if (i != 0 and stringList[i] == stringList[i - 1]):
                    return ''

                # increment frequency and index
                freq += 1
                i += 2

        return ''.join(stringList)
