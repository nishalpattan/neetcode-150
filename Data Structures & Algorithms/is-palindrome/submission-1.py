class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr_s = list()
        nums = "0123456789"
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in s:
            if char in nums or char in chars:
                arr_s.append(char)
        left = 0
        right = len(arr_s) - 1
        while left <= right:
            if arr_s[left] != arr_s[right]:
                return False
            left +=1
            right -=1
        return True