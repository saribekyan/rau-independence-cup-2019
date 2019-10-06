#include "bits/stdc++.h"
 
using namespace std;
 
int main() {
  int n;
  cin >> n;
  vector <long long> v(n), left(n), left_num(n), right_num(n), right(n);
  for (int i = 0; i < n; ++i)
    cin >> v[i];
  left_num[0] = v[0];
  for (int i = 1; i < n; ++i) {
    left_num[i] = max(left_num[i - 1] + 1, v[i]);
    left[i] = left[i - 1] + left_num[i] - v[i];
  }
  right_num[n - 1] = v[n - 1];
  for (int i = n - 2; i >= 0; --i) {
    right_num[i] = max(right_num[i + 1] + 1, v[i]);
    right[i] = right[i + 1] + right_num[i] - v[i];
  }
  long long answer = -1;
  for (int i = 0; i < n; ++i) {
    long long tmp = left[i] + right[i] - (min(left_num[i], right_num[i]) - v[i]);
    if (answer == -1 || answer > tmp) {
      answer = tmp;
    };
  }
  cout << answer << endl;
}
