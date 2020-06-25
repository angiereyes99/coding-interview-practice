# PROBLEM: 
# Given the array nums consisting of 2n elements 
# in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# EXAMPLE:  
# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

from typing import List

class Solution:

    # APPROACH: SPLIT ARRAYS IN HALF
    # - We just split the given arr in half
    # and add elements from the other halfs every
    # other space in our output array. In this method,
    # we assume that the arrays will always be even. 
    # And in this method, you can notice I do not use 
    # n at all. All test cases passed.
    # 
    # Runtime 52 ms
    # Memory: 14 MB
    # Faster than 99.02% of Python3 submissions.
    # Less than 100% of Python3 submissions memory usage.
    def approach(self, arr: List[int], n: int) -> List[int]:
        result = []
        # EX: nums = [2,5,1,3,4,7]
        a_half = arr[:len(arr)//2] # [2,5,1]
        b_half = arr[len(arr)//2:] # [3,4,7]
        for i in range(len(a_half)):
            result.append(a_half[i])
            result.append(b_half[i])
            # result = [a_half, b_half, ...,]
        return result




if __name__ == '__main__':
    solution = Solution()
    arr = [2,5,1,3,4,7]
    n = 3
    print(solution.approach(arr, n))