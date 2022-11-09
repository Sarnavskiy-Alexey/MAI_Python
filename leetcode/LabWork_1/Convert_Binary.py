"""
1290. Convert Binary Number in a Linked List to Integer
"""

from One_Signed_List import ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        st = ''
        while head:
            st += str(head.val)
            head = head.next
        return int(st, 2)
