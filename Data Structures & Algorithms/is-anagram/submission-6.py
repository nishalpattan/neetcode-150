class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
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
        '''
        '''
        # efficient way to solve the problem
        # TC : O(N), SC : O(1) using hashMaps to store the frequency of 26 letters
        if len(s) != len(t): return False
        s_hashMap = dict()
        t_hashMap = dict()
        for val in s:
            if val in s_hashMap:
                s_hashMap[val] += 1
            else:
                s_hashMap[val] = 1
        for val in t:
            if val in t_hashMap:
                t_hashMap[val] += 1
            else:
                t_hashMap[val] = 1
        for val in s:
            if s_hashMap.get(val, 0) != t_hashMap.get(val, 0):
                return False
        return True
        '''
        
        # efficient way using only array
        if len(s) != len(t): return False

        charArray = [0] * 26

        for char in s:
            charArray[ord(char) - ord('a')] += 1
        for char in t:
            charArray[ord(char) - ord('a')] -= 1

        for charIdx in charArray:
            if charIdx != 0:
                return False
        return True
        
        
        

