from itertools import accumulate

INF = 10 ** 19

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.min = [ INF ] * (4 * n)
        self.lmost = [ n ] * (4 * n)
        self.rmost = [ -1 ] * (4 * n)
        self.prev  = [ None ] * n
        self.next  = [ None ]  * n
        self.index_loc = [ None ] * n
        
    def set(self, index, val):
        l = 0
        r = self.n - 1
        p = 0

        ind_prev = -1
        ind_next = self.n
        while r > l:
            m = (l + r) >> 1
            if index <= m:
                p = (p << 1) | 1
                # the least index of the right child
                ind_next = min(ind_next, self.lmost[p + 1])

                r = m
            else:
                p = (p << 1) + 2
                # the largest index of the left child
                ind_prev = max(ind_prev, self.rmost[p - 1])

                l = m + 1

        self.prev[index] = ind_prev
        self.next[index] = ind_next

        if ind_prev >= 0:
            self.next[ind_prev] = index
        if ind_next < self.n:
            self.prev[ind_next] = index

        self.min[p] = val
        self.lmost[p] = self.rmost[p] = index

        if self.index_loc[index] is None:
            self.index_loc[index] = p

        while p > 0:
            p = (p - 1) >> 1

            self.min[p] = min(self.min[(p << 1) | 1], self.min[(p << 1) + 2])
            self.lmost[p] = min(self.lmost[(p << 1) | 1], self.lmost[(p << 1) + 2])
            self.rmost[p] = max(self.rmost[(p << 1) | 1], self.rmost[(p << 1) + 2])

    def rmost_ind_less_than_val(self, val):
        l = 0
        r = self.n - 1
        p = 0

        while r > l:
            m = (l + r) >> 1
            if self.min[(p << 1) + 2] > val:
                p = (p << 1) | 1
                r = m
            else:
                p = (p << 1) + 2
                l = m + 1

        return l

    def remove(self, index):
        self.next[self.prev[index]] = self.next[index]
        self.prev[self.next[index]] = self.prev[index]

        self.prev[index] = None
        self.next[index] = None

        p = self.index_loc[index]

        self.min[p] = INF
        self.lmost[p] = self.n
        self.rmost[p] = -1

        while p > 0:
            p = (p - 1) >> 1

            self.min[p] = min(self.min[(p << 1) | 1], self.min[(p << 1) + 2])
            self.lmost[p] = min(self.lmost[(p << 1) | 1], self.lmost[(p << 1) + 2])
            self.rmost[p] = max(self.rmost[(p << 1) | 1], self.rmost[(p << 1) + 2])

    def get_prev(self, index):
        return self.prev[index]

    def get_next(self, index):
        return self.next[index]

def solution(A):
    n = len(A)
    S = accumulate([0] + list(A))
    S = sorted(zip(S, range(n + 1)))
    slopeRank = [0] * (n + 1)
    for i in range(n + 1):
        slopeRank[S[i][1]] = i
    S = tuple([x[0] for x in S])
    # print(S)
    dp = [ None ] * (n + 1)
    dp[0] = 0
    
    # pdb.set_trace()
    
    a = [ None ] * (n + 1)
    b = [ None ] * (n + 1)
    lineLeftPt = [ None ] * (n + 1)
    lineRightPt = [ None ] * (n + 1)

    T = SegmentTree(n + 1)

    # line 0*x + 0, leftmost intersect at -INF
    r0 = slopeRank[0]
    T.set(r0, -INF)
    
    lineLeftPt[r0] = -INF
    lineRightPt[r0] = +INF
    a[r0] = 0
    b[r0] = 0

    def removeInd(i):
        a[i] = None
        b[i] = None
        lineLeftPt[i] = None
        lineRightPt[i] = None
        T.remove(i)

    for iInd in range(1, n + 1):
        # print(iInd)
        # print(S)
        # print(a, b)
        i = slopeRank[iInd]

        j = T.rmost_ind_less_than_val(S[i])

        # print(S[i], T.min[0])
        # print(j, slopeRank[iInd], slopeRank[0])

        res_i = S[i] ** 2 + a[j] + S[i] * b[j]

        a[i] = S[i] ** 2 + res_i
        b[i] = -2 * S[i]

        # temporary, so that the values next,prev are set
        # can be optimised
        T.set(i, INF)

        lineLeftPt[i] = -INF
        j = T.get_prev(i)

        while j >= 0:
            # print('left', i, j)
            j1 = T.get_prev(j)

            if b[i] == b[j]:
                if a[i] >= a[j]:
                    removeInd(i)
                    break
                else:
                    removeInd(j)
            else:
                x = (a[j] - a[i]) / (b[i] - b[j])
                if x <= lineLeftPt[j]:
                    removeInd(j)
                else:
                    T.set(i, x)
                    lineRightPt[j] = x
                    lineLeftPt[i] = x
                    break

            j = j1

        if j == -1:
            T.set(i, -INF)
            lineLeftPt[i] = -INF

        if lineLeftPt[i] is not None: # i did not get removed
            lineRightPt[i] = +INF
            j = T.get_next(i)

            # if iInd == 3:
            #     pdb.set_trace()

            while j <= n:
                # print('right', i, j)
                j1 = T.get_next(j)

                if b[i] == b[j]:
                    if a[i] >= a[j]:
                        removeInd(i)
                        break
                    else:
                        removeInd(j)
                else:
                    x = (a[j] - a[i]) / (b[i] - b[j])
                    if x >= lineRightPt[j]:
                        removeInd(j)
                    else:
                        T.set(j, x)
                        lineRightPt[i] = x
                        lineLeftPt[j]  = x
                        break

                j = j1

            if j > n:
                lineRightPt[i] = +INF
    # return res_i
    # print(res_i)
    total = sum(A)
    return (total ** 2 - res_i) // 2

def bf(A):
    n = len(A)
    S = tuple(accumulate([0] + list(A)))
    dp = [ INF ] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = min(dp[i], dp[j] + (S[i] - S[j]) ** 2)

    return dp[n]
    return (S[n] ** 2 - dp[n]) // 2

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().split()))
    print(solution(A))

