"""
Problem: Best Time to Buy and Sell Stock
Time: O(n)
Space: O(1)
"""

def max_profit(prices):
    min_price = float("inf")
    best_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            best_profit = max(best_profit, price - min_price)

    return best_profit


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
