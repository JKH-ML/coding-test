import sys
input = sys.stdin.readline

def solution(w, h, data):
    dirs = [(-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0),  (1,1)]
    visited = [[False] * w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if data[i][j] == 1 and not visited[i][j]:
                count += 1
                S = [(i, j)]
                visited[i][j] = True
                while S:
                    x, y = S.pop()
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and  data[nx][ny] == 1:
                            if not visited[nx][ny]:
                                S.append((nx, ny))
                                visited[nx][ny] = True
    return count

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0: break
    DATA = []
    for _ in range(H): DATA.append(list(map(int, input().split())))
    print(solution(W, H, DATA))
