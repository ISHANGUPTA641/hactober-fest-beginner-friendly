#Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices):
    maxProfit=0
    n=len(prices)
    max_=[0]*n
    maxEle=None
    for i in range(n-1,-1,-1):
        if maxEle==None:
            maxEle=prices[i]
            max_[i]=maxEle
        else:
            if maxEle<prices[i]:
                maxEle=prices[i]
                max_[i]=maxEle
            else:
                max_[i]=maxEle
    for i in range(n):
        diff=max_[i]-prices[i]
        if diff>maxProfit:
            maxProfit=diff
    return maxProfit
            