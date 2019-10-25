#include <cstdio>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int n, k, l;
    scanf("%d%d%d", &n, &k, &l);
    vector< int > mask(n);

    char mask_s[9];
    for (int i = 0; i < n; ++i) {
        scanf("%s", mask_s);

        int m = 0;
        for (int j = 0; j < k; ++j) {
            m = (m << 1) | (mask_s[j] - '0');

        }
        mask[i] = m;
    }

    vector< vector< int > > g(n);

    for (int i = 0; i < n - 1; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        g[u - 1].push_back(v - 1);
        g[v - 1].push_back(u - 1);
    }

    queue< int > Q;
    vector< int > vis(n, -1);
    vector< long long > at_most_mask(1 << k, 0);
    for (int m = 0; m < (1 << k); ++m) {

        for (int s = 0; s < n; ++s) {
            // s is not in any component yet and
            // mask[m] does not have an extra 1 compared to m
            if (vis[s] != m && (mask[s] | m) == m) {
                int component_size = 1;
                vis[s] = m;

                Q.push(s);

                while (!Q.empty()) {
                    int u = Q.front(); Q.pop();

                    for (int v : g[u]) {
                        if (vis[v] != m && (mask[v] | m) == m) {
                            component_size++;
                            vis[v] = m;
                            Q.push(v);
                        }
                    }
                }

                at_most_mask[m] += ((long long)component_size) * (((long long)component_size) + 1) / 2;
            }
        }
    }


    long long answer = 0;
    for (int m = 0; m < (1 << k); ++m) {
        int mbits = 0;
        for (int m1 = m; m1 > 0; m1 >>=1 ) {
            mbits += m1 & 1;
        }
        if (mbits < l) {
            continue;
        }
        for (int subm = 0; subm <= m; ++subm) {
            if ((subm | m) == m) {
                int submbits = 0;
                for (int m1 = subm; m1 > 0; m1 >>= 1) {
                    submbits += m1 & 1;
                }
                if ((mbits - submbits) % 2 == 0) {
                    answer += at_most_mask[subm];
                } else {
                    answer -= at_most_mask[subm];
                }
            }
        }
    }

    printf("%lld\n", answer);
    return 0;
}

