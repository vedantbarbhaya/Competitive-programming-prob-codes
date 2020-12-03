"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4] Output: 6 Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1] Output: 0 Explanation: The result cannot be 2, because [-2,-1] is not a subarray
"""


"""
APPROACH:
As the subarrays have to be continuous, the intuition here is that when we traverse the array, at any given position, we have to maintain a max and min number where max is the max product of the elements before the current position and min is the minimum product of the elements before the current position. If the current position is a negative number, and min product is also a negative number, there are high chances that their product will be a very large positive number so we maintain min product. Now the output can also be a single number, meaning a single element of the array so we need to take the max of ele at curr pos, (ele at curr pos * max_prod), and (ele at curr pos * min_prod).
"""


def maxProduct(l1):
    r = l1[0]
    print("intially r = " + str(r))
    imax = r
    imin = r

    for i in range(1,len(l1)):
          print("imax = " + str(imax))
          print("imin = " + str(imin))

          if(l1[i] < 0):
            imax,imin = imin,imax


          imax = max(l1[i], imax * l1[i])
          imin = min(l1[i], imin * l1[i])

          print("after upd imax = " + str(imax))
          print("after upd imin = " + str(imin))


          r = max(r, imax);
          print("global r = " + str(r))

    print(r)
