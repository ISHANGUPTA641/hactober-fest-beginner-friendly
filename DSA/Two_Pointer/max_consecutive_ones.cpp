//Given the array of 0's and 1's.we may change up to k values
//from 0 to 1.Therefore return the longest (continuous)subarray
//that contains only one


//Example 1:n=11  k=2
//[1,1,1,0,0,0,1,1,1,1,0] 
//output :6
//explanation: [1,1,1,0,0,1,1,1,1,1,1]



#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;cin>>n;
    int k;cin>>k;
    vector<int> a(n);
    for(auto &i : a){
        cin>>i;
    }
    int zerocnt =0,i=0,ans=0;
    for(int j=0;j<n;j++){
        if(a[j]==0)
         zerocnt++;
        while(zerocnt > k){
            if(a[i]==0){
                zerocnt--;
            }
            i++;
        }
        ans=max(ans,j-i+1);
    }
    cout<<ans<<endl;
    return 0;
}