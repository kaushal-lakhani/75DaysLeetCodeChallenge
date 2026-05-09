class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n = len(nums2)
        mp = defaultdict(lambda : -1)

        for i in range(n):

            while stack and stack[-1] < nums2[i]:
                fr = stack.pop()
                mp[fr] = nums2[i]
            
            stack.append(nums2[i])

        return [mp[x] for x in nums1]