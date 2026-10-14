"""
Problem: Find First and Last Position of Element in Sorted Array (LeetCode 34)
Difficulty: Medium

Return [first, last] index of target, or [-1, -1] if not found.

Time: O(log n)
Space: O(1)

Approach: two binary searches — one biased left for first,
one biased right for last. Do not stop at the first match.
"""

def search_range(nums, target):
    def find_first():
        lo, hi = 0, len(nums) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                result = mid
                hi = mid - 1        # keep searching left
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    def find_last():
        lo, hi = 0, len(nums) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                result = mid
                lo = mid + 1        # keep searching right
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return result

    return [find_first(), find_last()]


if __name__ == "__main__":
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([1, 1, 1, 1], 1) == [0, 3]
    print("All tests passed.")
