#Problem Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/


def maxScore(cardPoints, k):
    i=k-1
    j=0
    h=sum(cardPoints[:k])
    ans=h
    l=cardPoints[::-1]
    while j<k:
        h+=l[j]
        h-=cardPoints[i]
        ans=max(h,ans)
        i-=1
        j+=1
    return ans