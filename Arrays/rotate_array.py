"""
Problem: Rotate Array (LeetCode 189)
Difficulty: Medium

Rotate the array to the right by k steps, in-place.

Time: O(n)
Space: O(1)

Approach: reverse the whole array, then reverse the first k,
then reverse the remaining n-k. Three reversals give a rotation.
"""

def rotate(nums, k):
    n = len(nums)
    if n == 0:
        return
    k = k % n

    def reverse(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1

    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    rotate(a, 3)
    print(a)  # [5, 6, 7, 1, 2, 3, 4]
    assert a == [5, 6, 7, 1, 2, 3, 4]

    b = [-1, -100, 3, 99]
    rotate(b, 2)
    print(b)  # [3, 99, -1, -100]
    assert b == [3, 99, -1, -100]

    c = [1, 2]
    rotate(c, 0)
    assert c == [1, 2]

    print("All tests passed.")
