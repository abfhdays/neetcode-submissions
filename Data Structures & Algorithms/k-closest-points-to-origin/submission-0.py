class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x, y in points:
            heapq.heappush(distances, (-1 * math.sqrt((x * x) + (y * y)), [x, y]))
        while len(distances) > k:
            heapq.heappop(distances)
        
        res = []

        for x, y in distances:
            res.append(y)
        
        return res