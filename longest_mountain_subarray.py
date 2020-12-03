"""
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]

(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5] Output: 5 Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

Example 2:

Input: [2,2,2] Output: 0 Explanation: There is no mountain.

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000

Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space?
"""



# the idea in the below code is to find peaks one by one and once we find a peak, expand towards both the sides to find the left and right boundaries of
# mountain made by that peak. If the length of that mountain is greater than the mountain formed using any previous peak, store that length.


class Solution:
    def longestMountain(self, A, res = 0):

        for i in range(1, len(A) - 1):

            if A[i + 1] < A[i] > A[i - 1]: #  find the peaks one by one
                left = right = i

                # once we have the peak, expand towards both sides
                while left and A[left] > A[left - 1]:
                  left -= 1

                while right + 1 < len(A) and A[right] > A[right + 1]:
                  right+= 1

                if right - left + 1 > res:
                  res = right - left + 1
        return res
