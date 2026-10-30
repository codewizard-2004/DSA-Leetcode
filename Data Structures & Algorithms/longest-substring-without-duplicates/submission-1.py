class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        mem = {}
        for r in range(len(s)):
            if s[r] in mem:
                l = max(l, mem[s[r]] + 1)

            mem[s[r]] = r
            res = max(res, r - l +1)

        return res  

        