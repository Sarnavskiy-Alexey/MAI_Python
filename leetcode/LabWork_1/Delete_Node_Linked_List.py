"""
237. Delete Node in a Linked List
"""

from One_Signed_List import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next
