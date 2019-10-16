#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define NUMMAX 1000000

vector< int > assign(vector< int > & counts, int m) {
    vector < int > assignment;
    for (int i = 1; i <= NUMMAX; ++i) {
        int c = counts[i];
        for (int j = 0; j < c && j < m; ++j) {
            assignment.push_back(i);
        }
    }
    return assignment;
}

int main() {
    int n, h;
    scanf("%d%d", &n, &h);

    vector< int > counts(NUMMAX + 1);
    for (int i = 0; i < n; ++i) {
        int x;
        scanf("%d", &x);
        counts[x] ++;
    }

    int l = 1, r = n / h;
    while (l + 1 < r) {
        int m = (l + r) >> 1;
        vector< int > a = assign(counts, m);
        if (a.size() >= h * m) {
            l = m;
        } else {
            r = m;
        }
    }
    while (r >= l) {
        vector< int > a = assign(counts, r);
        if (a.size() >= h * r) {
            printf("%d\n", r);
            return 0;
            // for (int i = 0; i < r; ++i) {
            //     for (int j = 0; j < h; ++j) {
            //         printf("%d%c", a[j * r + i], ((j < h - 1) ? ' ' : '\n'));
            //     }
            // }
            // return 0;
        }
        r--;
    }
    printf("0\n");
    // printf("impossible\n");
    return 0;
}

