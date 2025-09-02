from tempfile import tempdir


def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next #Store current.next in next_node. (This saves the rest of the list before we break the link).
        curr.next = prev #Change current.next to point to prev. (This is the actual reversal step).
        prev = curr #Move prev one step forward: prev = current.
        curr = next_node #Move current one step forward: current = next_node.
        
        return prev
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

"""
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    
    # Create a dummy node to handle edge cases where start is at 1 and we do not have prev none node
    dummy = ListNode(0, head)

    leftPrev, cur = dummy, head

    # Iterate on the left nodes and update the values
    for i in range(left-1):
        leftPrev = cur
        cur = cur.next

    # Reverse from point left to right which is right - left + 1 positions
    # cur = left and leftPrev = node before left
    #reverse from left to right
    prev = None
    for i in range(right-left + 1):
        tempNext = cur.next
        cur.next = prev
        prev = cur
        cur = tempNext
    
    # Update pointers start and last or left and right
    leftPrev.next.next = cur
    leftPrev.next = prev

    return dummy.next


        
