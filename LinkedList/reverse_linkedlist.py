#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        
        # node = None 
        # while head is not None:
        #     next = head.next
        #     head.next = node
        #     node = head
        #     head = next
        # return node
    
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev



s = Solution()
l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_4 = ListNode(4)
l1_5 = ListNode(5)
l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5
d = s.reverseList(l1_1)
while d is not None:
    print(d.val)
    d = d.next


