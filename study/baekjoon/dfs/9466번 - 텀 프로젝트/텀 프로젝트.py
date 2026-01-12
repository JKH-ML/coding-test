import sys
from collections import deque
input = sys.stdin.readline

def solution(n, data): 
    visited = [-1] * n # -1: not visited / 0: excluded / 1: included
    for i in range(n):
        team = []
        Q = deque()
        Q.append(i)
        while Q:
            x = Q.popleft()
            team.append(x)
            nx = data[x]
            if nx == i:
                for member in team:
                    visited[member] = 1
                    
            if visited[nx] == 1 and visited[i] != 1:
                
                
                    
    return

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    DATA = [x-1 for x in list(map(int, input().split()))]
    print(solution(N, DATA))