#Problem Link: https://leetcode.com/problems/two-sum/

#Finding Pair Sum == Traget u
# Used Two pointer Alogrithm

def twoSum(nums, target):
    a=nums.copy()
    nums.sort()
    i=0
    n=len(nums)
    j=n-1
    ans=[]
    while i<j:
        if nums[i]+nums[j]==target:
            ans=[nums[i],nums[j]]
            break
        elif nums[i]+nums[j]<target:
            i+=1
        elif nums[i]+nums[j]>target:
            j-=1
    index1=a.index(ans[0])
    a[index1]=None
    index2=a.index(ans[1])
    a[index2]=None
    return [index1,index2]
    