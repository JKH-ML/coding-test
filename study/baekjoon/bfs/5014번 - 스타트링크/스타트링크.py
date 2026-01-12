import sys
from collections import deque
input = sys.stdin.readline

# 1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000
def solution(f, s, g, u, d):
    moves = [u, -d] 
    Q = deque()
    visited = [False] * (f + 1)
    visited[s] = True
    Q.append((s, 0)) # position and button
    while Q:
        pos, button = Q.popleft()
        if pos == g:
            return button
        for move in moves:
            next_pos = pos + move
            if 1 <= next_pos <= f and visited[next_pos] == False:
                visited[next_pos] = True
                Q.append((next_pos, button + 1))
    return "use the stairs"

F, S, G, U, D = map(int, input().rstrip().split())
print(solution(F, S, G, U, D))
