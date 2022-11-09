"""
2181. Merge Nodes in Between Zeros
"""

from One_Signed_List import ListNode


class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            if cur.val == 0:
                summ = 0
                tmp = cur
                cur = cur.next
                while cur and cur.val != 0:
                    summ += cur.val
                    cur = cur.next
                tmp.val = summ
                if cur.next:
                    tmp.next = cur
                else:
                    tmp.next = None
                    break
        return head
