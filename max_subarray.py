"""
PROBLEM - Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4], Output: 6 Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution:
    def maxSubArray(self, nums):


        dp = [None for x in range(len(nums))]

        dp[0] = nums[0]
        for i in range(1,len(nums)):

                temp = dp[i-1] + nums[i]

                if dp[i] == None:
                    dp[i] = temp
                elif dp[i] <= temp:
                    dp[i] = temp

                if dp[i] < nums[i]:
                    dp[i] = nums[i]

        dp.sort()
        return(dp[-1])


# kadane's algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        curr_sum = max_sum = nums[0]
      =
        for i in range(1,len(nums)):

          # curr_sum basically acts like an accumulator
          # we do max(nums[i],nums[i] + curr_sum) because if nums[i] + curr_sum , nums[i], we want to start a new subarray from nums[i]
            curr_sum = max(nums[i], nums[i] + curr_sum)
            max_sum = max(curr_sum,max_sum)

        return max_sum
