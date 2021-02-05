class Solution(object):
    def totalFruit(self, tree):
        # Keep hashmap of fruits, maxFruit count, and i and j window indices
        fruits = {}
        maxFruit = float('-inf')
        j = 0
        # Add fruits to the hashmap until there are 3 fruits in the hashmap
        for i in range(0, len(tree)):
            if (tree[i] not in fruits):
                fruits[tree[i]] = 1
            else:
                fruits[tree[i]] += 1

            # if there are three fruits, delete from the beginning
            # until one of the fruits disappears
            while (len(fruits) > 2):
                if (fruits[tree[j]] > 0):
                    fruits[tree[j]] -= 1
                    if (fruits[tree[j]] == 0):
                        del fruits[tree[j]]
                j += 1

            maxFruit = max(maxFruit, i - j + 1)

        return maxFruit
