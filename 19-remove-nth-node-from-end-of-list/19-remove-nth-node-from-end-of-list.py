# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        curr = head
        #find len
        length = 0
        while curr:
            length += 1
            curr = curr.next
        curr2 = head
        curr2x = head.next
        if n == length:
            return head.next
        
        for _ in range(length - n - 1):
            curr2 = curr2.next
            curr2x = curr2x.next
        curr2.next = curr2x.next
        return head
            