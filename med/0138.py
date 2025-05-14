
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

        #attempt 2:
        # loop through original list to make hashmap, oldnode:newnode with val done, next & random not done
        # loop original list again, from each original node find the new node, update next & random using hashmap

        nodemap = {None:None} #handle nulls 

        cur = head
        #first loop
        while cur:
            nodemap[cur] = Node(cur.val)
            cur = cur.next


        #second loop
        #now we add in next and random
        cur = head
        while cur:
            new = nodemap[cur]
            new.next = nodemap[cur.next]
            new.random = nodemap[cur.random]
            cur = cur.next
        
        return nodemap[head]