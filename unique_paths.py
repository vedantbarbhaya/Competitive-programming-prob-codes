"""
PROBLEM - Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:

Input: m = 3, n = 2 Output: 3

Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

    Right -> Right -> Down
    Right -> Down -> Right
    Down -> Right -> Right

Example 2:

Input: m = 7, n = 3 Output: 28
"""


'''
The above problem can be recursively solved but that would require calculating some subproblems for than once
so we use memoization or dynamic programming to optimize the solution
'''
# ***************MEMOIZATION - A TOP DOWN APPROACH***************
class Solution:
    def uniquePaths(self, row: int, col: int) -> int:

        l1 = [[0 for x in range(col)] for x in range(row)]


        def helper(row,col,l1):

            if row < 0 or col < 0:
                return 0
            elif row == 0 or col == 0:
                return 1

            elif l1[row][col] > 0:
                return l1[row][col]
            else:
                l1[row][col] = helper(row-1,col,l1) + helper(row,col-1,l1)

                return l1[row][col]

        return helper(row-1,col-1,l1)


# ***************DYNAMIC PROGRAMMING - A BOTTOM UP APPROACH***************


class Solution:
    def uniquePaths(self,m,n):
        grid = [[0 for x in range(n)] for x in range(m)]

        for i in range(m):
            grid[i][0] = 1

        for i in range(n):
             grid[0][i] = 1

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]0
