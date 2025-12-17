"""
LINK: https://www.geeksforgeeks.org/problems/number-of-factors1435/1
Number of factors
Difficulty: Easy    |    Accuracy: 50.86%    |    Submissions: 21K+    |    Points: 2
Find the number of factors for a given integer n.

 Examples:

Input: n = 5
Output: 2
Explanation: 5 has 2 factors 1 and 5
Input: n = 25
Output: 3
Explanation: 25 has 3 factors 1, 5, 25 
Constraints:
1 ≤ n ≤ 105

Expected Complexities
Time Complexity: O(sqrt(n)
Auxiliary Space: O(1)

"""
class Solution:  # Not Optimise
    def countFactors (self, n):
        count = 0
        for i in range(1,n//2+1):
            if n%i ==0:
                count += 1
        return count+1

# Optimise Solution
import math
class OptimiseSolution:
    def count_Factors(self, n):
        count = 0
        for i in range(1, int(math.sqrt(n))+1):
            if n%i ==0:
                if i == n//i:
                    count +=1
                else:
                    count +=2
        return count 

output = OptimiseSolution()
print(output.count_Factors(36))