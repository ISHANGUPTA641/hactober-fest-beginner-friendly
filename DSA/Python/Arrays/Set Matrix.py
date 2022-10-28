#Problem Link: https://leetcode.com/problems/set-matrix-zeroes/submissions/

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    m=len(matrix)
    n=len(matrix[0])
    
    horizontal=[0]*(n)
    vertical=[0]*m
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                horizontal[j]=1
                vertical[i]=1
    
    for i in range(m):
        for j in range(n):
            if horizontal[j]==1 or vertical[i]==1:
                matrix[i][j]=0
