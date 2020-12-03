"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution:
    def twoSum(self, num,target):
        for i,v in enumerate(num):
            for j in range(i+1,len(num)):
                if v + num[j] == target:
                    return [i+1,j+1]



# solution using hashset
import collections
class solution():

    def twoSum(nums,target):

        d1 = collections.defaultdict(list)
        res = list()

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in d1.keys():
              res.append([d1[complement], i])
              return res

            d1[nums[i]] = i
            #print(d1[nums[i]])

        print("no solution")
