class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}

        for ix,ele in enumerate(nums):
            if target-ele in rem:
                return [ix, rem[target-ele]]
            rem[ele] = ix