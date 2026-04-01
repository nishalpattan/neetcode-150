class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        char_array_s = [0] * 26
        char_array_t = [0] * 26
        for idx in range(len(s)):
            char_s = s[idx]
            char_t = t[idx]
            char_array_s[ord(char_s) - ord('a')] += 1
            char_array_t[ord(char_t) - ord('a')] += 1
        return char_array_s == char_array_t
