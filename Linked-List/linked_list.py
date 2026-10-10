"""
Singly Linked List implementation.

Operations:
- append(value): add to the end
- prepend(value): add to the front
- delete(value): remove first occurrence
- search(value): return True if found
- to_list(): return Python list of values
- __len__: number of nodes
"""

class Node:
    __slots__ = ("value", "next")

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def prepend(self, value):
        self.head = Node(value, self.head)
        self._size += 1

    def delete(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            self._size -= 1
            return True

        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        if current.next:
            current.next = current.next.next
            self._size -= 1
            return True
        return False

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_list(self):
        out = []
        current = self.head
        while current:
            out.append(current.value)
            current = current.next
        return out

    def __len__(self):
        return self._size


if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    assert ll.to_list() == [0, 1, 2, 3]
    assert len(ll) == 4
    assert ll.search(2) is True
    assert ll.search(99) is False
    assert ll.delete(2) is True
    assert ll.to_list() == [0, 1, 3]
    assert ll.delete(99) is False
    print("All tests passed.")
