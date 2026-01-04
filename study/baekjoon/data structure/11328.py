import sys
input = sys.stdin.readline
N = int(input().rstrip())
DATA = []
for _ in range(N):
    DATA.append(list(input().rstrip().split(' ')))

def solution(n, data):
    result = []
    def make_dict(sss):
        d = {}
        for s in sss:
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        return d
    for i in range(n):
        if make_dict(data[i][0]) == make_dict(data[i][1]):
            result.append('Possible')
        else:
            result.append('Impossible')
    
    return '\n'.join(result)

print(solution(N, DATA))