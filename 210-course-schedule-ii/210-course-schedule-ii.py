class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hm = defaultdict(list)
        for x in prerequisites:
            hm[x[0]].append(x[1])
        visited = set()
        
        res = []
        added = set()
        def dfs(node):
            if hm[node] == []:
                if node not in added:
                    added.add(node)
                    res.append(node)
                return True
            if node in visited:
                return False
            visited.add(node)
            for x in hm[node]:
                if dfs(x) == False:
                    return False
            visited.remove(node)
            if node not in added:
                added.add(node)
                res.append(node)
            hm[node] = []
            return True
        for x in range(numCourses):
            if dfs(x) == False:
                return []
            if x not in added:
                added.add(x)
                res.append(x)
        return res
            
            
        
        

        