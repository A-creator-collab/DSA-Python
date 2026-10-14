"""
Problem: Search Insert Position (LeetCode 35)
Difficulty: Easy

Return index of target if found, else the index where it would be inserted
to keep the array sorted.

Time: O(log n)
Space: O(1)
"""

def search_insert(nums, target):
    lo, hi = 0, len(nums)

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid

    return lo


if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([], 5) == 0
    print("All tests passed.")
