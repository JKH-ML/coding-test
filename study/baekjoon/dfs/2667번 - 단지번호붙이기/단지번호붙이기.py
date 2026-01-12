# BFS
# import sys
# from collections import deque
# input = sys.stdin.readline

# def solution(n, data):
#     dx = [1,0,-1,0] 
#     dy = [0,-1,0,1] 
#     result = []
#     for i in range(n):
#         for j in range(n):
#             if data[i][j] == 1:
#                 count = 0
#                 Q = deque([(i, j)])
#                 data[i][j] = 2
#                 while Q:
#                     x, y = Q.popleft()
#                     count += 1
#                     for d in range(4):
#                         nx = x + dx[d]
#                         ny = y + dy[d]
#                         if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 1:
#                             Q.append((nx,ny))
#                             data[nx][ny] = 2
#                 result.append(count)
#     result.sort()
#     return str(len(result)) + '\n' + '\n'.join(map(str, result))

# N = int(input().rstrip())
# DATA = [list(map(int, input().rstrip())) for _ in range(N)]
# print(solution(N, DATA))

#DFS
import sys
input = sys.stdin.readline

def solution(n, data):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    result = []

    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                count = 0
                S = [(i, j)]
                data[i][j] = 2

                while S:
                    x, y = S.pop()
                    count += 1

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 1:
                            S.append((nx, ny))
                            data[nx][ny] = 2

                result.append(count)

    result.sort()
    return str(len(result)) + '\n' + '\n'.join(map(str, result))

N = int(input().rstrip())
DATA = [list(map(int, input().rstrip())) for _ in range(N)]
print(solution(N, DATA))
