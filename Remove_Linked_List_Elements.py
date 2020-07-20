# Remove all elements from a linked list of integers that have value val.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        pointer=head
        while pointer:
            if pointer.next and pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        if head and head.val==val:
            head=head.next
        return head
