import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [input().rstrip() for _ in range(N)]

def solution(n, data):
    result = []
    q = deque()
    for command in data:
        if command[:2] == 'pu': q.append(command[5:])
        if command[:2] == 'po': 
            if len(q)==0: result.append(-1)
            else: result.append(q.popleft())
        if command[:2] == 'si': result.append(len(q))
        if command[:2] == 'em':
            if len(q)==0: result.append(1)
            else: result.append(0)
        if command[:2] == 'fr':
            if len(q)==0: result.append(-1)
            else: result.append(q[0])
        if command[:2] == 'ba':
            if len(q)==0: result.append(-1)
            else: result.append(q[-1])
    return '\n'.join([str(x) for x in result])

print(solution(N, DATA))