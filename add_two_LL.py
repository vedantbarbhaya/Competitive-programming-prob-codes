"""
2 numbers are given in reverse order in 2 seperate Linkedlist. Ex 2->9>1 and 5->6->2. Add them and store the result in a new Linkedlist
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''

        l1 : ListNode
        l2 : ListNode
        rtype: ListNode

        '''

        finalSum = ListNode(0)
        finalSumTail = finalSum
        carry = 0

        while l1 or l2 or carry:

            if l1 and l2:
                Sum = l1.val + l2.val + carry
                if Sum >= 10:
                    Sum = Sum%10
                    carry = 1
                else:
                    carry = 0

            elif l1:
                Sum = l1.val + carry
                if Sum >= 10:
                    Sum = Sum % 10
                    carry = 1
                else:
                    carry = 0

            elif l2:
                Sum = l2.val + carry
                if Sum >= 10:
                    Sum = Sum % 10
                    carry = 1
                else:
                    carry = 0

            elif carry:
                Sum = carry
                if Sum >= 10:
                    Sum = Sum % 10
                    carry = 1
                else:
                    carry = 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            finalSumTail.val = Sum
            finalSumTail.next = ListNode(0) if l1 or l2 or carry else None
            finalSumTail = finalSumTail.next

        return finalSum

        
