from typing import cast
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current = ListNode()
        result = current
        carry = 0

        while(l1 or l2 or carry):
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if carry:
                sum += carry 
            rest = sum % 10
            carry = sum // 10

            current.next = ListNode(rest)
            current = current.next

        return result.next
    def printListNodeAsList(self, res: Optional[ListNode]) -> None:
        while res:
            print(res.val, end="")
            res = res.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(7)


s = Solution()

s.printListNodeAsList(s.addTwoNumbers(l1, l2))