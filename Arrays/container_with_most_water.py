"""
Problem: Container With Most Water (LeetCode 11)
Difficulty: Medium

Given heights, find two lines that together with the x-axis form a
container holding the most water.

Time: O(n)
Space: O(1)

Approach: two pointers from both ends. Move the pointer at the shorter
line inward, because the shorter line is what limits the area.
"""

def max_area(height):
    lo, hi = 0, len(height) - 1
    best = 0

    while lo < hi:
        width = hi - lo
        h = min(height[lo], height[hi])
        best = max(best, width * h)

        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1

    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    print("All tests passed.")
