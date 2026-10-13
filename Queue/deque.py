"""
Double-ended queue (deque) implementation.

Supports O(1) operations at both ends:
- push_front(value)
- push_back(value)
- pop_front()
- pop_back()
- peek_front()
- peek_back()
- is_empty()
- size()
"""

from collections import deque


class Deque:
    def __init__(self):
        self._items = deque()

    def push_front(self, value):
        self._items.appendleft(value)

    def push_back(self, value):
        self._items.append(value)

    def pop_front(self):
        if self.is_empty():
            return None
        return self._items.popleft()

    def pop_back(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek_front(self):
        if self.is_empty():
            return None
        return self._items[0]

    def peek_back(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Deque({list(self._items)})"


if __name__ == "__main__":
    d = Deque()
    d.push_back(2)
    d.push_back(3)
    d.push_front(1)
    d.push_front(0)
    assert list(d._items) == [0, 1, 2, 3]
    assert d.peek_front() == 0
    assert d.peek_back() == 3
    assert d.pop_front() == 0
    assert d.pop_back() == 3
    assert d.size() == 2
    print("All tests passed.")
