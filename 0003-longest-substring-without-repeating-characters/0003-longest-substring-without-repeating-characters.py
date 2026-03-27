class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        l = 1
        sx, ex = 0,0
        ix = 0
        n = len(s)

        while ix < n:
            if s[ix] in s[sx : ex]:
                sx += 1
            else:
                ex += 1
                ix += 1
            l = max(l, ex-sx)
        
        return l