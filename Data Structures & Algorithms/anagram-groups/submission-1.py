class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        TC : O(m * n) where m in length of strs and n is the longest length of str in strs
        SC : O(m) for hashMap as it stores atleast m distinct keys
        '''
        hashMap = dict()
        for _str in strs:
            charArray_List = [0] * 26
            for char in _str:
                charArray_List[ord(char) - ord('a')] += 1
            charArray_Tuple = tuple(charArray_List)
            if charArray_Tuple in hashMap:
                hashMap[charArray_Tuple].append(_str)
            else:
                hashMap[charArray_Tuple] = [_str]
        return hashMap.values()