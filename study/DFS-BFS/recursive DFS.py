# 각 노드의 연결 정보
graph = [
	[],
	[2, 3, 8],
	[1, 7],
	[1, 4, 5],
	[3, 5],
	[3, 4],
	[7],
	[2, 6, 8],
	[1, 7]
]

# 각 노드의 방문 여부 정보
visited = [False] * 9

# DFS 메서드 정의 (재귀적)
def DFS(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v] = True
	print(v, end=' ')

	for i in graph[v]:
		if not visited[i]:
			DFS(graph, i, visited)
   
DFS(graph, 1, visited)