"""
Problem - longest substring without repetition in a string
"""


class Solution:
    def lengthOfLongestSubstring(self, s):

        dicts = {}
        maxlength = start = 0

        for i,ch in enumerate(s):

            if ch in dicts:
                sums = dicts[ch] + 1

                if sums > start:
                    start = sums

            num = i - start + 1

            if num > maxlength:
                maxlength = num

            dicts[ch] = i

        return maxlength
