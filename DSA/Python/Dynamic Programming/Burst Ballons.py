#Problem Link: https://leetcode.com/problems/burst-balloons/

#Application of Matrix chain Multiplication 

import sys
def helper(i,j,p,dp):
    if i==j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    maxopr=-sys.maxsize
    for k in range(i,j):
        steps=(p[i-1]*p[k]*p[j]) + helper(i,k,p,dp) + helper(k+1,j,p,dp)
        
        maxopr=max(maxopr,steps)

    dp[i][j]=maxopr
    return maxopr

def maxCoins(nums):
    N=len(nums)
    nums=[1]+nums+[1]
    dp=[[-1 for i in range(N+2)] for j in range(N+2)]
    return helper(1,N+1,nums,dp)