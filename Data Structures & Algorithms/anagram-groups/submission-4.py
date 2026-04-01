class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = dict()

        for _str in strs:
            char_array = [0] * 26
            for char in _str:
                char_array[ord(char) - ord('a')] += 1
            char_tuple = tuple(char_array)
            if char_tuple in hash_map:
                hash_map[char_tuple].append(_str)
            else:
                hash_map[char_tuple] = [_str]
        return list(hash_map.values())