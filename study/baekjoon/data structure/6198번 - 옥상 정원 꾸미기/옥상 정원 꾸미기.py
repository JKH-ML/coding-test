import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [int(input().rstrip()) for _ in range(N)]

def solution(n, data):
    # 보는 것을 기준으로 계산 == 보임을 당하는 것을 기준으로 계산
    result = 0
    stack = [data[0]]
    for i in range(1, n):
        if stack[-1] <= data[i]:
            while stack and stack[-1] <= data[i]:
                stack.pop()
        if stack:    
            result += len(stack)        
        stack.append(data[i])
    return result

print(solution(N, DATA))