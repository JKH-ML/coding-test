import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = [int(x) for x in list(input().rstrip().split(' '))]
X = int(input().rstrip())

def solution(n, data, x):
    result = 0
    checked = {} # 확인한 숫자와 그 숫자가 나온 횟수를 저장
    for i in range(n):
        if x - data[i] in checked:
            result += checked[x - data[i]]
        if not data[i] in checked:
            checked[data[i]] = 0
        checked[data[i]] += 1
    return result

print(solution(N, DATA, X))

# Gemini 
# import sys

# def solution(n, data, x):
#     result = 0
#     checked = {}
    
#     for val in data:
#         target = x - val
#         # 짝이 존재한다면 그 개수만큼 결과에 더함
#         if target in checked:
#             result += checked[target]
            
#         # 현재 숫자의 등장 횟수를 갱신 (초기값 0 처리 포함)
#         checked[val] = checked.get(val, 0) + 1
        
#     return result

# # 입력 처리 부분
# input = sys.stdin.readline
# N = int(input())
# DATA = list(map(int, input().split())) # map을 쓰면 더 깔끔합니다.
# X = int(input())

# print(solution(N, DATA, X))