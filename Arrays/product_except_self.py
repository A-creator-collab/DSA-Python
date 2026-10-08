"""
Problem: Product of Array Except Self (LeetCode 238)
Difficulty: Medium

Return an array where output[i] is the product of all elements except nums[i].
Must run in O(n) and without using division.

Time: O(n)
Space: O(1) extra (output array not counted)

Approach: two passes. First pass stores prefix products.
Second pass multiplies in the suffix products on the fly.
"""

def product_except_self(nums):
    n = len(nums)
    out = [1] * n

    # prefix products
    prefix = 1
    for i in range(n):
        out[i] = prefix
        prefix *= nums[i]

    # suffix products multiplied in
    suffix = 1
    for i in range(n - 1, -1, -1):
        out[i] *= suffix
        suffix *= nums[i]

    return out


if __name__ == "__main__":
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([2, 3]) == [3, 2]
    print("All tests passed.")
