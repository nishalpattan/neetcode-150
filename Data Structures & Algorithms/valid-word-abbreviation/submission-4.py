class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_idx = 0
        abbr_idx = 0
        if word == abbr: return True

        while word_idx < len(word) and abbr_idx < len(abbr):
            num = ""
            if word[word_idx] == abbr[abbr_idx]:
                word_idx += 1
                abbr_idx += 1
                continue
            elif word[word_idx] != abbr[abbr_idx] and not abbr[abbr_idx].isdigit(): return False
            else:
                if abbr[abbr_idx] == '0': return False
                while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                    num += abbr[abbr_idx]
                    abbr_idx += 1
                word_idx += int(num)
        print(abbr_idx)
        print(word_idx)
        return abbr_idx == len(abbr) and word_idx == len(word)
                    