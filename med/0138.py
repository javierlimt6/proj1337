
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        #for loop to add next pointers
        #add each node to a list for easy retrieval
        #loop again to assign random pointers
        #space O(n) time O(n)

        # new = new Node(head.val, head.next, )
        # cur = head
        # while cur.next:

        #FAILED

        pass