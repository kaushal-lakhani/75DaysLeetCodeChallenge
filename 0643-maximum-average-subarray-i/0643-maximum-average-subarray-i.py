class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        k_sum = sum(nums[:k])
        m = k_sum
        for i in range(k, len(nums)):
            k_sum += nums[i]
            k_sum -= nums[i - k]
            m = max(m , k_sum)
        return m / k