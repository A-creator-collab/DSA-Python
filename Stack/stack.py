"""
Stack implementation using a Python list.

Operations:
- push(value)
- pop() -> value or None if empty
- peek() -> top value or None
- is_empty()
- size()
"""

class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"


if __name__ == "__main__":
    s = Stack()
    assert s.is_empty() is True
    assert s.pop() is None

    s.push(1)
    s.push(2)
    s.push(3)
    assert s.size() == 3
    assert s.peek() == 3
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.size() == 1
    assert s.peek() == 1
    print("All tests passed.")
