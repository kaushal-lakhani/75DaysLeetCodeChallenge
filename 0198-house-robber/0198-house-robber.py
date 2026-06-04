class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(ix):
            if ix == 0:
                return nums[ix]
            
            if ix < 0:
                return 0
            
            if ix in memo:
                return memo[ix]

            p = nums[ix]+dfs(ix-2)
            np = 0+dfs(ix-1)

            memo[ix] = max(np,p)
            return memo[ix]

        return dfs(len(nums)-1)