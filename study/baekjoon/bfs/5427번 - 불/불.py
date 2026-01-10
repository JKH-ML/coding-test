import sys
from collections import deque
input = sys.stdin.readline

def solution(w, h, data):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    fire_time = [[-1]*w for _ in range(h)]
    character_time = [[-1]*w for _ in range(h)]

    F = deque()
    J = deque()

    for i in range(h):
        for j in range(w):
            if data[i][j] == '*':
                F.append((i, j))
                fire_time[i][j] = 0
            elif data[i][j] == '@':
                J.append((i, j))
                character_time[i][j] = 0

    # Fire BFS
    while F:
        x, y = F.popleft()
        for k in range(4):
            xn = x + dx[k]
            yn = y + dy[k]
            if 0 <= xn < h and 0 <= yn < w:
                if data[xn][yn] != '#' and fire_time[xn][yn] == -1:
                    fire_time[xn][yn] = fire_time[x][y] + 1
                    F.append((xn, yn))

    # Character BFS
    while J:
        x, y = J.popleft()

        if x == 0 or x == h-1 or y == 0 or y == w-1:
            return character_time[x][y] + 1

        for k in range(4):
            xn = x + dx[k]
            yn = y + dy[k]
            if 0 <= xn < h and 0 <= yn < w:
                if data[xn][yn] != '#' and character_time[xn][yn] == -1:
                    if fire_time[xn][yn] == -1 or fire_time[xn][yn] > character_time[x][y] + 1:
                        character_time[xn][yn] = character_time[x][y] + 1
                        J.append((xn, yn))

    return 'IMPOSSIBLE'

N = int(input().rstrip())
for _ in range(N):
    W, H = map(int, input().rstrip().split())
    DATA = [list(input().rstrip()) for _ in range(H)]
    print(solution(W, H, DATA))
