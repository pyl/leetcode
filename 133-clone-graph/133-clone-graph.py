"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        hm = dict()
        if node == None:
            return None
        def dfs(node):

            nn = Node(node.val)
            hm[node] = nn
            for x in node.neighbors:
                if x in hm:
                    nn.neighbors.append(hm[x])
                else:
                    nn.neighbors.append(dfs(x))
            return nn
        return dfs(node)
    
    # you start with one node. You create a node copy. You save references to all its neighbors. I
    # Iterate through the original. For all neighbors in the original, add as neighbors to the corresponding node in the hashmap. 
    
    # How to deal with cycles? Have a set. Than way, 
    
    # create a hashmap from one node to another node