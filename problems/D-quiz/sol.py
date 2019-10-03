import sys

def solution(S):
    n = len(S)
    ans = 0
    ans = [ ]
    if n > 3:
        if S[0] == '?':
            ans.append('1')
        else:
            ans.append(S[0])
        for x in S[1 : n - 3]:
            if x == '?':
                ans.append('0')
            else:
                ans.append(x)

        S = S[-3:]

    ok = False
    for i in range(0, 1000, 8):
        s = str(i)
        if n <= 3 and (i == 0 or len(s) != len(S)):
            continue

        while len(s) < len(S):
            s = '0' + s
        ok = True
        for j in range(len(S)):
            if S[j] != '?' and S[j] != s[j]:
                ok = False
        if ok:
            return ''.join(ans) + s

    if not ok:
        return '-1'

if __name__ == '__main__':
    print(solution(sys.stdin.readline().strip()))

