import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [int(input().rstrip()) for _ in range(N)]

def solution(n, data):
    result = []
    for command in data:
        # print(result) # 디버깅
        if command == 0:
            result.pop()
        else: 
            result.append(command)
    return sum(result)

print(solution(N, DATA))


