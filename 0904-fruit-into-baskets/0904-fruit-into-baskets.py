class Solution:
    def totalFruit(self, frt: List[int]) -> int:
        basket = {}
        sx,ex = 0,0
        n = len(frt)
        mx = 0

        while ex<n:
            basket[frt[ex]] = ex
            
            if len(basket) > 2:
                t = frt[sx]
                sx = basket[frt[sx]]+1
                del basket[t]
            if len(basket) <= 2:
                mx = max(mx, ex-sx+1)
            ex += 1
        return mx