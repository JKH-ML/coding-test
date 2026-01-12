import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, data):
    dx = [1,0,-1,0] 
    dy = [0,-1,0,1] 
    dist = [[[-1]*m for _ in range(n)] for _ in range(2)]

    Q = deque()
    Q.append((0,0,0)) # (사용한 드릴 수, x 좌표, y 좌표)
    dist[0][0][0] = 1
    while Q:
        drill, x, y =  Q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                # 드릴 안쓰고 0인 지역으로 이동
                if data[nx][ny] == 0 and dist[drill][nx][ny] == -1:
                    Q.append((drill,nx,ny))
                    dist[drill][nx][ny] = dist[drill][x][y] + 1
                # 드릴 쓰고 1인 지역으로 이동
                if data[nx][ny] == 1 and dist[1][nx][ny] == -1 and drill == 0:
                    Q.append((1,nx,ny))
                    dist[1][nx][ny] = dist[0][x][y] + 1

    a = dist[0][n-1][m-1]
    b = dist[1][n-1][m-1]

    if a == -1 and b == -1:
        return -1
    elif a == -1:
        return b
    elif b == -1:
        return a
    else:
        return min(a, b)

N, M = map(int, input().strip().split())
DATA = [list(map(int, input().strip())) for _ in range(N)]
print(solution(N, M, DATA))