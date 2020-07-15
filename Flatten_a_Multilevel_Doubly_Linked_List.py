# You are given a doubly linked list which in addition to the next and previous pointers, it could have a child pointer, which may or may not point to a separate doubly linked list. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure, as shown in the example below.

# Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the head of the first level of the list.

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
      # approach: recursively flatten rest list and child list
        #           when meet a child pointer

        # find the node that contains child
        pointer = head
        while pointer and not pointer.child:
            pointer = pointer.next

        if pointer:
            # find child tail and connect with rest head if it exists
            child_tail = pointer.child
            while child_tail.next:
                child_tail = child_tail.next

            rest_head = self.flatten(pointer.next)
            if rest_head:
                child_tail.next = rest_head
                rest_head.prev = child_tail

            # connect pointer with child
            child_head = self.flatten(pointer.child)
            pointer.next = child_head
            child_head.prev = pointer
            pointer.child = None

        return head
      
