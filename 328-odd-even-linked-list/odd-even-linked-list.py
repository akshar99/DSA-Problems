# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        even_half = ListNode(None)
        odd_half = ListNode(None)
        odd = odd_half
        even = even_half

        move = head
        counter = 1
        
        while move:
            if counter % 2 !=0:
                odd.next = move
                odd =odd.next
            else:
                even.next = move
                even  = even.next
            move = move.next
            counter += 1

        even.next = None

        odd.next = even_half.next

        return odd_half.next