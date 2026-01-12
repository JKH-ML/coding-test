import sys
from collections import deque
input = sys.stdin.readline

def solution(n, data):
    dx = [1,0,-1,0] 
    dy = [0,-1,0,1] 
    result = []
    # 비가 0(모두 안잠김)부터 maxHeight(모두 잠김) 전까지 내리는 모든 경우에 대해 
    # 안전 영역이 몇 개인지 bfs로 count -> result에 append한다.
    maxHeight = max(map(max, data)) 
    for rain in range(maxHeight):
        visited = [[False for _ in range(n)] for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(n):
                if visited[i][j] == False and data[i][j] > rain:
                    count += 1
                    Q = deque([(i, j)])
                    visited[i][j] = True
                    while Q:
                        x, y = Q.popleft()
                        for d in range(4):
                            nx = x + dx[d]
                            ny = y + dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                if visited[nx][ny] == False and data[nx][ny] > rain:
                                    Q.append((nx,ny))
                                    visited[nx][ny] = True
        result.append(count)
    return max(result)

N = int(input().rstrip())
DATA = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, DATA))