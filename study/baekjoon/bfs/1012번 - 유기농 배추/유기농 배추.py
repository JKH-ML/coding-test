import sys
from collections import deque
input = sys.stdin.readline

def solution(m, n, data):
    dx = [1,0,-1,0] 
    dy = [0,-1,0,1] 
    result = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                result += 1
                Q = deque()
                Q.append((i,j))
                data[i][j] = 0
                while Q:
                    x, y = Q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
                            Q.append((nx,ny))
                            data[nx][ny] = 0
    
    return result

T = int(input().rstrip())
for i in range(T):
    M, N, K = map(int, input().rstrip().split(' '))
    DATA = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().rstrip().split(' '))
        DATA[x][y] = 1
    print(solution(M, N, DATA))


