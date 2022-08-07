# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        len1 = 0
        len2 = 0
        curr = l1
        while curr:
            sum1 += 10**(len1)*curr.val
            len1 += 1
            curr = curr.next
        curr = l2
        while curr:
            sum2 += 10**(len2)*curr.val
            len2 += 1
            curr = curr.next
        intres = sum1 + sum2
        root = ListNode(int(str(intres)[-1]))
        curr = root
        for x in str(intres)[-2::-1]:
            curr.next = ListNode(int(x))
            curr = curr.next
        return root
            
            
            
