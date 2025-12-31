from collections import deque

# BFS 메서드 정의
def BFS(graph, start, visited):

	# deque를 사용해 큐 구현
	queue = deque([start])

	# 현재 노드를 방문 처리
	visited[start] = True

	# 큐가 빌 때까지 반복
	while queue:
		v = queue.popleft()
		print(v, end=' ')
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

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

# BFS(graph, 1, visited)
BFS(graph, 7, visited)