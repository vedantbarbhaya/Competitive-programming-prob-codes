"""
PROBLEM : Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7, A solution set is: { [7], [2,2,3] }
"""

class Solution:
    def combinationSum(self, cand, target):
        cand.sort()
        res = []



        def helper(target,index,path):

            if target == 0:
                res.append(path)
                return

            for i in range(index,len(cand)):

                if cand[i] > target:
                    break

                else:
                    temp = target - cand[i]
                    helper(temp,i,path+[cand[i]])

        helper(target,0,[])
        return res

     
