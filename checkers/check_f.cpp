#include <string>
#include <iostream>
#include <vector>
#include "../testlib/testlib.h"
using namespace std;

#define NMAX 20
#define AMAX 1000000000

int main(int argc, char * argv[]) {
    setName("Check output of problem homework.");
    registerTestlibCmd(argc, argv);

    int n = inf.readInt();
    int a = inf.readInt();

    int possibilityCheck = ans.readInt();

    if (possibilityCheck == -1) {
        int res = ouf.readInt();
        if (res != -1) {
            quitf(_wa, "solution is found, but none exists");
        }
        quitf(_ok, "no solution");
    }

    vector< int > curr = ouf.readInts(n, 1, AMAX);
    for (int i = n - 1; i > 0; --i) {
        vector< int > next = ouf.readInts(i, 1, AMAX);
        for (int j = 0; j < i; ++j) {
            if (curr[j] + curr[j + 1] != next[j]) {
                quitf(_wa, "rows do not add correctly");
            }
        }
        curr = next;
    }
    if (a != curr[0]) {
        quitf(_wa, "final answer, expected %d, received %d", a, curr[0]);
    }
    quitf(_ok, "%d", a);
    return 0;
}

