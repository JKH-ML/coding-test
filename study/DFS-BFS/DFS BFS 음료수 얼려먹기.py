"""
문제 설명
N x M 크기의 얼음틀이 있다. 
구멍이 뚫려있는 부분은 0, 
칸막이가 존재하는 부분은 1로 표시된다. 
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 
서로 연결되어 있는 것으로 간주한다. 
이때 얼음 틀의 모양이 주어졌을 때 
생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 
다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

입력 조건
첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. 
(1 <= N, M <= 1000)
두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

출력 조건
한 번에 만들 수 있는 아이스크림의 개수를 출력한다.

예시

입력
4 5
00110
00011
11111
00000

출력
3
"""

# dfs


def solution(n,m,array):
    result = 0
    
    def dfs(x, y):
        # 범위를 벗어나면 종료
        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        # 아직 방문하지 않은 경우
        if array[x][y] == 0:
            array[x][y] = 1  # 방문 처리

            # 상하좌우 재귀 호출
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

            return True
        return False
    
    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True:
                result += 1
    return result
            
n, m = 4, 5
array = [
[0,0,1,1,0],
[0,0,0,1,1],
[1,1,1,1,1],
[0,0,0,0,0]
]

print(solution(n,m,array))
                    

    
