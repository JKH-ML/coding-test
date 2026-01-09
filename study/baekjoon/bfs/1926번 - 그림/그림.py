# BFS는 일반적으로 큐(Queue) 자료구조를 사용하여 구현됩니다. 
# 1) 시작 정점을 큐에 넣고 방문 처리합니다.
# 2) 큐에서 하나의 정점을 꺼냅니다.
# 3) 해당 정점과 인접한 정점들 중 아직 방문하지 않은 정점들을 모두 큐에 넣고 
# 방문 처리합니다.
# 4) 큐가 빌 때까지 2)~3)을 반복합니다.

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(' '))
DATA = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

def solution(n, m, data):
    result = [] # len(result), max(result)을 return 한다.
    # 아이디어: 0은 방문, 1은 미방문으로 보고
    # 미방문 점에 대해 while을 돌면서 size를 키워나가, result에 append한다.
    # 알고리즘: bfs
    # 자료구조: queue
    # 시간복잡도: o(nm)
    dx = [1, 0, -1, 0] # 행
    dy = [0, -1, 0, 1] # 열
    for i in range(n):
        for j in range(m):
            if data[i][j] == 1: # 방문처리 안된 지점을 찾으면
                data[i][j] = 0 # 방문처리하고 
                size = 0 # 사이즈 초기화
                q = deque() # 큐 초기화
                q.append((i,j))
                while q: # 큐가 빌 때까지 while을 돈다.
                    # q[0] 에 대해 주변을 봐서 
                    # 범위 내에 있으면서 미방문인 점이 있으면
                    # 큐에 append 하고, 방문처리 하고 
                    # 4방향 조사 끝나면 q[0] 는 popleft() 로 뺀다.
                    # 큐에서 1개 뺄 때마다 size를 늘린다.
                    for k in range(4):
                        x = q[0][0] + dx[k]
                        y = q[0][1] + dy[k]
                        if 0 <= x < n and 0 <= y < m and data[x][y] == 1:
                            q.append((x,y))
                            data[x][y] = 0
                    q.popleft()
                    size += 1
                result.append(size)
    if not result:
        return "0\n0"
    return str(len(result)) + '\n' + str(max(result))

print(solution(N, M, DATA))