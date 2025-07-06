class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        if s == "":
            return 0
        count = Counter()
        i = 0
        res = 0
        for j, char in enumerate(s):
            #increase first, then adjust i accordingly
            count[char] += 1
            while i < j and k + count.most_common(1)[0][1] < (j - i + 1):
                count[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            
        return res
    

soln = Solution()
print(soln.characterReplacement("AABABBA", 1))