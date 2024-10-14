# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Initiate a dummy node and slow fast to it 
increment the fast pointer by n steps
now start incrementing slow and fast together 

when loops end slow will be just one point before desored point ot be reomved 

inititate the next to next pointer for slow and isolate the point to bne removed
"""


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        slow=fast= dummy
        #increment fast already n steps ahead
        for _ in range(n):
            fast = fast.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next


        return dummy.next
        