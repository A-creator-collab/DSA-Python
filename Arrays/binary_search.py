"""
Problem: Binary Search
Time: O(log n)
Space: O(1)
Note: Array must be sorted.
"""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    print(binary_search([1, 3, 5, 7, 9, 11], 7))  # 3
    print(binary_search([1, 3, 5, 7, 9, 11], 4))  # -1
