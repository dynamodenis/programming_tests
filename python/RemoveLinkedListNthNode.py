    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ahead =  behind = dummy
        
        for _ in range(n+1):
            ahead = ahead.next
        print(ahead)
        print(behind)
        while ahead:
            behind = behind.next
            ahead = ahead.next
        behind.next = behind.next.next
        print(dummy)
        return dummy.next
    
"""Given the head of a linked list, remove the nth node from the end of the list and return its head."""
