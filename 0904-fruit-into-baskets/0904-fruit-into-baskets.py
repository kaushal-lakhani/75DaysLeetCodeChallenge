class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm = defaultdict(int)
        left = 0
        ans = 0
        picked = 0

        for right in range(len(fruits)):
            if hm[fruits[right]] == 0:
                picked += 1
            hm[fruits[right]] += 1

            while picked > 2:
                hm[fruits[left]] -= 1
                if hm[fruits[left]] == 0:
                    picked -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans