"""
PROBLEM

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8 Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6 Output: [-1,-1]

Example 3:

Input: nums = [], target = 0 Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):



        # edge cases where no of ele = 0 or 1
        ret = [-1,-1]

        if len(nums) == 0:
            return ret

        if target < nums[0] or target > nums[-1]:
            return ret

        print("Target" ,target)

        # actual code
        start = 0
        end = len(nums)-1


        while(start < end):
              print("Start",start)
              print("end",end)

              mid = (start + end) // 2

              print("mid",mid)
              print("mid ele",nums[mid])
              print()


              if nums[mid] < target:
                  start = mid + 1
              else:
                  end = mid

        if(nums[start]!=target):
            return ret
        else:
          ret[0] = start

        print("\nFinal start before right",start)



        # do not have set start = 0 this time
        end = len(nums)-1

        while(start < end):
              print("Start",start)
              print("end",end)

              mid = (start + end) // 2 + 1

              print("mid",mid)
              print("mid ele",nums[mid])
              print()

              if nums[mid] > target:
                  end = mid - 1
              else:
                  start = mid


        ret[1] = end
        return ret
