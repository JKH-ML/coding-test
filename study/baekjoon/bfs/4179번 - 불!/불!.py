import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
DATA = [list(input().rstrip()) for _ in range(R)]

def solution(r, c, data):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    fire_time = [[-1]*c for _ in range(r)]
    jihun_time = [[-1]*c for _ in range(r)]

    F = deque()
    J = deque()

    for i in range(r):
        for j in range(c):
            if data[i][j] == 'F':
                F.append((i, j))
                fire_time[i][j] = 0
            elif data[i][j] == 'J':
                J.append((i, j))
                jihun_time[i][j] = 0

    # Fire BFS
    while F:
        x, y = F.popleft()
        for k in range(4):
            xn = x + dx[k]
            yn = y + dy[k]
            if 0 <= xn < r and 0 <= yn < c:
                if data[xn][yn] != '#' and fire_time[xn][yn] == -1:
                    fire_time[xn][yn] = fire_time[x][y] + 1
                    F.append((xn, yn))

    # Jihun BFS
    while J:
        x, y = J.popleft()

        if x == 0 or x == r-1 or y == 0 or y == c-1:
            return jihun_time[x][y] + 1

        for k in range(4):
            xn = x + dx[k]
            yn = y + dy[k]
            if 0 <= xn < r and 0 <= yn < c:
                if data[xn][yn] != '#' and jihun_time[xn][yn] == -1:
                    if fire_time[xn][yn] == -1 or fire_time[xn][yn] > jihun_time[x][y] + 1:
                        jihun_time[xn][yn] = jihun_time[x][y] + 1
                        J.append((xn, yn))

    return 'IMPOSSIBLE'

print(solution(R, C, DATA))
