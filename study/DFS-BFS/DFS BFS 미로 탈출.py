"""
문제
A는 N x M 크기의 직사각형 형태의 미로에 갇혀 있다. 
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다. 
현재 위치는 (1, 1)이고 미로의 출구는 (N,M)의 위치에 존재하며 
한 번에 한 칸씩 이동할 수 있다. 
괴물이 있는 부분은 0으로, 
괴물이 없는 부분은 1로 표시되어 있다. 
미로는 반드시 탈출할 수 있는 형태로 제시된다. 
탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

입력조건
첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다. 
다음 N개의 줄에는 각각 M개의 정수(0혹은 1)로 미로의 정보가 주어진다. 
각각의 수들은 공백 없이붙어서 입력으로 제시된다. 
또한 시작 칸과 마지막 칸은 항상 1이다.

출력 조건
첫째 줄에 최소 이동 칸의 개수를 출력한다.

입력 예시
5 6
101010
111111
000001
111111
111111

출력 예시
10
"""

# 테스트 데이터 input 받기
n, m = 5, 6
s = """101010
111111
000001
111111
111111"""
lines = s.split('\n') # ['101010','~',...]
array = []
for line in lines:
    row = []
    for element in line:
        row.append(int(element))
    array.append(row)
    
from collections import deque

def solution(n, m, array):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    queue = deque()
    queue.append((1, 1))

    while queue:
        x, y = queue.popleft()

        if x == n and y == m:
            return array[x-1][y-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1 <= nx <= n and 1 <= ny <= m:
                if array[nx-1][ny-1] == 1:
                    array[nx-1][ny-1] = array[x-1][y-1] + 1
                    queue.append((nx, ny))
                    
print(solution(n,m,array))