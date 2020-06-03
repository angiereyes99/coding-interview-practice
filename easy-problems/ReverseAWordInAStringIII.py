# PROBLEM:
# Given a string, you need to reverse the order of 
# characters in each word within a sentence while still 
# preserving whitespace and initial word order.

# EXAMPLE: 
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

from typing import List

class Solution:

    # APPROACH: STRING -> LIST 
    # - In this approach, we just convert the string
    # to a list of different s using split()
    # the we can itterate through the list an reverse
    # each word on it's own. then we can convert back
    # to a string at the return statement.

    # s = "Let's take LeetCode contest"
    # -> ["Let's", "take", "LeetCode", "contest"]

    # Runtime: 28 ms
    # Memory: 14 MB
    # Faster thn 91.12% of submissions
    def approach(self, s: str) -> str:

        s = list(s.split())

        for word in range(len(s)):
            s[word] = s[word][::-1]
        
        return ' '.join(s)




if __name__ == '__main__':
    solution = Solution()
    s = "Let's take LeetCode contest"
    print(solution.approach(s))