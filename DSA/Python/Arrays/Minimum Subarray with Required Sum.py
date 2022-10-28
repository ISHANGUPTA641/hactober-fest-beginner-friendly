#Problem Link: https://www.codingninjas.com/codestudio/problems/minimum-subarray-with-required-sum_696460?leftPanelTab=0

import sys
def minSubarray(arr, n, x):
	#Write your code here.
    hashmap=[0]
    sum_=0
    for i in range(1,n+1):
        sum_+=arr[i-1]
        hashmap.append(sum_)
    
    i=0
    j=n
    min_=sys.maxsize
    start=None
    end=None
    while i>=0 and j<=n and i<=j:
        if i==j:
            i+=1
            j=n
        else:
            if hashmap[j]-hashmap[i]>x:
                currlen=j-i
                if min_>currlen:
                    min_=currlen
                    start=i
                    end=j
                j-=1

            elif hashmap[j]-hashmap[i]<=x:
                j+=1
                i+=1
    ans=[]
    if start==None and end==None:
        return ans
    for h in range(start+1, end+1):
        ans.append(arr[h-1])
    return ans
        