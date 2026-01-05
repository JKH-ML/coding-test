import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [int(x) for x in input().rstrip().split(' ')]

def solution(n, data):
    result = [-1] * n
    stack = [] 
    stack.append(data[-1])
    for i in range(2,n+1): 
        while stack and data[-i] >= stack[-1]:
            stack.pop()
        if stack:
            result[-i] = stack[-1]
        stack.append(data[-i])
    return ' '.join([str(x) for x in result])

print(solution(N, DATA))