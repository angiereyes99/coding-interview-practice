# PROBELM: Given an array of integers, 
#          return indices of the two numbers 
#          such that they add up to a specific target.
#
#          You may assume that each input would have 
#          exactly one solution, and you may not use 
#          the same element twice.

# EXAMPLE:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List

class Solution:

    # APPROACH 1: BRUTE FORCE
    # - Use one pointer to check current nums[i]
    # then use another pointer to check each 
    # index one by one, until the current + second ptr = target
    # Once you find the target sum, return those indices.
    # - Works, but highly inefficient!
    # - Inneficient because we cannot assume that
    # the array provided is going to be small. 
    # We must assume that the array given 
    # can go up to something like 100000 elements. 

    # Runtime: 5924 ms
    # Memory: 14.9 MB
    # Time Complexity: O(n^2)
    def approach1(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


    # APPROACH 2: USING A HASHMAP
    # - We can figure out the complement by
    # target - nums[i]. And this should be 
    # equal to nums[j].
    # - Now, instead of searching the entire array,
    # we can just store complements in our 
    # hashmap. Since, hashmaps have constant
    # retrieval, this will drastically improve
    # out time complexity.
    # - We check if there is a matching pair, then
    # we will return the pair. If not, we just add
    # the keys to our HashMap.

    # Runtime: 44 ms
    # Memory: 15.3 MB
    # Time Complexity O(n)
    def approach2(self, nums: List[int], target: int) -> List[int]:
        
        compMap = dict()

        for i in range(len(nums)):
            comp = target - nums[i]
            num = nums[i]
            if num in compMap:
                return [compMap[num], i]
            else:
                compMap[comp] = i




if __name__ == "__main__":
    solution = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    # print(solution.approach1(nums, target))
    print(solution.approach2(nums, target))