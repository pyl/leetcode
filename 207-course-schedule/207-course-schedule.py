class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # first, convert to adjacency list
        hm = defaultdict(list)
        for x in prerequisites:
            hm[x[0]].append(x[1])
            
        visited = set()
        visitedgood = set()
        def dfs(node):
            if node in visitedgood:
                return True
            if node in visited:
                return False
            visited.add(node)
            for x in hm[node]:
                if dfs(x) == False:
                    return False
            visited.remove(node)
            visitedgood.add(node)
            hm[node] = []
            return True
        for x in prerequisites:
            if dfs(x[0]) == False:
                return False
        return True