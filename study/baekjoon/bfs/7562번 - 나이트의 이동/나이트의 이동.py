import sys
from collections import deque
input = sys.stdin.readline

def solution(l, sx, sy, ex, ey):
    if (sx, sy)== (ex, ey):
        return 0
    dx = (2, -2, -2, 2, 1, 1, -1, -1)
    dy = (1, -1, 1, -1, 2, -2, 2, -2)
    visited = [[-1 for _ in range(l)] for _ in range(l)]
    Q = deque([(sx,sy)])
    visited[sx][sy] = 0
    while Q:
        x, y = Q.popleft()
        for k in range(8): 
            nx = x + dx[k]
            ny = y + dy[k]
            if nx == ex and ny == ey:
                return visited[x][y] + 1
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == -1 :
                Q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
N = int(input().rstrip())
for _ in range(N):
    L = int(input().rstrip())
    SX, SY = map(int, input().rstrip().split(' '))
    EX, EY = map(int, input().rstrip().split(' '))          
    print(solution(L, SX, SY, EX, EY))