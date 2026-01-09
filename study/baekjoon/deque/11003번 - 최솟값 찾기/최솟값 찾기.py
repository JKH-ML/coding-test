import sys
from collections import deque

input = sys.stdin.readline
write = sys.stdout.write

N, L = map(int, input().rstrip().split(' '))
DATA = list(map(int, input().rstrip().split(' ')))

def solution(n, l, data):
    q = deque()
    for i in range(n):
        while q and q[0][1] <= i - l:
            q.popleft()
        while q and q[-1][0] > data[i]:
            q.pop()
        q.append((data[i], i))
        write(str(q[0][0]))
        write(' ')

solution(N, L, DATA)
