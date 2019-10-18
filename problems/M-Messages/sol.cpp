#include <stdio.h>
#include <iostream>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)

struct node {
    int part, end;
    node *l, *r;
} start;

int main() {
    int M, N; scanf("%d %d", &M, &N);
    REP(i, M) {
        int b; scanf("%d", &b);
        node *at = &start;
        REP(i, b) {
            int bit; scanf("%d", &bit);
            if (bit == 0) {
                if (at->l == NULL) at->l = new node();
                at = at->l;
            }
            else {
                if (at->r == NULL) at->r = new node();
                at = at->r;
            }
            at->part++;
        }
        at->end++;
    }

    REP(i, N) {
        int b; scanf("%d", &b);
        int matches = 0;
        node *at = &start;
        REP(i, b) {
            int bit; scanf("%d", &bit);
            if (at == NULL) continue;
            matches += at->end;
            if (bit == 0) at = at->l;
            else at = at->r;
        }
        if (at != NULL) matches += at->part;
        printf("%d\n", matches);
    }
    return 0;
}