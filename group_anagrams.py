"""
PROBLEM: Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],

Output: [ ["ate","eat","tea"], ["nat","tan"], ["bat"] ]

Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

#USING HASHING CONCEPT
# when we sort characters of anagrams, it will give us the same result. This can be
# used as a key to bin the anagrams from a given list

import collections
class Solution:
    def groupAnagrams(self, strs):

        d1 = collections.defaultdict(list)

        for i in strs:
            d1[tuple(sorted(i))].append(i)

        ans = []
        for key in d1.keys():
            ans.append(d1[key])

        return ans


# another solution will be add the ascii values of each word. Anagrams will have
# the same ascii value.
# we use ord(char) functi
class Solution:
    def groupAnagrams(self, strs):
        d = {}
        for i in strs:
            val = 0
            for j in i:
                val = val + ord(j)
            if val not in d.keys():
                d[val] = []
            d[val].append(i)

        print(d.values())
