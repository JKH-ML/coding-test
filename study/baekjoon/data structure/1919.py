import sys
input = sys.stdin.readline
N = input().rstrip()
M = input().rstrip()

def solution(n, m):
    def make_dict(sss):
        d = {}
        for s in sss:
            d[s] = d.get(s, 0) + 1
        return d
    nd = make_dict(n)
    md = make_dict(m)
    for s in md:
        nd[s] = abs(nd.get(s, 0) - md[s])
    return sum(nd.values())
print(solution(N, M))