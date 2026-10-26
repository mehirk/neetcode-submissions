"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        
        old_to_new = {}

        #adding None in this hashmap so that when we look up none it doesn't return an error
        old_to_new[None] = None

        #Pass 1, filling the hash map without pointers
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        #Pass 2, now we establish the relationship within the hashmap
        curr = head
        while curr:
            cloned_node = old_to_new[curr]
            cloned_node.next = old_to_new[curr.next]
            cloned_node.random = old_to_new[curr.random]
            curr = curr.next
        
        return old_to_new[head]