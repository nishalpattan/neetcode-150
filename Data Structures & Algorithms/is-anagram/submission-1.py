class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len not same return False
        # naive solution, sort and compare both strings 
        # TC : O(n logn), SC : O(n)
        if len(s) != len(t):
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for idx in range(len(s)):
            if s[idx] != t[idx]:
                return False
        return True