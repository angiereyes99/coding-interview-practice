# PROBLEM:
# Given an integer number n, return the 
# difference between the product of its 
# digits and the sum of its digits.

# EXAMPLE: 
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

from typing import List

class Solution:

    # APPROACH 1: BRUTE FORCE
    # - We can create n to be a list
    # and multiply and sum up all the 
    # numbers in the list. The we just
    # return product - sum.

    # Runtime: 32 ms
    # Memory: 14 MB
    # Faster than 45.25% of Python submissions
    def approach1(self, n: int) -> int:

        n = list(map(int, str(n)))
        n_product = 1
        n_sum = 0

        for num in n:
            n_product = n_product * num
            n_sum = n_sum + n
        
        return n_product - n_sum
    

    # APPROACH 2: HELPER METHODS
    # - Using a product and sum helper method
    # uses good OOP principle practice and even
    # inreases speed in this case. While not 
    # the most optimal solution,it is an 
    # improvement from approach 1.

    # Runtime: 28 ms
    # Memory: 13.8 MB 
    # Faster than 75.48% of Python submissions.
    def approach2(self, n: int) -> int:

        # HELPER METHOD: Product of n
        def Nproduct(n):
            n = list(map(int, str(n)))
            n_product = 1

            for x in n:
                n_product = n_product * x
            return n_product
        
        # HELPER METHOD: Sum of n
        def Nsum(n):
            n = list(map(int, str(n)))
            n_sum = 0

            for x in n:
                n_sum = n_sum + x
            return n_sum
    
        return Nproduct(n) - Nsum(n)




if __name__ == '__main__':
    solution = Solution()
    n = 234
    print(solution.approach2(n))