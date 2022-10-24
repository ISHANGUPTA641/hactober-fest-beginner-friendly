#Problem Link: https://leetcode.com/problems/3sum/submissions/


#Time Comlexity: O(n^2)
#Using Two pointer Alogorithm

def threeSum(nums):
    ans=[]
    nums.sort()
    n=len(nums)
    for i in range(n):
        rem=(0-nums[i])
        left=i+1
        right=n-1
        while left<right:
            if nums[left]+nums[right]==rem:
                l=[nums[i],nums[left],nums[right]]
                if l not in ans:
                    ans.append(l)
                left+=1
                right-=1
            elif nums[left]+nums[right]>rem:
                right-=1
            elif nums[left]+nums[right]<rem:
                left+=1
    return ans

t=int(input())
j=1
while t>0:
    nums=[int(x) for x in input().split()]
    ans=threeSum(nums)
    print("Case #{}: {}".format(j,ans))
    j+=1
    t=t-1