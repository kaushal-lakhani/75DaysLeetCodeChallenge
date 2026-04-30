class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        curr = 0
        longest = 0
        for i in s:
            if i-1 not in s:
                curr = 1
                while(i+1 in s):
                    curr+=1
                    i+=1
                longest=max(longest,curr)
        return longest 