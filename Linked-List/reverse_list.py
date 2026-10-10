"""
Problem: Reverse Linked List (LeetCode 206)
Time: O(n)
Space: O(1)

Reverses a singly linked list in place.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def build_list(values):
    dummy = Node(0)
    tail = dummy
    for v in values:
        tail.next = Node(v)
        tail = tail.next
    return dummy.next


def list_to_python(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    reversed_head = reverse_list(head)
    assert list_to_python(reversed_head) == [5, 4, 3, 2, 1]

    head2 = build_list([])
    assert list_to_python(reverse_list(head2)) == []

    head3 = build_list([7])
    assert list_to_python(reverse_list(head3)) == [7]

    print("All tests passed.")
