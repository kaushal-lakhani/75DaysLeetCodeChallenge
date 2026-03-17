class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for i in nums:
            d[i] += 1

        res = sorted(d.items(), key=lambda item: item[1], reverse=True)
        return [res[x][0] for x in range(0,k)]