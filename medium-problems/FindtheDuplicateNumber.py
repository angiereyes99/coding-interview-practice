# PROBLEM:
# Given an array nums containing n + 1 integers where each integer 
# is between 1 and n (inclusive), prove that at least one duplicate 
# number must exist. Assume that there is only one duplicate number, 
# find the duplicate one.

# EXAMPLE 1:
# Input: [1,3,4,2,2]
# Output: 2

# EXAMPLE 2:
# Input: [3,1,3,4,2]
# Output: 3

# NOTE:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

from typing import List

class Solution:

    # APPROACH 1: SORT THEN LINEAR SCAN
    # - Here, we will just sort the given array
    # and the duplicate number will be adjacent
    # to the corresponding duplicate number.

    # Runtime: 64 ms
    # Memory: 16.4 MB
    # Faster than 86.09% of Python3 solutions.
    def appraoch1(self, nums: List[int]) -> int:

        nums.sort()

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]




if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,4,2,2]
    print(solution.appraoch1(nums))