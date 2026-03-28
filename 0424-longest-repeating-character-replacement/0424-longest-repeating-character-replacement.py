class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sx, ex = 0, 0
        char = defaultdict(int)
        n = len(s)
        res = 1

        while ex < n:
            char[s[ex]] += 1
            max_key = max(char, key=char.get)
            if ((ex-sx+1) - char[max_key]) <= k:
                res = max(res, (ex-sx+1))
            else:
                char[s[sx]] -= 1
                sx += 1
            ex += 1

        return res