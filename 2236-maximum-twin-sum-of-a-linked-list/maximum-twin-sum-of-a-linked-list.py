# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse second half
        current = slow
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        max_sum = 0
        fast ,slow = head, prev
        while slow:
            max_sum = max(fast.val + slow.val, max_sum)
            fast = fast.next
            slow = slow.next

        return max_sum