class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_price = 0
        while i<j and j < len(prices):
            curr_price = prices[j]-prices[i]
            if prices[i] > prices[j]:
                i = j
                j = j + 1
            else:
                max_price = max(max_price,curr_price)
                j = j+1
        return max_price