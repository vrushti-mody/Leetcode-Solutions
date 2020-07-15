# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head == None or head.next ==None:
            return head
        head1=head
        head2,head2_beg= head.next,head.next
        while head2.next!= None and head2.next.next!= None:
            head1.next = head2.next
            head2.next = head2.next.next
            head1 = head1.next
            head2 = head2.next
        if head2.next!=None:
            head1.next = head2.next
            head1 = head1.next
        head1.next = head2_beg
        head2.next = None
        return head
