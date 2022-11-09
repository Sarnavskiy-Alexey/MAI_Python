"""
2095. Delete the Middle Node of a Linked List
"""

from One_Signed_List import ListNode


class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head.next:
            return head.next
        tur = head
        rab = head
        while rab.next:
            tur = tur.next
            rab = rab.next
            if rab.next:
                rab = rab.next
        if tur.next:
            tur.val = tur.next.val
            tur.next = tur.next.next
        else:
            head.next = None
        return head
