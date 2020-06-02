# PROBLEM: Given an array nums of n integers where n > 1,  
#          return an array output such that output[i] is equal 
#          to the product of all the elements of nums except nums[i].

# EXAMPLE: 
# Input: [1,2,3,4]
# Output: [24,12,8,6]

# Constraint: It's guaranteed that the product of 
#             the elements of any prefix or suffix 
#             of the array (including the whole array) 
#             fits in a 32 bit integer.

# Note: Please solve it without division and in O(n).

from typing import List

class Solution:

    # INITIAL APPROACH (NAIVE SOLUTION):
    # - You can simply loop through the 
    # first array and get the product of
    # every element. Then you can divide by 
    # each nuber and store that quotient in the output array.

    # --> [1,2,3,4] = 24
    # Loop to each element -> 24/1 -> 24/2 -> 24/3 -> 24/4
    # Store each value in an array -> [24, 12, 8 ,6]

    # - However, we are NOT allowed to use division, and this method does
    # not take into account of 0's in  an array.

    # Time Complexity: O(2n)
    def approach1(self, nums: List[int]) -> List[int]:
        
        result = 1
        output = []
        for x in nums: # O(n)
            result = result * x

        for i in range(len(nums)): # O(2n)
            output.append(int(result / nums[i]))
            
        return output
    


    # SECOND APPROACH:
    # - For the current nums[i], we want to get the product
    # of its left and right side. We then want to multiply
    # the products of the left and right, then store it in
    # out output array. If there is no left or right side,
    # we will set the value to 1.

    # -> [1,2,3,4], nums[i] = 1
    #    left = 1, Since there is no left side.
    #    right = 24, (2 * 3 * 4)
    # - Therefore, left * right = 24 -> nums = [24]
    # - We keep repeating this til we reach the end of the list.


    def approach2(self, nums: List[int]) -> List[int]:

        left_products = []
        right_products = []
        output = []

        for i in range(len(nums)):
            left_products.append(i)
            right_products.append(i)
        
        # - As mentioned, the start and end
        # of the list will equal 1 since 
        # there will be no number for the
        # opposite side of the list.
        left_products[0] = 1
        right_products[len(nums) - 1] = 1

        # Left side
        for i in nums[0:]:
            left_products.append(nums[i - 1] * left_products[i - 1])
        
        # Right side
        for i in range(len(nums)-2, 0, -1):
            right_products.append(nums[i + 1] * right_products[i + 1])

        for i in nums:
            output.append(left_products[i] * right_products[i])

        return right_products



if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4]
    #print(solution.approach1(nums))
    print(solution.approach2(nums))