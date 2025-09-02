# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(f"head {head}")
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,3,4,5]

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        print(f"head {head}")
        curr = head
        prev = dummy

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.next.val == curr.val:
                    #We have a duplicate 
                    curr = curr.next
                    # curr.next = curr.next.next

                prev.next =curr.next
            else:
                prev = curr
            
            curr = curr.next
        return dummy.next
    
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]