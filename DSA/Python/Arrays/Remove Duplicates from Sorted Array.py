#Problem Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Using two pointer Alogirthm
def removeDuplicates(nums):
    i=0
    j=0
    n=len(nums)
    while i<n:
        if j<=(n-1):
            if j<(n-1):
                while j<n:
                    if nums[i]!=nums[j]:
                        break
                    else:
        
                        j+=1
            
                try:
                    nums[i+1]=nums[j]
                except:
                    pass
    
                i+=1
            else:
                try:
                    nums[i+1]=nums[j]
                except:
                    pass
                
                j+=1
                i+=1
        else:
            nums[i]=" "
            i+=1
    k=0
    for x in nums:
        if x!=" ":
            k+=1
    return k

nums=[int(x) for x in input().split()]
ans=removeDuplicates(nums)
print(ans)
print(nums)