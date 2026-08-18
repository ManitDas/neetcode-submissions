# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy 

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            digit_sum = l1_val + l2_val + carry
            carry = digit_sum // 10
            new_digit = digit_sum % 10

            newNode = ListNode(new_digit)
            tail.next = newNode
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

            
        