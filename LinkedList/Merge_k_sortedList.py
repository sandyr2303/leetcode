# Definition for singly-linked list.
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode(0)
        ans = dummy
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        while list1:
            dummy.next = list1
            list1 = list1.next
            dummy = dummy.next

        while list2:
            dummy.next = list2
            list2 = list2.next
            dummy = dummy.next

        return ans.next 

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        i = 0
        last = len(lists) - 1
        j = last
        while  last != 0:
            i = 0
            j = last
            while i < j:
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j
        return lists[0]

s = Solution()
l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(4)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(1)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

l3_1 = ListNode(1)
l3_2 = ListNode(3)
l3_3 = ListNode(4)
l3_1.next = l3_2
l3_2.next = l3_3

ans = s.mergeKLists([l1_1, l2_1, l3_1])
while ans:
    print(ans.val)
    ans = ans.next