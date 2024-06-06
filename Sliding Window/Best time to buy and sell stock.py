class Solution:
    def maxProfit(self, prices):
        min_val = float('inf')  # positive only
        max_profit = 0

        for price in prices:
            # Check if the current price is less than the minimum value
            if price < min_val:
                min_val = price  # Update the minimum value

            # Check if the difference between the current price and minimum value is greater than the maximum profit
            elif price - min_val > max_profit:
                max_profit = price - min_val  # Update the maximum profit

        return max_profit  # Return the final maximum profit
