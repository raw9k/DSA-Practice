"""
LINK: https://www.geeksforgeeks.org/problems/palindrome-string0817/1
You are given a string s. Your task is to determine if the string is a palindrome. A string is considered a palindrome if it reads the same forwards and backwards.

Examples :

Input: s = "abba"
Output: true
Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
Input: s = "abc" 
Output: false
Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
Constraints:
1 ≤ s.size() ≤ 106
The string s contains only lowercase english letters (a-z).
"""





class Solution:
    def isPalindrome(self, s):
        def helper(l, r):
            if l >= r:
                return True
            if s[l] != s[r]:
                return False
            return helper(l + 1, r - 1)
        return helper(0, len(s) - 1)
    
output = Solution()
print(output.isPalindrome("ABABBABA"))