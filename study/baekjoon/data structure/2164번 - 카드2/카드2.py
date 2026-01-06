import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())

def solution(n):
    if n==1: return 1
    if n==2: return 2
    q = deque([x+1 for x in range(n)])
    for _ in range(n-2):
        q.popleft()
        q.append(q.popleft())
    q.popleft()
    return q[0]

print(solution(N))