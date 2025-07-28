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