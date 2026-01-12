import sys
input = sys.stdin.readline

def solution(n, graph):
    visited = [False] * (n+1)
    count = 0
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            count += 1
            S = []
            S.append(i)
            while S:
                x = S.pop()
                for nx in graph[x]:
                    if not visited[nx]: 
                        visited[nx] = True
                        S.append(nx)
    return count

N, M = map(int, input().split())
GRAPH = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    GRAPH[a].append(b)
    GRAPH[b].append(a)
print(solution(N, GRAPH))
