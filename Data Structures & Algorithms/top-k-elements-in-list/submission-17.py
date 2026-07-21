class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val = {}
        for i in nums:
            if i in val:
                val[i] += 1
            else:
                val[i] = 1
        
        sorted_val = sorted(val.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_val[:k]]