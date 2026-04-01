class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s and t are empty => true
        # s and t of different length => false
        # s or t is empty => false
        # are all in lowercase => yes

        # approach 1: using 2 hashMaps and compare counts of char in\
        # both if same keep continue else return false
            # this approach has TC: O(n) SC: O(n)

        # approach 2: leveraging the use of unicode point of char
                        # by ord(char) - ord('a') incrementing through one string
                        # decrementing through another string
                        # total sum of array should be 0
                        # TC : O(n) SC: O(1) as the list length is 26 which is constant
        
        if len(s) != len(t): return False
        if len(s) == 0 or len(s) == 0: return True
        if len(s) == 0 and len(t) == 0: return True

        n = len(s)
        char_array = [0] * 26
        
        for idx in range(n):
            print(idx)
            char_array[ord(s[idx]) - ord('a')] += 1
            char_array[ord(t[idx]) - ord('a')] -= 1
        
        for val in char_array:
            if val != 0:
                return False
        return True
        

