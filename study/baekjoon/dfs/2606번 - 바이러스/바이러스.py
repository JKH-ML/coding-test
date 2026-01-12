import sys
input = sys.stdin.readline

# DFS
def solution(data, start):
    visited = [False] * len(data)
    result = []
    def dfs_recursive(x):
        visited[x] = True
        result.append(x)
        for nx in data[x]:
            if not visited[nx]:
                dfs_recursive(nx)
    dfs_recursive(start)
    return len(result) - 1 # 자기 자신 제외

N = int(input().strip())
M = int(input().strip())
V = 1
GRAPH = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    GRAPH[a].append(b)
    GRAPH[b].append(a)
print(solution(GRAPH, V))