# PROBLEM:
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
#

# Example:
# Input:
# [4,3,2,7,8,2,3,1]
# Output:
# [2,3]

from typing import List

class Solution:

    # APPROACH: SORTH THEN LINEAR SCAN 
    # - Just like in a previous duplicates problem,
    # we could just sort then once we see a repeating
    # number, we just append it to our result list and 
    # return the list that contained all duplicates. 
    # Also take in to account for edge cases.
    # 
    # Runtime: 372 ms
    # Memory: 20.8 MB
    # Faster than 84.98% of Python3 Solutions 
    # Uses less memory than 90.70% of Python3 submissions.
    def approach1(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = []

        # EDGE CASES:
        # - If input is length 1,
        # there will not be a duplicate
        # so just return empty list.
        # - If the length is 2 and both 
        # numbers are duplicates, just return
        # a list of one of them.
        if len(nums) == 1:
            return result
        elif len(nums) == 2 and nums[0] == nums[1]:
            result.append[nums[0]]
            return result

        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                result.append(nums[i])
        
        return result




if __name__ == '__main__':
    solution = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(solution.approach1(nums))