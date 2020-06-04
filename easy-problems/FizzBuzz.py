# PROBLEM:
# Write a program that outputs the string representation of numbers from 1 to n. 
# But for multiples of three it should output “Fizz” instead of the number and 
# for the multiples of five output “Buzz”. For numbers which are multiples of 
# both three and five output “FizzBuzz”.

# EXAMPLE
'''
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''

from typing import List

class Solution:

    # APPROACH: USING REMAINDER
    # - In this method, we would have to append
    # n amounts to a list starting from 1 all the
    # way to n. Then, we would loop through the array
    # and check to see if each element is a multiple
    # of 3, 5 or both, by using x % 3 or 5 or 15 == 0.
    # We then replace elements that, with the required
    # words.
    # - Not efficient, but works.

    # Runtime: 48 ms
    # Memory: 15 MB
    # Faster than 28.72% of Python submissions
    def approach(self, n: int) -> List[str]:

        result = []

        # - We start at 1 to n
        # based on the given n
        # and append the str
        # form.
        for i in range(1, n+1):
            result.append(str(i))
        
        for nums in range(len(result)):
            
            # - 15 is first because a number
            # that is a multiple of both 5
            # and 3 will have no remainder
            # from 15.
            if int(result[nums]) % 15 == 0:
                result[nums] = 'FizzBuzz'
            elif int(result[nums]) % 3 == 0:
                result[nums] = 'Fizz'
            elif int(result[nums]) % 5 == 0:
                result[nums] = 'Buzz'
        
        return result




if __name__ == '__main__':
    solution = Solution()
    n = 15
    print(solution.approach(n))