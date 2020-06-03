# PROBLEM: 
# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
# Return the number of negative numbers in grid.

# EXAMPLE:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negative number in the matrix.

from typing import List

class Solution:

    # APPROACH 1: BRUTE FORCE
    # - We just loop to each list and loop again
    # to each item in the lists and check to see
    # which ones are less than 0. Then we add to
    # out counter variable and return the counter
    # when every item is checked.

    # Runtime: 136 ms
    # Memory: 14.8 MB
    # Faster than 28.41% of Python submissions.
    def approach1(self, grid: List[int]) -> int:

        counter = 0

        for list in grid:
            for i in list:
                if i < 0:
                    counter += 1
        
        return counter




if __name__ == '__main__':
    solution = Solution()
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    print(solution.approach1(grid))