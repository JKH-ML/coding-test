import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = list(map(int, input().rstrip().split(' ')))
K = int(input().rstrip())

def solution(n, data, k):
    result = 0
    for i in range(n):
        if data[i] == k:
            result += 1
    return result

print(solution(N, DATA, K))