import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [input().rstrip() for _ in range(N)]

def solution(n, data):
    result = []
    stack = []
    for command in data:
        if command[:3] == 'pus': # push X
            stack.append(command[5:])
        if command[:3] == 'pop': # pop
            if stack:
                result.append(stack.pop())
            else:
                result.append('-1')
        if command[:3] == 'siz': # size
            result.append(str(len(stack)))
        if command[:3] == 'emp': # empty
            if stack:
                result.append('0')
            else:
                result.append('1')
        if command[:3] == 'top': # top
            if stack:
                result.append(str(stack[-1]))
            else:
                result.append('-1')
    return '\n'.join(result)

print(solution(N, DATA))