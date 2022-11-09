"""
203. Remove Linked List Elements
"""

from One_Signed_List import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = head
        prev = head
        while cur:
            if cur.val == val:
                if cur == head:
                    head = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return head
