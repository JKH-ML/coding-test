import sys
input = sys.stdin.readline

N = int(input().rstrip())
DATA = [int(input().rstrip()) for _ in range(N)]

def solution(n, data):
    result = []
    stack = []
    currentMax = 0

    for i in data:
        if i > currentMax:
            for x in range(currentMax + 1, i + 1):
                stack.append(x)
                result.append('+')
            currentMax = i

        # 여기서 검증
        if stack[-1] != i:
            return 'NO'

        stack.pop()
        result.append('-')

    return '\n'.join(result)

print(solution(N, DATA))