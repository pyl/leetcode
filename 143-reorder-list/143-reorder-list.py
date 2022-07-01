# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = []
        curr = head
        while curr:
            l.append(curr)
            curr = curr.next
        for i,x in enumerate(l[:((len(l))//2)]):
            print(i)
            pl = i
            pr = len(l) - 1 - i
            l[pl].next = l[pr]
            l[pr].next = l[pl + 1]
        l[(len(l))//2].next = None