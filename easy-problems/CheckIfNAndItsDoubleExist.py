# PROBLEM: Given an array arr of integers, 
#          check if there exists two integers 
#          N and M such that N is the double of M ( i.e. N = 2 * M).

# EXAMPLE:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

from typing import List

class Solution:

    # APPROACH 1: NAIVE SOLUTION
    # - In this solution, we are just creating 
    # a seperate list that contains all the 
    # multiples of 2 of each int in the list. 
    # And if the arr has one of the multiples 
    # in the products lst, it will return True.
    # - However, this wil not work when considering 0 
    # b/c 0 * 2 = 0. And if the arr has 0 and products 
    # list has 0, it will return True. But this should 
    # return False because [1,2,0] does not have another 0.

    # -> arr = [10, 2, 5, 3]
    # New list -> products = [20, 4, 10, 6] True

    # 103/104 TEST CASES PASSED IN TERMS OF LEETCODE
    def approach1(self, arr: List[int]) -> bool:
        
        products = []
        zeros = []

        for i in range(len(arr)):
            products.append(arr[i] * 2)
        
        for i in range(len(arr)):
            for j in range(len(products)):
                if arr[i] == products[j]:
                    return True

        return False

    # APPROACH 2: TWO POINTERS
    # - A working solution, but not efficient. 
    # We just use two pointers, one starting from 
    # i and another startig at i+1. We then just
    # check to see if arr[i] == arr[i+1] * 2 
    # or arr[i+1] / 2.

    # Runtime: 88 ms
    # Memory: 13.8 MB
    def approach2(self, arr: List[int]) -> bool:
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] == (arr[j] * 2) or arr[i] == (arr[j] / 2):
                    return True
        
        return False



if __name__ == "__main__":
    solution = Solution()
    arr = [10,2,5,3]
    print(solution.approach2(arr))