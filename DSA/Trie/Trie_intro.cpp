//Trie is a type of  search tree used for storing and searching a specific key from a set. 
//Using Trie, search complexities can be brought to optimal limit (key length).


//Give a set of string and a key.Display all suggestion corresponding to a given key that is used previosly.
//Example 1:
//n=6
//strings:[ans,and,rahul,word,animal,aman]
//key:an
//output:[ans,and,animal] 

#include<bits/stdc++.h>
using namespace std;
#define ll long long
struct vertex {                         
    vector<vertex*> next;
    bool leaf = false;
    vertex(int k){
        next.resize(k,NULL);
    }
};
void add_string(string const& s,vertex* node) {
    for (char ch : s) {
        int c = ch - 'a';
        if (node->next[c]==NULL) {
            node->next[c] = new vertex(26);
        }
        node=node->next[c];
    }
    node->leaf=true;
}
vertex* automation_node(string s,vertex* node){
    for (char ch : s) {
        int c = ch - 'a';
        if (node->next[c]==NULL) {
            return NULL;
        }
        node=node->next[c];
    }
    return node;
}
void words(string s,vertex* prefix,vector<string> &ans,string t){
    if(prefix->leaf==true){
        ans.push_back(s+t);
    }
    for(int i=0;i<=25;i++){
        if(prefix->next[i]!=NULL){
            char ch='a'+i;
            words(s,prefix->next[i],ans,t+ch);
        }
    }
    return ;
}
void solve(){
    vertex* node=new vertex(26);
    ll n;cin>>n;
    for(int i=0;i<n;i++){
        string h;cin>>h;
        add_string(h,node);
    }
    string s;cin>>s;
    vertex* prefix=automation_node(s,node);
    if(s!="" && prefix==NULL){
        cout<<-1<<endl;return ;
    }
    vector<string> ans;
    words(s,prefix,ans,"");
    for(auto i:ans){
        cout<<i<<" ";
    }cout<<endl; 
}
int main(){
    ll t=1;cin>>t;
    for(int q=1;q<=t;q++){
       solve();
    }
    return 0;
}