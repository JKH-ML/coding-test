# import sys
# input = sys.stdin.readline
# N = int(input().rstrip())
# DATA = [int(x) for x in input().rstrip().split(' ')]

# def solution(n, data):
#     # 탑의 인덱스를 혼동하지 않기 위해 0부터 n-1을 사용함.
#     result = [-1 for _ in range(n)]
#     stack = []
#     stack.append([data[0],0])
#     for i in range(1, n):
#         if stack[-1][0] > data[i]:
#             result[i] = i-1
#             stack.append([data[i],i])
#         else: # stack[-1] < data[i]
#             while stack[-1][0] < data[i]:
#                 stack.pop()
#                 if not stack:
#                     result[i] = -1
#                     break
#                 else:
#                     result[i] = stack[-1][1]
#             stack.append([data[i],i])
#     return ' '.join([str(x+1) for x in result])

# print(solution(N, DATA))


import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [int(x) for x in input().rstrip().split(' ')]

def solution(n, data):
    result = [-1 for _ in range(n)]
    stack = []
    stack.append([data[0], 0])
    for i in range(1, n):
        while stack and stack[-1][0] < data[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1][1]
        else:
            result[i] = -1
        stack.append([data[i], i])
    return ' '.join([str(x + 1) for x in result])

print(solution(N, DATA))