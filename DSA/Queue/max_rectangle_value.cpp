//Given an array where each element represent the height of the 
// histogram's bar and the width of each bar is 1.Find the area of 
// largest rectangular in the histogram.


//Example 1:
// array=[2,1,5,6,2,3]
//ans=10



#include<bits/stdc++.h>          //header file

using namespace std;
int get_max_area(vector<int> a){               //function to calculate it
    int n=a.size(),ans=0,i=0;               
    a.push_back(0);
    stack <int> st;
    while(i<=n){
        while(!st.empty() and a[st.top()] > a[i]){
              int t=st.top();
              int h=a[t];
              st.pop();
              if(st.empty()){
                  ans=max(ans,h*i);
              }
              else
              {
                  int len=i-st.top()-1;
                  ans= max(ans,h*len);
              }
        }
        st.push(i);
        i++;
    }
    return ans;
}

int main(){
    vector<int> a={2,1,5,6,2,5};
    cout<<get_max_area(a)<<endl;
    return 0;
}
//{2,1,2,,2,4,6,3,2,7,9,4}