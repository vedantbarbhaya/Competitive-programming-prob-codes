"""
PROBLEM:
There are n oranges in the kitchen and you decided to eat some of these oranges every day as follows:

Eat one orange.
If the number of remaining oranges (n) is divisible by 2 then you can eat  n/2 oranges.
If the number of remaining oranges (n) is divisible by 3 then you can eat  2*(n/3) oranges.

You can only choose one of the actions per day.

Return the minimum number of days to eat n oranges.

Example 1:

Input: n = 10 Output: 4 Explanation: You have 10 oranges.

Day 1: Eat 1 orange, 10 - 1 = 9.

Day 2: Eat 6 oranges, 9 - 2*(9/3) = 9 - 6 = 3. (Since 9 is divisible by 3)

Day 3: Eat 2 oranges, 3 - 2*(3/3) = 3 - 2 = 1.

Day 4: Eat the last orange 1 - 1 = 0.

You need at least 4 days to eat the 10 oranges.

"""


from functools import lru_cache
class Solution:
    @lru_cache()
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n;
        return 1+ min(n % 2 + self.minDays(n // 2), 2* (n % 3) + self.minDays( n -  (2* (n % 3))    ));


# without using lru_cache() decorator, this program exceeds time limit.
# check what is lru_cache() decorator at https://docs.python.org/3/library/functools.html and https://book.pythontips.com/en/latest/function_caching.html
        
