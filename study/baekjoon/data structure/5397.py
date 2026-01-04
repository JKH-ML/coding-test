import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [input().rstrip() for _ in range(N)]


def solution(n, data):
    result = []
    for i in range(n):
        left, right = [], []
        for s in data[i]:
            if s=='<' and left:
                right.append(left.pop())
            elif s=='>' and right:
                left.append(right.pop())
            elif s=='-' and left:
                left.pop()
            elif s!='<' and s!='>' and s!='-':
                left.append(s)
        result.append(''.join(left + right[::-1]))
    return '\n'.join(result)

print(solution(N, DATA))