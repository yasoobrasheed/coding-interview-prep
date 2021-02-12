class Solution(object):
    def insert(self, intervals, newInterval):
        # Edge case
        if (len(intervals) == 0):
            return [newInterval]

        # Keep track of the newIntervals
        # Loop until you find the first place to insert the new interval
        newIntervals = []
        i = 0
        for interval in intervals:
            if (interval[1] < newInterval[0]):
                newIntervals.append(interval)
                i += 1
            else:
                break
        newIntervals.append(newInterval)

        # Run merge intervals on the newest interval added
        while (i < len(intervals)):
            currInterval = intervals[i]
            prevInterval = newIntervals[-1]
            if (prevInterval[1] >= currInterval[0]):
                newIntervals[-1] = [min(currInterval[0], prevInterval[0]),
                                    max(currInterval[1], prevInterval[1])]
            else:
                newIntervals.append(currInterval)
            i += 1

        return newIntervals
