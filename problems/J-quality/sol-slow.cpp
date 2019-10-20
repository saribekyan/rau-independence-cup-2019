#include <iostream>
#include <string>
#include <vector>
using namespace std;

const long long MOD = 1000000007;

#define LAST 'z'

vector< long long > solve(int n, string x, int k) {
    int m = x.size();
    vector< vector< vector < long long > > > d =
        vector< vector< vector< long long > > >(n + 1,
                vector< vector< long long> >(m + 1,
                    vector< long long >(k + 1, 0)));

    vector< vector < int > > next(m,
            vector< int >(26));

    for (int p = 0; p < m; ++p) {
        for (char c = 'a'; c <= LAST; c++) {
            for (int j = p; j >= 0; j--) {
                if (x.substr(p - j + 1, j - 1) + c == x.substr(0, j)) {
                    next[p][c - 'a'] = j;
                    break;
                }
            }
        }
    }

    d[0][0][0] = 1;

    for (int i = 0; i < n; ++i) {
        for (int p = 0; p < m; ++p) {
            for (int j = 0; j <= k; ++j) {
                if (d[i][p][j] != 0) {
                    for (char c = 'a'; c <= LAST; ++c) {
                        int p1 = next[p][c - 'a'];
                        if (c == x[p]) {
                            if (p == m - 1) {
                                if (j < k) {
                                    d[i + 1][p1][j + 1] = (d[i + 1][p1][j + 1] + d[i][p][j]) % MOD;
                                }
                            } else {
                                d[i + 1][p + 1][j] = (d[i + 1][p + 1][j] + d[i][p][j]) % MOD;
                            }
                        } else {
                            d[i + 1][p1][j] = (d[i + 1][p1][j] + d[i][p][j]) % MOD;
                        }
                    }
                }
            }
        }
    }

    vector< long long > res(n + 1, 0);
    for (int i = 0; i <= n; ++i) {
        for (int p = 0; p < m; ++p) {
            for (int j = 0; j <= k; ++j) {
                res[i] += d[i][p][j];
            }
        }
        res[i] %= MOD;
    }
    return res;
}

int main() {
    int n;
    string xa, xv;
    int ka, kv;
    cin >> n;
    cin >> xa >> ka;
    cin >> xv >> kv;

    vector< long long > da = solve(n, xa, ka);
    vector< long long > dv = solve(n, xv, kv);

    long long answer = 0;
    for (int i = 0; i <= n; ++i) {
        answer = (answer + da[i] * dv[n - i]) % MOD;
    }
    cout << answer << endl;

    return 0;
}

