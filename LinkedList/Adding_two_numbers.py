# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        head = ListNode(0)
        curr = head
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sum = carry + x + y
            carry = sum // 10
            curr.next = ListNode(sum % 10)
            curr = curr.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
s = Solution()
l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(9)
l1_1.next = l1_2
l1_2.next = l1_3
l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3
d = s.addTwoNumbers(l1_1, l2_1)
while d is not None:
    print(d.val)
    d = d.next
