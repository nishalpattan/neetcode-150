class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        char_array_map = defaultdict(list)

        # TC : O(k), k is total chars in inputs strs
        # TC : O(n), n is total strs in inputs

        for _str in strs:
            char_array = [0] * 26
            for idx in range(len(_str)):
                char_array[ord(_str[idx]) - ord('a')] += 1

            tuple_char_array = tuple(char_array)
            if tuple_char_array in char_array_map:
                char_array_map[tuple_char_array].append(_str)
            else:
                char_array_map[tuple_char_array] = [_str]
        return list(char_array_map.values())
