class Solution(object):
    def generateParenthesis(self, n):
        self.combinations = []
        self.recurse('', n, n)
        return self.combinations

    def recurse(self, parens, numLeft, numRight):
        if (numLeft == 0 and numRight == 0):
            self.combinations.append(parens)
            return

        if (numLeft < numRight):
            if (numLeft != 0):
                self.recurse(parens + '(', numLeft - 1, numRight)
            self.recurse(parens + ')', numLeft, numRight - 1)
        else:
            self.recurse(parens + '(', numLeft - 1, numRight)
