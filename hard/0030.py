class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sublen = len(words[0])
        starting = []
        conlen = sublen * len(words)

        for i, chr in enumerate(s):
            if i + conlen > len(s):
                break
            elif s[i:i + sublen] in words:
                #check if it is valid
                temp = words.copy()
                p = i
                valid = True
                while len(temp) != 0 and valid:
                    substr = s[p:p + sublen]
                    if substr in temp:
                        temp.remove(substr)
                        p += sublen
                        if len(temp) != 0 and p >= len(s):
                            valid = False
                    else:
                        valid = False
                if valid:
                    starting.append(i)
        return starting
