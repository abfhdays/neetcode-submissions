class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {c: [] for c in range(numCourses)} # {prereq: courses}
        indegree = {course: 0 for course in range(numCourses)}
        for course, prereq in prerequisites:
            adjlist[prereq].append(course)
            indegree[course] += 1

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        # q = [0, 2]
        completed = 0
        res = []
        while q:
            node = q.popleft()
            res.append(node)
            completed += 1
            for nei in adjlist.get(node, []):
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if completed == numCourses:
            return res
        else:
            return []
