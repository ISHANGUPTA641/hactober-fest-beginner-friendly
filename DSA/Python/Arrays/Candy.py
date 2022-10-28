#Problem Link: https://leetcode.com/problems/candy/


def candy(ratings):
    n=len(ratings)
    candies=[1]*n
    for i in range(n):
        if i<n-1:
            if ratings[i]>ratings[i+1]:
                candies[i]=candies[i+1]+1
        if i>0:
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
    for i in range(n-1,-1,-1):
        if i>0:
            if ratings[i]>ratings[i-1]:
                if candies[i]<=candies[i-1]:
                    candies[i]=candies[i-1]+1
        if i<n-1:
            if ratings[i]>ratings[i+1]:
                if candies[i]<=candies[i+1]:
                    candies[i]=candies[i+1]+1
    tot=sum(candies)
    return tot


ratings=[int(x) for x in input().split()]
ans=candy(ratings)
print(ans)
