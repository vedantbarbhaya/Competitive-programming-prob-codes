"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?

Example 1:

Input: nums = [2,0,2,1,1,0] Output: [0,0,1,1,2,2]

Example 2:

Input: nums = [2,0,1] Output: [0,1,2]

Example 3:

Input: nums = [0] Output: [0]

Example 4:

Input: nums = [1] Output: [1]
"""


lass Solution:
    def sortColors(self, nums):


        # set start = 0, index = 0 and end = last element index
        start,end, index = 0, len(nums) - 1 , 0

        if len(nums) == 0 or len(nums) ==1:
            return

        while(index <= end and start <= end):

            # if the current element is 0, it should come at first so we swap curr element and
            # the element at the start. If you see closely, start always points to the index
            # where the next 0 should come. we increment index as well because we have already
            # seen the element that is coming at index from start as start is always equal to
            # less than index.

            if nums[index] == 0:
                nums[index] = nums[start]
                nums[start] = 0 # same as nums[start] = nums[index]

                index+=1
                start+=1

            # if the current element is 2, it should come at last so we swap curr element and
            # the element at the end. We dont increment index because we dont what the element
            # that we swapped from end was. It might be a 0 or it might be a 2 and so we will
            # have to swap that again if that is the case.


            elif nums[index] == 2:
                nums[index] = nums[end]
                nums[end] = 2 # same as nums[end] = nums[index]

                end-=1

            else:
                index+=1
