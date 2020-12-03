"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (s == '' or len(s) < 1):
            return ""

        # boundaries for final substring and we will adjust them based on return values from
        # expandAroundCenter method
        end = 0
        start = 0

        for center in range(0,len(s)):

            len1 = self.expandAroundCenter(s, center, center);    #this is for cases like aabaa
            len2 = self.expandAroundCenter(s, center, center+1);  #this is for cases like aabbaa

            stlen = max(len1,len2)
            # with this stlen we got our longest palidromic substring for that iteration
            # so now we adjust our boudaries accordinly

            # start and end will be at half the length of ss from the center on either sides
            if (stlen > end - start):

                    start = center - int((stlen - 1) / 2)
                    end = int(center + stlen / 2)

        return s[start: end + 1]

    def expandAroundCenter(self,s,left,right):
        if (s == '' or left > right):
            return 0

        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left-=1
            right+=1
        return right - left - 1;
        
