#include <bits/stdc++.h>
using namespace std;

void helper(vector<vector<int>> &res, vector<int> &vec, int begin,vector<int> &nums) {
    if(vec.size()==2) {
        res.push_back(vec);
        return;
    }
    for (int i = begin; i<nums.size(); i++) {
		vec.push_back(nums[i]);
		helper(res, vec, i+1, nums);
		vec.pop_back();
	}
}
    
vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> res;
    vector<int> arr;
    helper(res,arr,0,nums);
    return res;
}

bool compare(vector<int> a, vector<int>b) {
    return a.size() < b.size();
}

int main() {
    vector<int> arr({1,2,3,4,4,5});
    vector<vector<int>> x = subsets(arr);
    sort(x.begin(),x.end(),compare);
    for(vector<int> a: x) 
    {
        cout<<"[";
        for(int i=0;i<a.size();i++) {
            cout<<a[i];
            if(i!=a.size()-1) cout<<",";
        }
        cout<<"] ";
    }
	return 0;
}




// int lis(vector<int>& nums) {
//         int n = nums.size();
//         vector<int> dp(n, 1);
//         for(int i = 0; i < n; i++) 
//             for(int j = 0; j < i; j++) 
//                 if(nums[i] > nums[j] && ((nums[i] & nums[j])*2)<(nums[i] | nums[j])) 
// 				    dp[i] = max(dp[i], dp[j] + 1);
//         return *max_element(dp.begin(),dp.end());
// }
