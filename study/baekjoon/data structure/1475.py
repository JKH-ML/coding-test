import sys, math
input = sys.stdin.readline
S = str(input().rstrip())

def solution(s):
    result = [0 for _ in range(10)]
    for i in s:
        result[int(i)] += 1
    a = max([result[x] for x in range(10) if x!=6 and x!=9])
    b = math.ceil((result[6]+result[9])/2)
    return max(a, b)

print(solution(S))