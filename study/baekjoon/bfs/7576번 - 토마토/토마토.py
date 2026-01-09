import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().rstrip().split(' '))
DATA = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

# 정수 1은 익은 토마토, 
# 정수 0은 익지 않은 토마토, 
# 정수 -1은 토마토가 들어있지 않은 칸
def solution(m, n, data):
    dx = [1,0,-1,0] 
    dy = [0,-1,0,1] 
    Q = deque()
    day = 0
    
    # 방문처리 = 며칠 뒤에 해당 위치의 토마토가 익는지 str로 표시
    for i in range(n):
        for j in range(m):
            if data[i][j]==1:
                Q.append((i,j)) # 스타팅 포인트 큐에 넣고 시작
                data[i][j] = '0' 
   
    while Q:
        x, y = Q.popleft()
        day = int(data[x][y])
        # print('day updated: ', data[x][y])
        for k in range(4):
            xn = x + dx[k]
            yn = y + dy[k]
            if 0 <= xn < n and 0 <= yn < m and data[xn][yn] == 0:
                Q.append((xn,yn))
                # print(xn,yn, 'added in Q')
                data[xn][yn] = str(int(data[x][y])+1)
    
    # 익지 않은 토마토 발견 -> -1 리턴
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                return -1
            
    # 정상 종료 시
    return day

print(solution(M, N, DATA))