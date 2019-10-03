#define EJUDGE

#include <iostream>
#include <cmath>
#include "../testlib/testlib.h"
using namespace std;

const long long XMAX = 1000000000;

int main(int argc, char * argv[]) {
    setName("interacts with user program");
    registerInteraction(argc, argv);

    int n;
    n = inf.readInt();
    cout << n << endl << flush;

    long long totalTravel = 0;
    long long minPossibleTravel = 0;

    long long currX = 0;
    for (int i = 0; i < n; ++i) {
        long long targetX  = ans.readInt(-2 * XMAX, 2 * XMAX);
        minPossibleTravel += abs(targetX - currX);

        while (true) {
            long long jump = ouf.readInt();
            if (currX < targetX && targetX <= currX + jump ||
                currX > targetX && targetX >= currX + jump) {
                totalTravel += abs(currX - targetX);
                currX = targetX;
                cout << "yes" << endl;
                break;
            } else {
                currX += jump;
                if (currX > XMAX || currX < -XMAX) {
                    tout << "went-too-far" << endl << flush;
                    quitf(_wa, "Went too far");
                }
                totalTravel += abs(jump);
                cout << "no" << endl;
            }
            cout.flush();
        }
    }

    if (totalTravel <= 8 * minPossibleTravel) {
        tout << "ok" << endl << flush;
        quitf(_ok, "%lldd steps <= 8 * %lld", totalTravel, minPossibleTravel);
    } else {
        tout << "too-many-steps" << endl << flush;
        quitf(_wa, "Too many steps");
    }
}

