"""
Queue implementation (FIFO) using collections.deque.

Operations:
- enqueue(value): add to the back
- dequeue(): remove from the front
- front(): peek at the front
- is_empty()
- size()

Using deque gives O(1) for both ends. Using a plain list for dequeue
would be O(n) because pop(0) shifts every element.
"""

from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Queue({list(self._items)})"


if __name__ == "__main__":
    q = Queue()
    assert q.is_empty() is True
    assert q.dequeue() is None

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    assert q.size() == 3
    assert q.front() == 1
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.size() == 1
    assert q.front() == 3
    print("All tests passed.")
