// Given a sorted array A[] of size N, delete all the duplicated elements from A[]. Modify the array such that if there are X distinct elements in it then the first X positions of the array should be filled with them in increasing order and return the number of distinct elements in the array.

#include <bits/stdc++.h>
using namespace std;

int remove_duplicate(int a[],int n){
         int i=0;int j=1;
         while(j<n){
      
         if(a[i]==a[j])
         j++;
         else
         {
         i++;
         a[i]=a[j];
         }
         }
         return i+1;
}

int mai(){
    int n;cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }

    cout<<remove_duplicate(a[n],n)<<endl;
}

