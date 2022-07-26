#include<bits/stdc++.h>
using namespace std;

int main() {
    string str = "abcxcbc";
    int n = str.size();
    int dp[n][n];
    memset(dp,0,sizeof(dp));

    for(int i=n-1;i>=0;i--) {
        for(int j=i;j<n;j++) {
            if(str[i]==str[j] && (j-i<=2 || dp[i+1][j-1]))
                dp[i][j] = 1;
        }
    }


    for(int i=0;i<n;i++) {
        for(int j=0;j<n;j++) {
            cout<<dp[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}