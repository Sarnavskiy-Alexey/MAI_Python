"""
160. Intersection of Two Linked Lists
"""

from One_Signed_List import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB

        while a is not b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next

        return a
