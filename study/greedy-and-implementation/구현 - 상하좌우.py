"""
여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다.
이 공간은 1 X 1 크기의 정사각형으로 나누어져있다. 
가장 위쪽 위 좌표는 (1,1) 이며 
아장 오른쪽 아래 좌표는 (N, N)에 해당한다. 
여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 
시작 좌표는 항상 (1, 1)이다. 
우리 앞에는 여행가 A가 이동할 계획이 적힌 계회서가 놓여 있다.
계획서에는 L,R,U,D중 하나의 문자가 반복적으로 적혀있으며, 
L은 왼쪽으로 한 칸, R은 오른쪽으로 한 칸, ... 이동한다.
이때 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다. 

입력 조건
첫째 줄에 공간의 크기를 나타내는 N이 주어진다 (1 <= N <= 100)
둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. ( 1<= 이동 횟수 <= 100)

출력 조건
첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 
공백으로 구분하여 출력한다.
"""

# 구현 유형, 시뮬레이션 유형, 완전 탐색 유형 <<< 이런 식으로 불림!

def solution(n, str):
    x, y = 1, 1 # 초기 위치는 1행 1열
    dx = [0, -1, 0, 1] # 행
    dy = [1, 0, -1, 0] # 열 
    direction = str.split()
    for i in range(len(direction)):
        if direction[i] == 'R':
            y += dy[0]
            if y > n:
                y -= 1
        if direction[i] == 'U':
            x += dx[1]
            if x < 1:
                x += 1
        if direction[i] == 'L':
            y += dy[2]
            if y < 1:
                y += 1
        if direction[i] == 'D':
            x += dx[3]
            if x > n:
                x -= 1
    return x, y

print(solution(3,'R R R R R R R R'))
print(solution(3,'R R R R R R R R D D D L L L L U'))

            