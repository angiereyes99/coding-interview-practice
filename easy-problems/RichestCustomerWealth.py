# Problem
# You are given an m x n integer grid accounts where accounts[i][j] 
# is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

# EXAMPLES:
# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.
# Example 2:

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.

from typing import List

class Solution:

    # APPROACH: USE SUM AND MAX
    #  - We create an empty list to append
    #    the sum of each list in the accounts.
    #    We then just return the max of that list
    #    to get the wealthiest customer.
    #
    # Runtime: 44 ms
    # Memory: 14.3 MB
    # Faster than 98.42% of Python 3 submissions
    # Time complexity: O(N) 
    # We check the list once, and sum() and max() have
    # a time complexity of O(N).
    def approach(self, accounts: List[int] ) -> int:

        sum_of_each_list = []

        for lists in accounts:
            sum_of_each_list.append(sum(lists))
        
        return max(sum_of_each_list)




if __name__ == '__main__':
    solution = Solution()
    accounts = [[1,2,3],[3,2,1]]
    print(solution.approach(accounts))