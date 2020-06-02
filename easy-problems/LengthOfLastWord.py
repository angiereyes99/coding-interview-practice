# PROBLEM:
# Given a string s consists of upper/lower-case alphabets 
# and empty space characters ' ', return the length of last 
# word (last word means the last appearing word if we loop 
# from left to right) in the string.

# If the last word does not exist, return 0.

# EXAMPLE:
# Input: "Hello World"
# Output: 5

class Solution:

    # APPROACH: SPLIT STRING TO LIST
    # - All we do in this method is split the string
    # and put each word in a list. Then we retrieve the 
    # length of the last word in the list.

    # -> "Hello World"
    # -> using split() -> ["Hello", "World"]

    # Runtime: 24 ms
    # Memory: 13.9 MB
    # Faster than 90.71% of Python3 Submissions
    def approach(self, s: str) -> int:

        word_list = s.split()
        
        if len(s) == 0 or len(word_list) == 0:
            return 0
        return (len(word_list[-1]))




if __name__ == "__main__":
    solution = Solution()
    word1 = "Hello World"
    word2 = ""
    word3 = "        "
    print(solution.approach(word1))
    print(solution.approach(word2))
    print(solution.approach(word3))