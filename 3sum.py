"""
Written sets of 3 numbers from a given array whose sum is equal to 0
"""

class Solution:
    def threeSum(self, nums):
        self.nums = nums.sort()
        ans = set()


        for i in range(0,len(nums)-2):
            sol = []
            j = len(nums)-1
            k = i+1

            if i > 0 and nums[i] == nums[i-1]:
              continue


            while(k<j):
                sol = []
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    sol.extend([nums[i],nums[j],nums[k]])
                    sol1 = tuple(sol)
                    ans.add(sol1)

                    while k < j and nums[k] == nums[k+1]:
                      k = k + 1
                    while k < j and nums[j] == nums[j-1]:
                      j = j - 1

                    k+=1
                    j-=1

                elif sum > 0:
                    j = j-1
                elif sum < 0:
                     k= k + 1

        return (list(ans))
