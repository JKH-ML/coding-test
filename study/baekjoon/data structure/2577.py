import sys
input = sys.stdin.readline
data = []
for _ in range(3):
    data.append(int(input()))

def solution(d):
    result = [0 for _ in range(10)]
    n = str(d[0]*d[1]*d[2])
    for i in n:
        result[int(i)] += 1
    return '\n'.join([str(x) for x in result])

print(solution(data))