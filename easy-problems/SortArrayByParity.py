# PROBLEM: 
# Given an array A of non-negative integers, return an array 
# consisting of all the even elements of A, followed by all 
# the odd elements of A.
# You may return any answer array that satisfies this condition.

# EXAMPLE: 
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

from typing import List

class Solution:

    # APPROACH: COMBINE 2 LIST
    # - In this approach we can create and 'evens'
    # and 'odds' list. Then we can itterate through 
    # the given input list and store numbers either
    # in the evens list or odds list based on whether
    # or not A[i] % 2 == 0. Then we can return the 
    # list concatenated together.
    
    # Runtime: 72 ms
    # Memory: 14.8 MB
    # Faster than 98.15% of Python Submissions.
    def approach(self, A: List[int]) -> List[int]:

        evens = []
        odds = []

        for num in range(len(A)):
            if A[num] % 2 == 0:
                evens.append(A[num])
            else:
                odds.append(A[num])
        
        # - If you want, you can have
        # the lists sorted as well for
        # output clarity.
        # evens.sort()
        # odds.sort()
        return evens + odds




if __name__ == '__main__':
    solution = Solution()
    A = [3,1,2,4,7,8,9,15]
    print(solution.approach(A))