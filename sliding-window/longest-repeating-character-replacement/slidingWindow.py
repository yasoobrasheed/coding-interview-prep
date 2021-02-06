class Solution(object):
    def characterReplacement(self, s, k):
        # Keep track of the counts
        counts = {}
        maxCountType = 0  # Save key of maxCount
        maxCount = 0  # Save value of maxCount

        maxLen = 0  # Save best possible window

        i = 0  # i = Pointer 1, j = Pointer 2
        for j in range(0, len(s)):
            # Add character to counts dict
            if (s[j] not in counts):
                counts[s[j]] = 1
            else:
                counts[s[j]] += 1

            # If we have a new maxCount, keep track of the key and value
            if (counts[s[j]] > maxCount):
                maxCount = counts[s[j]]
                maxCountType = s[j]

            # If window - mode > k, then our window is too big
            if ((j - i + 1) - maxCount > k):
                # Shrink window by 1
                counts[s[i]] -= 1

                # If first element was the maxCountType, update the maxCount (subtract 1)
                if (counts[s[i]] == maxCountType):
                    maxCount -= 1

                if (counts[s[i]] == 0):
                    del counts[s[i]]
                i += 1

            # Record the window size
            maxLen = max(maxLen, (j - i + 1))

        return maxLen
