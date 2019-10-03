#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main() {
    int n;
    cin >> n;
    while (n--) {
        int curr = 0;
        int next = 1;
        if (rand() % 2 == 0) {
            next = -1;
        }
        while (true) {
            cout << next - curr << '\n';

            string found;
            cin >> found;
            if (found == "yes") {
                break;
            }
            curr = next;
            next *= -2;
        }
    }
    return 0;
}

