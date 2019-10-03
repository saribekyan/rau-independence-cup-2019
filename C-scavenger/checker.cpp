#include <string>
#include <iostream>
#include "../testlib/testlib.h"
using namespace std;

int main(int argc, char * argv[]) {
    setName("compares log of interactor to actual output");
    registerTestlibCmd(argc, argv);

    string rec = ouf.readString();

    if (rec != "ok") {
        quitf(_wa, " ");
    }
    quitf(_ok, " ");
    return 0;
}

