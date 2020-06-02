# PROBLEM:
# Given the array of integers nums, 
# you will choose two different indices 
# i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

# EXAMPLE: 
# Input: nums = [3,4,5,2]
# Output: 12 
# Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
# you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.

# # EXAMPLE 2:
# Input: nums = [1,5,4,5]
# Output: 16
# Explanation: Choosing the indices i=1 and j=3 (indexed from 0), 
# you will get the maximum value of (5-1)*(5-1) = 16.

from typing import List

class Solution:

    # APPROACH: SORT THEN MULTIPLY LAST 2
    # - This approach is simple as it only sorts the given array. 
    # Then all you hae to do is return the final two elements in 
    # the array based on the algo they give. We do the last two 
    # because since it is asking fo the max product, the last two 
    # numbers will be the biggest numbers in the array when sorted.

    # Runtime: 48 ms
    # Memory: 14 MB
    # Faster than 96.85% of Python3 submissions.
    def approach(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[len(nums) - 2] - 1) * (nums[len(nums) - 1] - 1)




if __name__ == "__main__":
    solution = Solution()
    nums = [3, 4, 5, 2]
    print(solution.approach(nums))