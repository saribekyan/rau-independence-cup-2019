#include "bits/stdc++.h"
 
using namespace std;
 
int main() {
  int n;
  cin >> n;
  int left = 1, right = n, ans = 0, i = 0;
  while (left < right) {
    if (i % 2 == 1) {
      ans += right - left;
      left++;
    } else {
      ans += right - left;
      right--;
    }
    ++i;
  }
  cout << ans << endl;
}
