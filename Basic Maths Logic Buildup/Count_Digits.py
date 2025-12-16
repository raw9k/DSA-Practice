'''
LINK = https://www.naukri.com/code360/problems/number-of-digits_4538242

Problem statement
Ninja want to add coding to his skill set so he started learning it. On the first day, he stuck to a problem in which he has given a long integer ‘X’ and had to count the number of digits in it.

Ninja called you for help as you are his only friend. Help him to solve the problem.

EXAMPLE:
Input: 'X' = 2

Output: 1

As only one digit is ‘2’ present in ‘X’ so answer is ‘1’.
'''

def countDigit(n: int) -> int:
   count = 0
   temp = n
   while temp>0:
      temp = temp//10
      count = count+ 1
   return count
output = countDigit(3535)
print(output)

"""
Time complexity is here O(log 10 (n))
Space Complexity is O(1)


Additional remarks: Remove all imports from the code when your are submitting your code in coding ninja platform
"""