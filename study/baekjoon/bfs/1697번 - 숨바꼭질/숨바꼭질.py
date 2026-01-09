import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().rstrip().split(' '))

def solution(n, k):
    if n == k:
        return 0
    limit = 100000
    visited = [False] * (limit + 1)
    Q = deque([(n,0)])
    visited[n] = True
    while Q:
        x = Q.popleft()
        candidate = [x[0]-1, x[0]+1, 2*x[0]]
        for nx in candidate: 
            if nx == k:
                return x[1]+1
            if 0 <= nx <= limit and not visited[nx] :
                Q.append((nx, x[1]+1))
                visited[nx] = True
                
print(solution(N, K))