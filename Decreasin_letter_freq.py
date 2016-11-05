
# Given a string, sort it in decreasing order based on the frequency of characters.
# Example 1:
    # Input:
    # "tree"
    # Output:
    # "eert"

# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:

    # Input:
    # "cccaaa"

    # Output:
    # "cccaaa"

# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

    # Input:
    # "Aabb"

    # Output:
    # "bbAa"

# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

from collections import Counter
import operator

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.l_dict = Counter(s)
        self.l_sorted_list = sorted(self.l_dict.items(), key = operator.itemgetter(1), reverse = True )
        self.string =''
        for it in self.l_sorted_list:
            self.string += it[0]*int(it[1])
        s = self.string
        return s
       
        

obj = Solution()
#obj.frequencySort('tree')