class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = {}
        currLen = 0
        maxLen = 0
        j = 0
        for i in range(0, len(s)):
            if (s[i] not in chars):
                chars[s[i]] = 1
            elif (s[i] in chars):
                chars[s[i]] += 1
                while (chars[s[i]] != 1):
                    chars[s[j]] -= 1
                    if (chars[s[j]] == 0):
                        del chars[s[j]]
                    j += 1
            maxLen = max(maxLen, len(chars))
        return maxLen
