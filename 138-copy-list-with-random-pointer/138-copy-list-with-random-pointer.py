"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hm = dict()
        def clone(node):
            if node == None:
                return None
            if node in hm:
                return hm[node]
            new = Node(node.val)
            hm[node] = new
            new.next = clone(node.next)
            new.random = clone(node.random)
            return new
        return clone(head)
