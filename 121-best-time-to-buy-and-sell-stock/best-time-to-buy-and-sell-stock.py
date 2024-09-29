class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        minimum = prices[0]
        maximum = 0

        for price in prices[1:]:
            maximum = max(maximum, price - minimum)
            minimum = min(price, minimum)

        return maximum 