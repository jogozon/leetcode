class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0] # find the minimum
        for price in prices:
            if price < lowest:
                lowest = price # update min if there is a lower numeber
            res = max(res, price - lowest) # update the current profit calculated after the new min
        return res
