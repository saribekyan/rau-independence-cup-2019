import sys
import string
from operator import add, sub, mod

MOD = 10 ** 9 + 7
alphabet = string.ascii_lowercase

### Matrix stuff ###

def zeros(n, m):
    return [[0] * m for i in range(n)]

def identity(n):
    A = zeros(n, n)
    for i in range(n):
        A[i][i] = 1
    return A

# https://stackoverflow.com/questions/10508021/matrix-multiplication-in-python
def matXmat(a, b):
    zip_b = zip(*b)
    # uncomment next line if python 3 : 
    zip_b = list(zip_b)
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) % MOD 
             for col_b in zip_b] for row_a in a]

def matOp(A, B, op): # op = add or sub
    modList = [MOD] * len(A)
    return [list(
        map(mod,
            map(add,
                map(op, r1, r2),
                modList),
            modList))
        for r1, r2 in zip(A, B)]

def matrixPower(A, N):
    n = len(A)
    if N == 0:
        return identity(n)
    
    B = matrixPower(A, N // 2)
    B = matXmat(B, B)
    if N % 2 == 1:
        B = matXmat(B, A)
    return B

# returns the sum we need, and auxiliary powers of A and B
def ACBpowerSum(A, C, B, N):
    if N == 0:
        return C, identity(len(A)), identity(len(A))

    k = N // 2
    R, Ak, Bk = ACBpowerSum(A, C, B, k)

    AN = matXmat(Ak, Ak)
    BN = matXmat(Bk, Bk)

    if N == 2 * k + 1:
        R = matOp(
            matXmat(R, matXmat(Bk, B)),
            matXmat(matXmat(Ak, A), R),
            add
        )
        AN = matXmat(AN, A)
        BN = matXmat(BN, B)
    else:
        R = matOp(
            matOp(
                matXmat(R, Bk),
                matXmat(Ak, R),
                add
            ),
            matXmat(matXmat(Ak, C), Bk),
            sub
        )
    return R, AN, BN

### END OF MATRICES ###

def moveRight(s1, s2): # len(s2) >= len(s1)
    for i in range(1, len(s1)):
        if s1[i:] == s2[:len(s1) - i]:
            return i
    return len(s1)

def matrixForString(K, X):
    n = len(X)
    
    t2i = lambda p, k: p * (K + 1) + k # tuple to index
    i2t = lambda i: (i // (K + 1), i % (K + 1)) # index to tuple

    N = t2i(n - 1, K) + 1 # matrix size
    A = zeros(N, N)

    for i in range(N):
        p, k = i2t(i)
        for x in alphabet:
            if x == X[p]:
                if p == n - 1:
                    if k > 0:
                        A[i][t2i(n - moveRight(X, X), k - 1)] += 1
                else:
                    A[i][t2i(p + 1, k)] += 1
            else:
                A[i][t2i(p + 1 - moveRight(X[:p] + x, X), k)] += 1

    return A, t2i(0, K)

def solution(N, K1, K2, X, Y):

    A, k = matrixForString(K1, X)
    nA = len(A)
    # the number of strings of length i
    # that have up to K1 instances of X is
    #    e_k * A^i * ones_nA        where
    # e_k is a unit horizontal vector of dimension nA with 1 in kth location and
    # ones_nA is an all-one vertical vector of size nA

    B, s = matrixForString(K2, Y)
    nB = len(B)
    # the number of strings of length i
    # that have up to K2 instances of Y is
    #    e_s * B^i * ones_nB        where
    # e_s is a unit horizontal vector of dimension nB with 1 in kth location and
    # ones_nB is an all-one vertical vector of size nB

    # we pad A and B to make them the same size
    n = max(nA, nB)
    for X in A, B:
        for row in X:
            row += [0] * (n - len(X))
        X += [[0] * n for i in range(n - len(X))]

    # thus, the answer is
    #           sum_{i=0}^N (e_k * A^i * ones_n) * (e_s * B^{N - i} * ones_n)
    #           = e_k * ( sum_{i=0}^N (A^i * C * B^{N - i}) ) * ones_n , where
    #  C = ones_n * e_s , which is a square matrix
    
    # we can compute this sum using divide and conquer
    # the recursion is pretty self-explanatory

    e_k = [[0] * n]
    e_k[0][k] = 1
    e_s = [[0] * n]
    e_s[0][s] = 1
    ones = [[1] for i in range(n)]

    C = matXmat(ones, e_s)

    M, _, _ = ACBpowerSum(A, C, B, N)

    ans = matXmat(matXmat(e_k, M), ones)
    return ans[0][0]

if __name__ == '__main__':
    f = sys.stdin
    N = int(f.readline().strip())
    XA, KA = f.readline().split()
    XV, KV = f.readline().split()

    KA = int(KA)
    KV = int(KV)

    print(solution(N, KA, KV, XA, XV))

