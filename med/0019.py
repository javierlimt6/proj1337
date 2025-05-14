# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        cur = head
        while cur.next:
            after = cur.next
            after.prev = cur
            cur = after
        if head == cur:
            return None
        for i in range(n):
            if cur == head:
                return head.next
            cur = cur.prev
        cur.next = cur.next.next
        return head

# comments: not wrong implementation but could have been better