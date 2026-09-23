class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = defaultdict(int)
        # {1: 1, 2: 2, 3: 3}
        # {7: 2}
        for n in nums:
            freqmap[n] += 1
        
        minheap = []
        for key,value in freqmap.items():
            heapq.heappush(minheap, (value, key))
        
        # [(1, 1), (2, 2), (3, 3)]

        while len(minheap) > k:
            heapq.heappop(minheap)
        
        res = []
        while minheap:
            _, key = heapq.heappop(minheap)
            res.append(key)
        return res

        