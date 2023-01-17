# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head
        fast = ans
        slow = ans
        for i in range(1, n + 2):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return ans.next


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
d = s.removeNthFromEnd(l1_1, 2)
while d is not None:
    print(d.val)
    d = d.next
    

            
        