"""
Print all possible combinations of a string
"""

class AllPossComb():
    def __init__(self):
        self.ans = []

    def perm(self,s):
        if len(s) == 1:
            #print(s)
            return [s]

        self.ans = []
        for i,v in enumerate(s):
            substr = s[:i] + s[i+1:]
            self.ans +=([v + x for x in self.perm(substr)])

        #print(self.ans)
        return self.ans
        
