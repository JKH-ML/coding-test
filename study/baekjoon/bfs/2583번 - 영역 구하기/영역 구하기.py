import sys
from collections import deque
input = sys.stdin.readline

def solution(h, w, data): # 5 7
    dx = [1,0,-1,0] 
    dy = [0,-1,0,1] 
    result = []
    paper = [[0 for _ in range(w)] for _ in range(h)]
    for k in range(len(data)):
        a,b,c,d = data[k] # 0 2 4 4
        for i in range(b, d):
            for j in range(a, c):
                paper[i][j] = -1
    
    for i in range(h):
        for j in range(w):
            if paper[i][j] == 0:
                s = 0
                paper[i][j] = 1
                Q = deque([(i, j)])
                while Q:
                    x, y = Q.popleft()
                    s = s + 1
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0<=nx<h and 0<=ny<w and paper[nx][ny] == 0:
                            Q.append((nx,ny))
                            paper[nx][ny] = paper[x][y] + 1
                result.append(s)
    result.sort()
    return f'{len(result)}\n' + ' '.join([str(x) for x in result])

M, N, K = map(int, input().rstrip().split(' '))
DATA = [tuple(map(int, input().rstrip().split(' '))) for _ in range(K)]
print(solution(M, N, DATA))