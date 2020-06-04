# PROBLEM: 
# Given a binary array, find the maximum 
# number of consecutive 1s in this array.

# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#         The maximum number of consecutive 1s is 3.

from typing import List

class Solution:

    # APPROACH: MAX AND COUNTER VARIABLES 
    # - This method has us initialize a max and counter
    # variable, both starting at 0. As we loop through
    # the whole array, we will increment our counter by
    # 1 everytime we see the number '1'. Then if we see 
    # a '0', we will reset counter to 0. and then we will
    # check if our counter is greater than our max and 
    # return the max of the last highest count.

    # Runtime: 75.45%
    # Memory: 14 MB
    # Faster than 75.45% of Python Submissions.
    def approach(self, nums: List[int]) -> int:

        max = 0
        counter = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
            else: 
                counter = 0
            
            if counter > max:
                max = counter

        return max




if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,0,0,1,1,1,1,0,1,1]
    print(solution.approach(nums))