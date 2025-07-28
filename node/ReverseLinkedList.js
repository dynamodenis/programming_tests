function reverseLinkedList(head) {
    let prev = null;
    let current = head;

    while (current !== null) {
        const nextNode = current.next; // Store the next node
        current.next = prev; // Reverse the link
        prev = current; // Move prev to current
        current = nextNode; // Move to the next node
    }

    return prev; // New head of the reversed list
}