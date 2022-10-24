// Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

// Example 1:

// Input: nums = [2,1,2]
// Output: 5
// Example 2:

// Input: nums = [1,2,1]
// Output: 0
 

// Constraints:

// 3 <= nums.length <= 104
// 1 <= nums[i] <= 106

#include <iostream>
#include <vector>
#include <algorithm>
 
using namespace std;

int largestPerimeter(vector<int>& nums) {
        sort(nums.begin(),nums.end(),greater<int>());
        for(int i=0;i<nums.size()-2;i++){
            if(nums[i]<nums[i+1]+nums[i+2]){
                return nums[i]+nums[i+1]+nums[i+2];
                break;
            }
        }
        return 0;
    }
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int t; cin>>t;
    while(t--){
        vector <int> v;
        for(auto x: v){
            cin>>x;
        }
        largestPerimeter(v);
    }
    return 0;
}
