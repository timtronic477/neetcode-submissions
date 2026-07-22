class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        
        vals = sorted(seen.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in vals[:k]]
        