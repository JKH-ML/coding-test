import sys
from collections import deque

input = sys.stdin.readline
M, N, H = map(int, input().split()) 

# 가로 칸의 수(y, 열 인덱스) / 세로 칸의 수(x, 행 인덱스) / 층 수 (z, 층 인덱스)
DATA = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def solution(m, n, h, data):
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    q = deque()

    # 멀티 소스 BFS 시작점 수집
    for i in range(n):
        for j in range(m):
            for k in range(h):
                if data[k][i][j] == 1:
                    q.append((k, i, j))

    # BFS
    while q:
        z, x, y = q.popleft()
        for direction in range(6):
            nx = x + dx[direction]
            ny = y + dy[direction]
            nz = z + dz[direction]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if data[nz][nx][ny] == 0:
                    data[nz][nx][ny] = data[z][x][y] + 1
                    q.append((nz, nx, ny))

    # 결과 확인
    max_day = 0
    for i in range(n):
        for j in range(m):
            for k in range(h):
                if data[k][i][j] == 0:
                    return -1
                max_day = max(max_day, data[k][i][j])

    return max_day - 1 # 1로 시작했기 때문에 보정

print(solution(M, N, H, DATA))

