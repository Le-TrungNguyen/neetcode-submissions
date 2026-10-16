class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mua = prices[0]
        maxP = 0
        for ban in prices[1:]:
            if ban < mua:
                mua = ban
            else:
                P = ban - mua
                maxP = max(maxP, P)
        
        return maxP