#Problem Link: https://leetcode.com/problems/find-the-duplicate-number/


def findDuplicate(nums):
    dict1={}
    #Making the frequency table.
    for x in nums:
        dict1[x]=dict1.get(x,0)+1
    
    #Chacking is frequency greater than 1 or not if then return number.
    for key in dict1:
        if dict1[key]>1:
            return key

n=int(input())
nums=[int(x) for x in input().split()]
print(findDuplicate(nums))
        