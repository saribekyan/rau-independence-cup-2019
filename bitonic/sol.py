import sys

def solution(A):
    n = len(A)
    x = [None] * n
    x[0] = (A[0], 0)
    currVal = A[0]
    currTotal = 0
    for i in range(1, n):
        currVal = max(currVal + 1, A[i])
        currTotal += currVal - A[i]
        x[i] = (currVal, currTotal)

    answer = currTotal

    currVal = A[-1]
    currTotal = 0
    for i in range(n - 2, -1, -1):
        currVal = max(currVal + 1, A[i])
        currTotal += currVal - A[i]
        
        answer = min(answer,
            currTotal + x[i][1] - (min(currVal, x[i][0]) - A[i]))

    return answer

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    A = map(int, sys.stdin.readline().split())
    print(solution(A))

