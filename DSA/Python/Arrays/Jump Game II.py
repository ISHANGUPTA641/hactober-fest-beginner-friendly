# Problem Link: https://leetcode.com/problems/jump-game-ii/submissions/

#Using Valley Top Approach
#Time Complexity: O(n)

def jump(nums):
    n=len(nums)
    if n==1:
        return 0
    rang=nums[0]
    steps=nums[0]
    jumps=1
    for i in range(1,n):
        if i==n-1:
            return jumps
        rang=max(rang,i+nums[i])
        steps-=1
        if steps==0:
            jumps+=1
            steps=rang-i
    
#Using BFS
#Time Complexity: O(n)
#Explaination: https://www.youtube.com/watch?v=dJ7sWiOoK7g
    
def jumpII(nums):
    res=0
    l=r=0
    
    while r<len(nums) - 1:
        farthest = 0
        for i in range(l,r+1):
            farthest=max(farthest, i+nums[i])
        l=r+1
        r=farthest
        res+=1
    return res