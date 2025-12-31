### 스택 자료구조

선입후출 (입구와 출구가 동일한 프링글스 통 같은 형태)
연산 - 삽입, 삭제

파이썬에서는 리스트 자료구조를 사용해서 스택을 구현한다.
append로 가장 오른쪽에 데이터를 삽입하거나
pop로 가장 오른쪽 데이터를 삭제할 수 있다.

```python
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop() # 3을 삭제함
print(stack) # [1, 2]
print(stack[::-1]) # [2, 1] 순서 거꾸로
```

---

### 큐 자료구조

선입선출 (입구와 출구가 다른 터널 같은 형태)
연산 - 삽입, 삭제

파이썬에서는 deque 라이브러리로 큐를 구현한다.
(리스트로 직접 구현하면 기능은 동일해도 삭제 연산 시
인덱스 재조정 과정에서 시간복잡도가 O(n)으로 늘어난다.)

```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft() # 1을 삭제함
print(queue) # deque([1, 2])
queue.reverse()
print(queue) # deque([2, 1])
```

---

### 재귀함수(Recursive function)

자기 자신을 다시 호출하는 함수

```python
def recursive_fcn():
	print('hello')
	recursive_fcn() # 자기 자신을 호출
recursive_fcn()
```

'hello'라는 문자열을 무한히 출력함.
어느 정도 출력하다가 "최대 재귀 깊이" 초과 메세지가 출력됨.
내부적으로 스택 안에 함수에 대한 정보가 담겨서 꽉차면 알아서 종료됨.

종료 조건을 명시해서 구현하는 것을 권장.
다음 코드의 실행 결과를 예측할 수 있어야 함.

```python
def recursive_fcn(i):
	if i == 100:
		return
	print(i, '번째가', i+1, '번을 호출함.')
	recursive_fcn(i+1)
	print(i, '번째 함수 종료.')

recursive_fcn(1)
```

재귀함수 대표 예제1: 팩토리얼 구현
반복문을 활용해 구현할 수 있지만,
수학적으로 0!=1!=1 임을 if문으로 구현하고
수식 n! = n \* (n-1)! 을 이용해서 재귀적으로도 구현할 수 있다.

```python
def factorial(n):
	if n<=1:
		return 1
	return n * factorial(n-1)

```

재귀함수 대표 예제2: 최대 공약수(GCD) 계산 - 유클리드 호제법

유클리드 호제법
두 자연수 A > B에 대해 A를 B로 나눈 나머지를 R이라 할 때,
GCD(A, B) = GCD(B, R)

예시 GCD(192, 162)
A B
1단계 192 162
2단계 162 30
3단계 30 12
4단계 12 6

```python
def recursive_GCD(a, b):
	if a%b == 0:
		return b
	else:
		return recursive_GCD(b, a%b)
```

참고로 위 코드에서
print(recursive_GCD(192, 162))
print(recursive_GCD(162, 192))
둘다 정상 작동함!

---

### DFS (Depth Firsh Search, 깊이 우선 탐색)

그래프 탐색 시 깊은 부분을 우선적으로 탐색하는 알고리즘.
스택 자료구조 혹은 재귀함수를 활용.

동작 과정

1. 탐색 시작 노드를 스택에 삽입 후 방문 처리.
2. 스택의 최상단 노드의 인접 노드 중 방문하지 않은 노드가 있다면
   그 노드를 스택에 삽입 후 방문 처리. 없다면 스택에서 최상단 노드 삭제.
3. 더 이상 2번의 과정을 반복할 수 없을 때까지 반복.

![](https://i.imgur.com/UBpwtG3.png)

탐색 순서: 1 -> 2 -> 7 -> 6 -> 8 -> 3 -> 4 -> 5

실제로 파이썬에서 DFS를 구현할 수 있다. (재귀적으로)
그래프에서 각 노드가 연결된 정보를 표현할 때는 2차원 리스트를 활용한다.
이 때 노드번호 1~8과 인덱스를 매칭시키기 위해 0번째 인덱스는 비워둔다.
또한 방문된 정보를 표시할 때는 1차원 리스트를 활용한다.

```python
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
def DFS(graph, v, visted):
	# 현재 노드를 방문 처리
	visited[v] = True
	print(v, end=' ')

	for i in graph[v]:
		if not visited[i]:
			DFS(graph, i, visted)
```


---


### BFS (Breadth Firsh Search, 너비 우선 탐색)

그래프 탐색 시 가까운 노드를 우선적으로 탐색하는 알고리즘.
큐 자료구조 혹은 재귀함수를 활용.

동작 과정

1. 탐색 시작 노드를 큐에 삽입 후 방문 처리.
2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리.
3. 더 이상 2번의 과정을 반복할 수 없을 때까지 반복.

![](https://i.imgur.com/UBpwtG3.png)

각 간선의 비용이 모두 동일하다면 '최단거리 문제'를 해결하는데 BFS를 사용할 수 있다.

```python
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
```