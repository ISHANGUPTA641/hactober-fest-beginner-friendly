#Problem Link: https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

#Partition dp
#Step 1: Start with entire block/array
#Step 2: Try all partition
        #Run a loop to try all
#Step 3: Return the best possible 2 partition.

#Time Complexity: O(n^3)
#Space Complexity: O(n^2) 
import sys
def helper(i,j,p,dp):
    if i==j:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    minopr=sys.maxsize
    for k in range(i,j):
        steps=(p[i-1]*p[k]*p[j]) + helper(i,k,p,dp) + helper(k+1,j,p,dp)
        
        minopr=min(minopr,steps)

    dp[i][j]=minopr
    return minopr

def matrixMultiplication(N, arr):
    # code here
    dp=[[-1 for i in range(N)] for j in range(N)]
    return helper(1,N-1,arr,dp)

