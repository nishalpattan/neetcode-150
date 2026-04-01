class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        min_len = float("inf")
        min_str = ""
        common_prefix = ""
        curr_prefix = ""
        
        for _str in strs:
            if len(_str) < min_len:
                min_len = len(_str)
                min_str = _str

        for idx in range(min_len):
            for _str in strs:
                if _str[idx] != min_str[idx]:
                    return min_str[:idx]
        return min_str