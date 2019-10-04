#include <iostream>
#include <vector>
#include <cassert>
#include <queue>
using namespace std;

#include "../../testlib/testlib.h"

const int NTESTS = 25;
int test = 1;
const char* template_path = "../../tests/E/%03d";

const int MAXN = 100000;
const int B    = 8;

vector< pair< int, int > > random_tree(int n, int t) {
    vector < int > p(n);
    for (int i = 0; i < n; ++i) {
        if (i > 0) {
            p[i] = rnd.wnext(i, t);
        }
    }

    vector<int> perm(n);
    for (int i = 0; i < n; ++i) {
        perm[i] = i;
    }

    shuffle(perm.begin() + 1, perm.end());
    vector< pair<int, int> > edges;

    for (int i = 1; i < n; i++)
        if (rnd.next(2))
            edges.push_back(make_pair(perm[i], perm[p[i]]));
        else
            edges.push_back(make_pair(perm[p[i]], perm[i]));

    shuffle(edges.begin(), edges.end());

    return edges;
}

vector< pair< int, int > > path(int n) {
    vector< pair< int, int > > edges;
    for (int i = 0; i < n - 1; ++i) {
        edges.push_back(make_pair(i, i + 1));
    }
    return edges;
}

vector< vector< int > > edges_to_graph(vector< pair < int, int > >& edges) {
    int n = edges.size() + 1;
    vector< vector< int > > g(n);
    for (auto edge : edges) {
        g[edge.first].push_back(edge.second);
        g[edge.second].push_back(edge.first);
    }
    return g;
}

pair< vector< int >, int> closest_k(vector< vector< int > > g, int p, int k) {
    int n = g.size();
    queue< int > Q;
    vector< int > vis(n, -1);
    vector< int > ans;
    int depth = 0;

    Q.push(p);
    vis[p] = 0;
    k--;
    ans.push_back(p);
    while (!Q.empty() && k > 0) {
        p = Q.front();
        Q.pop();

        for (int u : g[p]) {
            if (vis[u] < 0 && k > 0) {
                Q.push(u);
                vis[u] = vis[p] + 1;
                depth = vis[u];
                ans.push_back(u);
                k--;
            }
        }
    }

    return make_pair(ans, depth);
}

void print_test(vector< pair< int, int > > edges, vector< int > masks, int K, int L) {
    assert(1 <= test && test <= NTESTS);

    char fname[100];
    sprintf(fname, template_path, test);
    cerr << fname << '\n';

    freopen(fname, "w", stdout);
    test += 1;

    int n = edges.size() + 1;
    assert(1 <= n && n <= MAXN);
    assert(1 <= L && L <= K && K <= B);

    printf("%d %d %d\n", n, K, L);

    assert(masks.size() == n);
    for (auto mask : masks) {
        assert(0 <= mask && mask < (1 << B));
        for (int i = 0; i < K; ++i) {
            printf("%d", ((mask >> i) & 1));
        }
        printf("\n");
    }

    assert(closest_k(edges_to_graph(edges), 0, n).first.size() == n);

    for (auto edge : edges) {
        assert(0 <= edge.first && edge.first < n);
        assert(0 <= edge.second && edge.second < n);
        printf("%d %d\n", edge.first + 1, edge.second + 1);
    }
}    

int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);

    // sample test
    print_test(vector< pair < int , int > >{
                make_pair(0, 1),
                make_pair(2, 1),
                make_pair(2, 3),
                make_pair(3, 4),
                make_pair(3, 5)
            },
            vector< int >{
                0b001,
                0b100,
                0b011,
                0b010,
                0b000,
                0b010
            },
            3, 2);

    // small tests
    print_test(vector< pair < int, int > >{ }, vector< int > {0}, B, 1);
    print_test(vector< pair < int, int > >{ }, vector< int > {(1 << B) - 1}, B, B);

    print_test(vector< pair < int, int > >{
            make_pair(0, 1)},
            vector< int >{0b0101, 0b1010},
            4, 3);


    // random tests
    while (test <= NTESTS) {
        int n, t;

        int K = B, L;
        int bitBias;
        if (test <= 10) { // small tests
            n = rnd.next(8, 20);
            if (test == 10) {
                t = 100000;
            } else {
                t = rnd.next(-5, 5);
            }
            K = B / 2;
            bitBias = 2;
        } else if (test <= 15) { // smallish tests
            n = rnd.next(100, 1000);
            if (test == 15) {
                t = 100000;
            } else {
                t = rnd.next(-20, 20);
            }
            K = B / 2;
            bitBias = 4;
        } else if (test <= 20) { // large tests
            n = rnd.next(MAXN * 9 / 10, MAXN);
            if (test == 20) {
                t = 100000;
            } else {
                t = rnd.next(-500, 500);
            }
        } else { // likely large tests
            n = rnd.next(1, MAXN);
            t = rnd.next(-100, 100);
        }

        // generate the graph
        vector< pair < int, int > > edges;
        if (t > 10000) {
            edges = path(n);
        } else {
            edges = random_tree(n, t);
        }
        auto g = edges_to_graph(edges);

        L = rnd.next(1, K);

        vector< int > masks(n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < K; ++j) {
                masks[i] = (masks[i] << 1) | rnd.wnext(2, -bitBias);
            }
        }

        // guaranteing a big component of useless towns.
        int p = rnd.next(1, n);
        vector< int > closest = closest_k(g, p, n / 10).first;
        for (auto u : closest) {
            masks[u] = (1 << (L - 1)) - 1; 
        }

        print_test(edges, masks, K, L);
        int l = 0, r = n;
        while (r - l > 1) {
            int m = (l + r) >> 1;
            if (closest_k(g, p, n).second < m) {
                r = m;
            } else {
                l = m;
            }
        }
 
        cerr << "n = " << n << '\n';
        cerr << "t = " << t << '\n';
        cerr << "diam ~= " << l << '\n';
        cerr << '\n';
    }

    return 0;
}

