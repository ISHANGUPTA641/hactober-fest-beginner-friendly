#Problem Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/

def findDuplicates(nums):
    dict1={}
    for x in nums:
        dict1[x]=dict1.get(x,0)+1
    ans=[]
    for key in dict1:
        if dict1[key]>1:
            ans.append(key)
    return ans

nums=[int(x) for x in input().split()]
ans=findDuplicates(nums)
print(ans)
        