//Given an array of element and you have to return a maximum element present in an window of k elements
// in o(n) time complexity




//Example 1:
// n=6  k=2
//a=[3,4,9,1,-4,10]
//output=[4,9,9,1,10]



#include<bits/stdc++.h>         //header file
using namespace std;

int main(){                          //time=o(n);
     int n,k;cin>>n>>k;
    vector<int> a(n);
    for(auto &i: a){               // inpur of array
        cin>>i;
    }
    deque<int> q;
    vector<int>  ans;
    for(int i=0;i<k;i++){                  
        while(!q.empty() and a[q.back()]<a[i]){          
            q.pop_back();                    
        }                                   
        q.push_back(i);                  
    }                                     
    ans.push_back(a[q.front()]);
    for(int i=k;i<n;i++){
        if(q.front()==i-k){           
            q.pop_front();
        }
        while(!q.empty() and a[q.back()]< a[i]){
             q.pop_back();
        }
        q.push_back(i);
        ans.push_back(a[q.front()]);

    }
    for(auto i: ans){
        cout<<i<<" ";
    }
    return 0;
}