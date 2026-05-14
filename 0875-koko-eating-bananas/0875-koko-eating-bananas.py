class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def totalHrs(hr):
            h = 0
            for i in piles:
                h += math.ceil(i/hr)
            return h
        
        low, high = 1, max(piles)
        res = high

        while low <= high:
            mid = (low+high)//2

            if totalHrs(mid) <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res