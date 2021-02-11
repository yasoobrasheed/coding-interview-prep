class Solution(object):
    def merge(self, intervals):
        # Sort intervals
        intervals.sort()

        # Instantiate previous interval list
        mergedIntervals = [intervals[0]]
        i = 1
        while (i < len(intervals)):
            # Compare to last merged interval and next merged interval
            lastInterval = mergedIntervals[-1]
            currInterval = intervals[i]

            # Check for overlap, if there is an overlap, merge the intervals by taking min and max of both
            if (currInterval[0] <= lastInterval[1]):
                start = min(currInterval[0], lastInterval[0])
                end = max(currInterval[1], lastInterval[1])
                mergedIntervals[-1] = [start, end]
            # If no overlap, add the new interval to the mergedInterval list
            else:
                mergedIntervals.append(currInterval)

            # Iterate to the next interval
            i += 1

        return mergedIntervals
