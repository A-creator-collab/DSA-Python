"""
Problem: Linear Search
Time: O(n)
Space: O(1)
"""

def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1


if __name__ == "__main__":
    print(linear_search([4, 2, 7, 1, 9], 7))  # 2
    print(linear_search([4, 2, 7, 1, 9], 5))  # -1
