class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = defaultdict(list)
        for x in prerequisites:
            hm[x[0]].append(x[1])
        visited = set()
        visitedgood = set()
        
      
        
        res = []
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
            res.append(node)
            hm[node] = []
            return True
        for x in range(numCourses):
            if dfs(x) == False:
                return []
        return res
            
            
        
        

        