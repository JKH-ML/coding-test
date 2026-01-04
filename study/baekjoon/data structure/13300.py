import sys, math
input = sys.stdin.readline
N, K = map(int, input().rstrip().split(' '))
data = []
for _ in range(N):
    data.append(input().rstrip())

def solution(n, k, data):
    result = { }
    room = 0
    for i in range(n):
        if data[i] in result:
            result[data[i]] += 1
        else:
            result[data[i]] = 1
    for i in result:
        room += math.ceil(result[i] / k)
    return room

print(solution(N, K, data))