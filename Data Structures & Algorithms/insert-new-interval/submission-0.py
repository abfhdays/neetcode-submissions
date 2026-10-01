class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        new_start, new_end = newInterval

        for i in range(len(intervals)):
            i_start, i_end = intervals[i][0], intervals[i][1]
            
            if new_end < i_start:
                return res + [[new_start,new_end]] + intervals[i:]
            
            if new_start > i_end:
                res.append([i_start,i_end])
            
            else:
                new_start = min(i_start, new_start)
                new_end =  max(i_end, new_end)
        
        res.append([new_start, new_end])
        return res
    
        
    
            
        