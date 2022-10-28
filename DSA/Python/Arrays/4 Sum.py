#Problem Link: https://leetcode.com/problems/4sum/

#Time Complexity: O(n^3)

def fourSum(nums, target):
    ans=[]
    nums.sort()
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            rem=target-(nums[i]+nums[j])
            left=j+1
            right=n-1
            while left<right:
                if nums[left]+nums[right]==rem:
                    l=[nums[i],nums[j],nums[left],nums[right]]
                    if l not in ans:
                        ans.append(l)
                    left+=1
                    right-=1
                elif nums[left]+nums[right]<rem:
                    left+=1
                else:
                    right-=1
    return ans