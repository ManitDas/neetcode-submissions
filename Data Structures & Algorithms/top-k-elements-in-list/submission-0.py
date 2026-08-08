class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counts = {}
        for num in nums: 
            counts[num] = counts.get(num, 0) + 1
        
        buckets = [[] for _ in range(n+1)]
        for num, freq in counts.items():
            buckets[freq].append(num)

        result = []
        for i in range(n, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result