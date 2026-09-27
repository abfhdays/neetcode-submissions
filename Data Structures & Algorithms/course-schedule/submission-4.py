class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {}
        indegree = {course: 0 for course in range(numCourses)}
        for course, prereq in prerequisites:
            if prereq not in adjlist:
                adjlist[prereq] = [course]
            else:
                adjlist[prereq].append(course)
            indegree[course] += 1

        print(adjlist)
        print(indegree)
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        completed = 0
        while q:
            node = q.popleft()
            completed += 1
            for nei in adjlist.get(node, []):
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
    
        return completed == numCourses
