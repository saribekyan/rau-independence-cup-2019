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

    vector< long long > targets;
    long long prev = 0;
    for (int i = 0; i < n; ++i) {
        long long t = ans.readInt(-2 * XMAX, 2 * XMAX);
        targets.push_back(t);
        minPossibleTravel += abs(t - prev);
        prev = t;
    }

    long long currX = 0;

    int verdict = 0;

    tout << "n = " << n << endl;
    for (int i = 0; i < n; ++i) {
        long long targetX = targets[i];

        tout << "target " << i + 1 << ": " << targetX << endl;

        while (true) {
            long long jump = ouf.readInt();

            if (verdict == 0) {
                tout << "current = " << currX << endl;
                tout << "received jump = " << jump << endl;
            }

            if (currX + jump < -XMAX || currX + jump > XMAX) {
                if (verdict == 0) {
                    verdict = 1;
                }
            }

            if (currX < targetX && targetX <= currX + jump ||
                currX > targetX && targetX >= currX + jump) {

                totalTravel += abs(currX - targetX);
                currX = targetX;
            } else {
                totalTravel += abs(jump);
                currX += jump;
            }


            if (totalTravel > 8 * minPossibleTravel) {
                if (verdict == 0) {
                    verdict = 2;
                }
            }

            if (currX == targetX) {
                cout << "Yes " << currX << endl << flush;
                tout << "found " << targetX << endl << flush;
                break;
            } else {
                cout << "No " << currX << endl << flush;
            }
        }
        tout << endl << flush;
    }

    if (verdict == 0) {
        tout << "ok";
        quitf(_ok, "ok");
    } else if (verdict == 1) {
        tout << "Instruction sends too far";
        quitf(_wa, "Instruction sends too far");
    } else if (verdict == 2) {
        tout << "Too many steps";
        quitf(_wa, "Too many steps");
    }
}

