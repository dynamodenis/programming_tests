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
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    
    dummy = ListNode(0, head)

    leftPrev, cur = dummy, head

    for i in range(left-1):
        leftPrev = cur
        cur = cur.next

    prev = None
    for i in range(right-left + 1):
        tempNext = cur.next
        cur.next = prev
        prev = cur
        cur = tempNext
    
    print(f"leftprev {leftPrev}")
    print(f"current {cur}")

    print(f'CUR {cur}')
    print(f"Prev {prev}")
    leftPrev.next.next = cur
    leftPrev.next = prev

    print(f"dummny next {dummy.next}")
    return dummy.next


        
