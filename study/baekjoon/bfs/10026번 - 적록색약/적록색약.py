import sys
from collections import deque
input = sys.stdin.readline

def solution(n, data):
    dx = [1,0,-1,0] 
    dy = [0,-1,0,1] 
    sector = [0, 0, 0, 0] # red, green, blue, yellow

    # bfs로 R G B 구역을 센다. -> r g b
    for i in range(n):
        for j in range(n):
            for idx, color in enumerate([('R','r'), ('G','g'), ('B','b')]):
                if data[i][j] == color[0]: # 대문자 발견하면
                    sector[idx] += 1
                    Q = deque([(i,j)])
                    data[i][j] = color[1] # 소문자로 바꾸는게 방문 처리
                    while Q:
                        x,y = Q.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == color[0]:
                                Q.append((nx,ny))
                                data[nx][ny] = color[1]
    
    # bfs로 r g 구역을 센다. -> y
    for i in range(n):
        for j in range(n):
            if data[i][j] in ('r', 'g'): # 'r' 또는 'g' 발견하면
                sector[3] += 1
                Q = deque([(i,j)])
                data[i][j] = 'y' # y로 바꾸는게 방문 처리
                while Q:
                        x,y = Q.popleft()
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] in ('r', 'g'):
                                Q.append((nx,ny))
                                data[nx][ny] = 'y'
    
    return f'{sector[0]+sector[1]+sector[2]} {sector[2]+sector[3]}'

N = int(input().rstrip())
DATA = [list(input().rstrip()) for _ in range(N)]
print(solution(N, DATA))



