# PROBLEM: Given two strings s and t , 
#          write a function to determine 
#          if t is an anagram of s.

# EXAMPLE: 
# Input: s = "anagram", t = "nagaram"
# Output: true

# EXAMPLE:
# Input: s = "rat", t = "car"
# Output: false

class Solution:

    # APPROACH 1: USE SORTING
    # - Simply just sort the letters in both the given
    # strings and compare the two after they are sorted.
    # If they equal to eachother, then they are anagrams.

    # Runtime: 44 ms
    # Memory: 14.7 MB
    # Time Complexity: O(nlgn)
    def approach1(self, s: str, t: str) -> bool:
        # - An obvious indicator that the strings are not anagrams
        # are if they are not the same length. So check to see if they
        # are first.
        return len(s) != len(t) or sorted(s) == sorted(t)

    # APPROACH 2: USE A HASMAP
    # Runtime: 44 ms
    # Memory: 14.1 MB
    # Time Complexity: O(n)
    def approach2(self, s: str, t: str) -> bool:

        h = {}

        for ch in s:
            if ch not in h:
                h[ch] = 0
            h[ch] += 1
        
        for ch in t:
            if ch not in h:
                h[ch] = 0
            h[ch] -=1
        
        for key in h.keys():
            if h[key] != 0:
                return False
        
        return True




if __name__ == "__main__":
    solution = Solution()
    s1 = "anagram"
    s2 = "nagaram"
    print(solution.approach2(s1, s2))

    s3 = "rat"
    s4 = "car"
    print(solution.approach2(s3, s4))