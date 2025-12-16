"""
LINK: https://leetcode.com/problems/reverse-integer/description/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-2^31 <= x <= 2^31 - 1
"""

class Solution(object):
    def reverse(self,x):
        rev = 0
        temp = x
        is_pos = True
        if x>0:
            is_pos = False
        temp = abs(x)
        while temp>0:
            rem = temp%10
            rev = rev *10 + rem
            temp = temp//10

        if rev < (-(21**31)) or rev > (2**31 - 1):
            return 0
        return -rev if is_pos else rev


# REMOVE BELOW LINES WHILE SUBMISSION   
result = Solution()
enter = int(input("Enter a digit to reverse: "))
print("Your Input integer is",enter,"and it's reverse is: " ,result.reverse(enter)) 


"""
Its a medium level question from Leetcode so i couldn't solve on first time and needed to saw dry run of solution.


Time complexity is O(log10 (n))
Space complexity is O(1)
"""