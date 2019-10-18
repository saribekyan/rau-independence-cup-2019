from itertools import accumulate

INF = 10 ** 19

def solution(A):
    n = len(A)
    S = tuple(accumulate([0] + list(A)))
    dp = [ INF ] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + (S[i] - S[j]) ** 2)

    return (S[n] ** 2 - dp[n]) // 2

import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    print(solution(A))

