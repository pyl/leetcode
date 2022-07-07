class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # detect if there is a cycle in the fucking thing
        edgeset = set()
        hm = { i : [] for i in range(numCourses) }
        for l in prerequisites:
            hm[l[0]].append(l[1])
        
        visitedSet = set()
        def dfs(node):
            # base case
            if hm[node] == []:
                return True
            if node in visitedSet:
                return False
            visitedSet.add(node)
            for x in hm[node]:
                if dfs(x) == False:
                    return False
            hm[node] = []
            visitedSet.remove(node)
            return True
        
        for x in hm:
            if dfs(x) == False:
                return False
        return True
        