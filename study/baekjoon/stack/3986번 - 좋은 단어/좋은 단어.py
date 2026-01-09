import sys
input = sys.stdin.readline

N = int(input().rstrip())
DATA = [input().rstrip() for _ in range(N)]

def solution(n, data):
    result = [1] * n
    for i in range(n):
        
        # 홀짝 체크도 O(n)이라 굳이 안해도 될 듯.
        # nA = data[i].count('A')
        # nB = data[i].count('B')

        # # 홀수면 바로 실패
        # if nA % 2 == 1 or nB % 2 == 1:
        #     result[i] = 0
        #     continue

        stack = []
        for s in data[i]:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)

        if stack:
            result[i] = 0

    return sum(result)

print(solution(N, DATA))
