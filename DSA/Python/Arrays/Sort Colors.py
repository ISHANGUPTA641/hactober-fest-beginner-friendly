# Problem Link: https://leetcode.com/problems/sort-colors/

def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    two=0
    zero=0
    one=0
    for x in nums:
        if x==0:
            zero+=1
        elif x==1:
            one+=1
        elif x==2:
            two+=1
    for i in range(len(nums)):
        if zero!=0:
            nums[i]=0
            zero-=1
        elif one!=0:
            nums[i]=1
            one-=1
        elif two!=0:
            nums[i]=2
            two-=1
        