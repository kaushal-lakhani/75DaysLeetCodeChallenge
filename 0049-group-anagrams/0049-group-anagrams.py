class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in tracker:
                tracker[key] = []
            tracker[key].append(s)
        return list(tracker.values())