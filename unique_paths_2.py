"""
PROBLEM :Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input: [ [0,0,0], [0,1,0], [0,0,0] ]

Output: 2

Explanation: There is one obstacle in the middle of the 3x3 grid above. There are two ways to reach the bottom-right corner:

    Right -> Right -> Down -> Down
    Down -> Down -> Right -> Right

"""

# *************SOLUTION USING DP*****************************

class Solution:
    def uniquePathsWithObstacles(self, grid):

        row = len(grid)
        col = len(grid[0])
        # print(row,col)

        def helper(grid,row,col):
            ans = [[0 for x in range(col)] for x in range(row)]

            if grid[0][0] == 1:
                return 0

            ans[0][0] = 1

            for i in range(1,col):
                if grid[0][i] != 1:
                    ans[0][i] =  ans[0][i-1]
                else:
                    ans[0][i] = 0

            for i in range(1,row):
                if grid[i][0] != 1:
                    ans[i][0] =  ans[i-1][0]
                else:
                    ans[i][0] = 0



            for i in range(1,row):
                for j in range(1,col):
                     if grid[i][j] != 1:
                            ans[i][j] = ans[i-1][j] + ans[i][j-1]
                     else:
                        ans[i][j] = 0

            # print(ans)
            return ans[row-1][col-1]



        return helper(grid,row,col)
