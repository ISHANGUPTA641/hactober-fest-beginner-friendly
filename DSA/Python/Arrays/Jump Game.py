#Problem Link1: https://leetcode.com/problems/jump-game/submissions/
#Problem Link2: https://practice.geeksforgeeks.org/problems/jump-game/1
#Explaination: https://www.youtube.com/watch?v=muDPTDrpS28&t=28s

#Time Comlexity: O(n) Using Valley Top Approach
#Time Complexity: O(n^2) Using Dynamic Programming

def helper(arr,n):
    if n==1:
        return 0
    if arr[0]==0:
        return -1
    
    rang=arr[0]
    for i in range(1,n):
        if i==n-1:
            return 0
        rang=max(rang,i+arr[i])
        if rang<=i:
            return -1
    return -1

def canJump(nums):
    n=len(nums)
    ans=helper(nums,n)
    if ans==-1:
        return False
    else:
        return True
