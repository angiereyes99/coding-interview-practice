# PROBLEM:
# Given a non-negative integer num, return the number of steps 
# to reduce it to zero. If the current number is even, you have 
# to divide it by 2, otherwise, you have to subtract 1 from it.

 
# EXAMPLE:
# Input: num = 14
# Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.

class Solution:

    # APPROACH: WHILE LOOP TIL 0
    # - We will keep the while loop going
    # until n is == 0. In the while loop
    # we will check everytime if the current
    # num is even or odd.

    # Runtime: 20 ms
    # Memory: 13.9 MB
    # Faster than 98.43% of Python3 submissions.
    def approach(self, n: int) -> int:
        count = 0
        while n != 0:
            if n % 2 == 0:
                n = n / 2
            else:
                n = n -1
            count += 1
        return count




if __name__ == '__main__':
    solution = Solution()
    n = 14
    print(solution.approach(n))