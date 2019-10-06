#include "bits/stdc++.h"
 
using namespace std;

bool good(const string& s) {
  return atoi(s.substr(max(0, (int)s.size() - 3)).c_str()) % 8 == 0;
}
 
int main() {
  string s;
  cin >> s;
  int n = s.size();
  int last = -1;
  for (int i = n - 1; i >= 0; --i) {
    if (s[i] == '?') {
      last = i;
      break;
    }
  }
  if (last == -1) {
    cout << (good(s) ? s : "-1") << endl;
    return 0;
  }
  for (int i = 0; i < last; ++i) {
    if (s[i] == '?') {
      s[i] = (i ? '0': '1');
    }
  }

  for (char c = '0'; c <= '9'; ++c) {
    if (last == 0 && c == '0') continue;
    s[last] = c;
    if (good(s)) {
      cout << s << endl;
      return 0;
    }
  }

  cout << -1 << endl;
}
 