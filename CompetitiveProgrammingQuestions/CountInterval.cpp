// Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

// Example 1:

// Input: low = 3, high = 7
// Output: 3
// Explanation: The odd numbers between 3 and 7 are [3,5,7].

// Example 2:

// Input: low = 8, high = 10
// Output: 1
// Explanation: The odd numbers between 8 and 10 are [9].


#include <iostream>
 
using namespace std;

int countOdds(int low, int high) {
    int count =0;
    if(high%2!=0 || low%2!=0) count++;
    count +=(high-low)/2;
    return count;
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t; cin>>t;
    while(t--){
        int low,high; cin>>low>>high;
        cout<<countOdds(low,high)<<endl;
    }
    return 0;
}


