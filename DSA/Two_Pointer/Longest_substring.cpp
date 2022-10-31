// find the length of the longest substring without repeating character using two pointer

//Example :1
//s="pwwwekw"
//ans=3;



#include<bits/stdc++.h>   //Header file
using namespace std;

int main(){
    string s;cin>>s;      // input the string
    vector<int> dict(256,-1);
    int maxlen=0,start=-1;
    for(int i=0;i<s.size();i++){
        if(dict[s[i]]> start)
          start=dict[s[i]];
        dict[s[i]]=i;
        maxlen = max(maxlen,i-start);
    }
    cout<<maxlen;
    return 0;
}