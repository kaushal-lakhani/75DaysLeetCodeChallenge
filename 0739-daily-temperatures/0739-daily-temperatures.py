class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        n = len(temp)
        d = [0]*n

        for i in range(n-1,-1,-1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            
            if stack:
                d[i] = stack[-1] - i
            
            stack.append(i)
        return d