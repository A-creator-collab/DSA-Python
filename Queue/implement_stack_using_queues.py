"""
Problem: Implement Stack using Queues (LeetCode 225)
Time: push O(n), pop O(1)
Space: O(n)

Uses one queue. On push, rotate the queue so the new element
sits at the front. Then pop and top are O(1).
"""

from collections import deque


class MyStack:
    def __init__(self):
        self._q = deque()

    def push(self, x: int) -> None:
        self._q.append(x)
        for _ in range(len(self._q) - 1):
            self._q.append(self._q.popleft())

    def pop(self) -> int:
        return self._q.popleft()

    def top(self) -> int:
        return self._q[0]

    def empty(self) -> bool:
        return len(self._q) == 0


if __name__ == "__main__":
    s = MyStack()
    s.push(1)
    s.push(2)
    assert s.top() == 2
    assert s.pop() == 2
    assert s.empty() is False
    assert s.pop() == 1
    assert s.empty() is True
    print("All tests passed.")
