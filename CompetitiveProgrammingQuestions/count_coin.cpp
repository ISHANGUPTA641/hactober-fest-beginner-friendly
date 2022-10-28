//Given an array which represent different coin denomination and total amount 'T'
//Find the minimum no of coins to make change for 'sum'


//Example 1:
// coins =4     sum=13
// array=[1,3,5,15]
//Result=3  [5,5,3]


//  Example 2
// coins=5   sum=19
//array=[1,2 ,7 ,9,13]
//result=4


// Constraints:

// 3 <= coin <= 105
// 1 <= sum <= 106


#include<bits/stdc++.h>              //header file
using namespace std;
#define ll long long                 // defing long long
int main(){
    int coin,sum;                    // taking input
    cin>>coin>>sum;
    vector<ll> denom(coin);           //coin
    for(int i=0;i<coin;i++){
        cin>>denom[i];
    }
    vector<ll> dp(sum+1);             //sum+1
    for(int i=1;i<=sum;i++){
        dp[i]=sum+1;
    }
    dp[0]=0;
    for(int i=0;i<=sum;i++){
        for(int j=0;j<coin;j++){       //with the dp approach calculating the value
            if(denom[j]<= i){
                dp[i]=min(dp[i],1+dp[i-denom[j]]);
            }
        }
    }
    if(dp[sum]==sum+1) cout<<"-1"<<endl;
    else
      cout<<dp[sum]<<endl;
}