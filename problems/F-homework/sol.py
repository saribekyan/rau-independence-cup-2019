import sys

n, a = map(int, sys.stdin.readline().split())

if a < 2 ** (n - 1):
    print(-1)
else:
    s = [ 1 ] * (n - 1) + [ a - 2 ** (n - 1) + 1 ]
    
    for i in range(n):
        print(' '.join(map(str, s[ : n - i])))
        for j in range(n - i - 1):
            s[j] += s[j + 1]

