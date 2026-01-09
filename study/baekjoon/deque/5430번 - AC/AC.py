import sys
from collections import deque
input = sys.stdin.readline

T = int(input().strip())

def solution(cmds, d):
    r = False
    for c in cmds:
        if c == 'R':
            r = not r
        else:  # 'D'
            if not d:
                return 'error'
            if r:
                d.pop()
            else:
                d.popleft()

    if r:
        return '[' + ','.join(reversed(d)) + ']'
    else:
        return '[' + ','.join(d) + ']'

for _ in range(T):
    cmds = input().strip()
    _ = input().strip()  # num, 신뢰하지 않음
    arr_line = input().strip()

    if arr_line == "[]":
        data = deque()
    else:
        data = deque(arr_line[1:-1].split(','))

    print(solution(cmds, data))
   