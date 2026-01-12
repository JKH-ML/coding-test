import sys
from collections import deque
input = sys.stdin.readline

def dfs(data, s):
    visited = [False] * len(data)
    result = []

    def dfs_recursive(x):
        # 1. 현재 노드를 방문 처리하고 결과에 추가
        visited[x] = True
        result.append(x)

        # 2. 현재 노드의 인접 노드 중에서
        # 방문하지 않은 노드에 대해 재귀적으로 DFS 수행
        for nx in data[x]:
            if not visited[nx]:
                dfs_recursive(nx)

    # 3. 탐색 시작 노드부터 DFS 수행
    dfs_recursive(s)

    return ' '.join(map(str, result))

"""
재귀 DFS에서 S = [] 같은 스택을 명시적으로 만들지는 않습니다. 
대신 논리적으로는 파이썬의 함수 호출 스택(call stack) 을 사용합니다. 
이 호출 스택이 역할상 DFS에서 말하는 “스택”과 동일합니다.
"""

def bfs(data, s):
    Q = deque()
    visited = [False] * len(data)
    result = []
    
    # 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
    Q.append(s)
    visited[s] = True
    
    # 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
    while Q:
        
        # 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 
        # 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
        x = Q.popleft()
        result.append(x)
        for d in range(len(data[x])):
            nx = data[x][d]
            if not visited[nx]:
                Q.append(nx)
                visited[nx] = True

    return ' '.join(map(str, result))


N, M, V = map(int, input().split()) # 정점의 수, 간선의 수, 탐색 시작점
DATA = [list(map(int, input().split())) for _ in range(M)] # 간선 연결 정보

GRAPH = [[] for _ in range(N+1)] # 주어진 노드 번호를 인덱스로 그대로 사용
for i in range(M): # 양방향 간선 그래프
    GRAPH[DATA[i][0]].append(DATA[i][1])
    GRAPH[DATA[i][1]].append(DATA[i][0])
for inner in GRAPH:
    inner.sort() # 정점 번호가 작은 것을 먼저 방문
    
print(dfs(GRAPH, V))
print(bfs(GRAPH, V))


