class Solution(object):
    def letterCasePermutation(self, S):
        self.permutations = []
        self.backtrack(S, 0)
        return self.permutations

    def backtrack(self, S, currIndex):
        # loop through the string checking for the first occurence of a letter
        for i in range(currIndex, len(S)):
            # if this is a letter, recurse with the upper and lowercase versions of that letter
            if (S[i].isdigit() != True):
                self.backtrack(S[:i] + S[i].lower() + S[i+1:], i + 1)
                self.backtrack(S[:i] + S[i].upper() + S[i+1:], i + 1)
                return  # return so that we don't check any other strings

        # if we've reached the end of the string, add it to the permutations array
        self.permutations.append(S)
