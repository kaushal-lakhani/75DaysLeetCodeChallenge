class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lpro = [0]*n
        rpro = [0]*n
        fp = 1
        rp = 1

        for i in range(0,n):
            fp *= nums[i]
            rp *= nums[n-i-1]
        
            lpro[i] = fp
            rpro[n-i-1] = rp
        
        res = [rpro[1]]

        for i in range(1,n-1):
            res.append(lpro[i-1]*rpro[i+1])
        
        res.append(lpro[-2])

        return res