import sys
from collections import deque
input = sys.stdin.readline

def solution(l, r, c, data):
    dz = [0,0,0,0,1,-1]
    dx = [1,0,-1,0,0,0] 
    dy = [0,-1,0,1,0,0] 
    dist = [[[-1] * c for _ in range(r)] for _ in range(l)]
    Q = deque()
    # print(data)
    found = False
    for k in range(l):
        for i in range(r):
            for j in range(c):
                if data[k][i][j] == 'S':
                    Q.append((k, i, j))
                    dist[k][i][j] = 0
                    found = True
                    break
            if found:
                break
        if found:
            break
    
    while Q:
        z, x, y = Q.popleft()
        # print(f'{z, x, y} poped out')
        for d in range(6):
            nz = z + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]
            if 0<=nz<l and 0<=nx<r and 0<=ny<c :
                if data[nz][nx][ny] == 'E':
                    return f'Escaped in {dist[z][x][y] + 1} minute(s).'
                if data[nz][nx][ny] == '.' and dist[nz][nx][ny] == -1 :
                    Q.append((nz,nx,ny))
                    dist[nz][nx][ny] = dist[z][x][y] + 1
    return 'Trapped!'

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    DATA = []
    for _ in range(L):
        DATA.append([list(input().strip()) for _ in range(R)])
        input() # for blank line
    print(solution(L, R, C, DATA))
