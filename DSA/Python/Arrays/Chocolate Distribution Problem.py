#Problem Link: https://practice.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1/
import sys

def findMinDiff(A,N,M):

    # code here
    A.sort()
    i=0
    j=i+M
    min_=sys.maxsize
    while j<=N:
        diff=A[j-1]-A[i]
        if diff<min_:
            min_=diff
        i+=1
        j+=1
    return min_

N, M=map(int, input().split())
arr=[int(x) for x in input().split()]
ans=findMinDiff(arr,N,M)
print(ans)