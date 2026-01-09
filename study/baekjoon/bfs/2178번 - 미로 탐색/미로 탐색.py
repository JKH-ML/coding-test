# BFS의 원칙
# 1. 큐에서 꺼낸 노드는 이미 '방문 처리된 상태'여야 한다.
# 2. 어떤 노드를 큐에 넣는 순간, 반드시 방문 처리를 동시에 한다.
#    (그래야 같은 노드가 여러 번 큐에 들어가지 않는다)
# 3. 하나의 좌표(정점)는 BFS 전체 과정에서 최대 한 번만 큐에 들어간다.
# 4. 거리 정보는 '부모 노드의 거리 + 1'로 갱신하며,
#    방문 처리와 거리 갱신은 분리하지 않는다.
# 5. q[0]을 참조하지 말고, 반드시 popleft()로 값을 꺼내 사용한다.

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))
DATA = [[int(x) for x in input().rstrip()] for _ in range(N)]

def solution(n, m, data):
    dx = [1, 0, -1, 0]  # 행
    dy = [0, -1, 0, 1]  # 열

    q = deque()
    q.append((1, 1))          # start point (1-indexed)
    data[0][0] = 1            # 시작 지점 거리

    while q:
        x0, y0 = q.popleft()
        for k in range(4):
            x = x0 + dx[k]
            y = y0 + dy[k]
            if 1 <= x <= n and 1 <= y <= m and data[x-1][y-1] == 1:
                data[x-1][y-1] = data[x0-1][y0-1] + 1
                q.append((x, y))

    return data[n-1][m-1]

print(solution(N, M, DATA))
