import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [int(input().rstrip()) for _ in range(N)]
# 왼쪽으로 봐도 되고 오른쪽으로 봐도 된다.
# 왼쪽을 보는 기준으로 진행(스택 관리 편함)
# 같은 키가 연속으로 잇으면 카운트 해줘야함.
# 스택에는 키, 나포함 연속으로 같은 키인 사람의 수 저장
# 자신이 탑보다 더 크면 탑팝 -> 자신이 탑보다 작거나 같아지거나 스택이 비어야함
# 0 1 2 3 4 5 6 : index
# 2 4 1 2 2 5 1 : 키
# 0 1 1 2 2 3 1 : 왼쪽 봤을 때 보이는 사람의 수
def solution(n, data):
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and data[i] > stack[-1][0]:
            result[i] += stack[-1][1]
            stack.pop() 
        if stack:
            if data[i] < stack[-1][0]:
                result[i] += 1
                stack.append([data[i], 1])
            elif data[i] == stack[-1][0]:
                result[i] += stack[-1][1]
                if len(stack) > 1:
                    result[i] += 1
                stack[-1][1] += 1
        else:
            stack.append([data[i], 1])    
    return sum(result)

print(solution(N, DATA))