// The span of stock's price today is defined as the maximum number of consecutive
//days (staring from today and going backwards )for which the price of the stocks 
//was less than or equal to todays price .Find the span of the stocks for all days.


//Example 1:
//array:[100,80,60,70,60,75,85]
//output:[1,1,1,2,1,4,6]




#include<bits/stdc++.h>     //header file
using namespace std;
vector<int>stockspan(vector<int>prices){
    vector<int> ans;
    stack<pair<int,int>> s;
    for(auto price: prices){
        int days=1;
        while(!s.empty() && (s.top().first  <= price)){
            days+=s.top().second;
            s.pop();
        }
        s.push({price,days});              //make pair or curly braces
        ans.push_back(days);
    }
    return ans;
}
int main(){
    vector<int> a={100,80,60,70,60,75,85};
    vector <int> res=stockspan(a);
    for(auto i:res){
        cout<<i<<" ";
    } 
    cout<<endl;
    return 0;
}
