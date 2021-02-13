class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        intersections = []
        i = 0
        j = 0
        while (i < len(firstList) and j < len(secondList)):
            intervalOne = firstList[i]
            intervalTwo = secondList[j]

            if (intervalOne[0] <= intervalTwo[1] and intervalOne[1] >= intervalTwo[0]):
                intersections.append(
                    [max(intervalOne[0], intervalTwo[0]), min(intervalOne[1], intervalTwo[1])])

            if (intervalOne[1] < intervalTwo[1]):
                i += 1
            elif (intervalTwo[1] < intervalOne[1]):
                j += 1
            else:
                i += 1
                j += 1

        return intersections
