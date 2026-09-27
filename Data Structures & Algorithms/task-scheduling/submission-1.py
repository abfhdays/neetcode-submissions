class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # leastInterval(tasks = ["A","A","A","B","C"], n = 3) -> 9
        time = 0
        count = Counter(tasks)
        maxHeap = [(-1 * count[tsk], tsk) for tsk in count.keys()]
        heapq.heapify(maxHeap)
        # [(-3, 'A'), (-1, 'B'), (-1, 'C')]
        q = deque() # [(cooldown_left, task)] [((3, 3, A)(4, 1, B)(5, 1, C)]
        
        while maxHeap or q:
            time += 1
            if q and time > q[0][0]:
               tc, cnt, tsk = q.popleft()
               heapq.heappush(maxHeap, (cnt, tsk))

            if maxHeap:
                cnt, tsk = heapq.heappop(maxHeap)
                cnt += 1
                if cnt < 0:
                    q.append((time + n, cnt, tsk))
            
        return time
