#Problem Link: https://leetcode.com/problems/merge-sorted-array/

def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr=nums1[:m]+nums2
        arr.sort()
        for i in range(n+m):
            nums1[i]=arr[i]

#Inplace

def merge(A,B):
    
    m=len(A)
    n=len(B)
    i=0
    j=0
    k=0
    
    
    while i<m:
        if A[i]>B[j]:
            A[i],B[j]=B[j],A[i]
        i+=1
    else:
        while j<n:
            A.append(B[j])
            j+=1
        A.sort()
            