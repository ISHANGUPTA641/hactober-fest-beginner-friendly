#Problem Link: https://leetcode.com/problems/move-zeroes/

def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    i=0
    n=len(nums)
    while i<(n):
        if nums[i]==0:
            j=i
            while j<n and nums[j]==0:
                j+=1
            if j<n:
                nums[i],nums[j]=nums[j],nums[i]
        i+=1
    