"""
328. Odd Even Linked List
"""

from One_Signed_List import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        even = head.next
        even_head = even
        while(even and odd and even.next and odd.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = even_head
        return head
