#Problem Link: https://leetcode.com/problems/majority-element/submissions/

#Using Boyer-Moore Voting Algorithm
#Time Complexity: O(N) 
#Space Complexity: O(1)

def majorityElement(nums):
    n=len(nums)
    major=None
    freq=0
    for i in range(n):
        if major==None:
            major=nums[i]
            freq+=1
        elif major==nums[i]:
            freq+=1
        else:
            freq-=1
            if freq==0:
                major=nums[i]
                freq+=1
    return major
                