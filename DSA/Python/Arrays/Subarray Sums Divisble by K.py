#Problem Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/submissions/

#Using the concept of prefix sum and mod and hashamap.
def subarraysDivByK( nums, k):
    n=len(nums)
    dict1={0:1}
    sum_=0
    for i in range(n):
        sum_+=nums[i]
        val=sum_%k
        dict1[val]=dict1.get(val,0)+1
        
        
    count=0
    for key in dict1:
        count+=(dict1[key]*(dict1[key]-1))//2
    return count

arr=[int(x) for x in input().split()]
k=int(input())
ans=subarraysDivByK(arr,k)
print(ans)