import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [input().rstrip() for _ in range(N)]

def solution(n, data):
    result = []
    q = deque()
    for command in data:
        if len(command) > 5:
            if command[:6] == 'push_f': # push_front X
                q.appendleft(int(command[11:]))
            elif command[:6] == 'push_b': # push_back X
                q.append(int(command[10:]))
            elif command[:6] == 'pop_fr': # pop_front
                if len(q) > 0:
                     result.append(q.popleft())
                else:
                    result.append(-1)
            elif command[:6] == 'pop_ba': # pop_back
                if len(q) > 0:
                     result.append(q.pop())
                else:
                    result.append(-1)
                
        else:
            if command[0] == 's': # size
                result.append(len(q))
            elif command[0] == 'e': # empty
                if len(q) == 0:
                     result.append(1)
                else:
                    result.append(0)
            elif command[0] == 'f': # front
                if len(q) > 0:
                     result.append(q[0])
                else:
                    result.append(-1)
            elif command[0] == 'b': # back
                if len(q) > 0:
                     result.append(q[-1])
                else:
                    result.append(-1)
        
    return '\n'.join([str(x) for x in result])

print(solution(N, DATA))