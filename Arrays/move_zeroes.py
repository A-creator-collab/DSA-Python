"""
Problem: Move Zeroes (LeetCode 283)
Difficulty: Easy

Move all zeroes to the end while keeping the order of non-zero elements.
Must be done in-place.

Time: O(n)
Space: O(1)
"""

def move_zeroes(nums):
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    move_zeroes(a)
    print(a)  # [1, 3, 12, 0, 0]
    assert a == [1, 3, 12, 0, 0]

    b = [0]
    move_zeroes(b)
    assert b == [0]

    print("All tests passed.")
