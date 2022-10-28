#Problem Link: https://leetcode.com/problems/subarray-sum-equals-k/

#HashTable #PrefixSum

def subarraySum(nums, k):
    n=len(nums)
    dict1={0:1}
    sum_=0
    count=0
    for i in range(n):
        sum_+=nums[i]
        if dict1.get(sum_-k,0)!=0:
            count+=dict1[sum_-k]
        dict1[sum_]=dict1.get(sum_,0)+1
        
    
    return count