"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note: Given n will always be valid.

Follow up: Can you do it in one pass?

"""

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        first = second = head

        for i in range(n):
                first = first.next

        if not first:
                return head.next

        while(first.next):
                first = first.next
                second = second.next

        second.next = second.next.next

        return head
