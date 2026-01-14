import sys
input = sys.stdin.readline

def solution(n, data):
    visited = [False] * (n + 1)
    onStack = [False] * (n + 1)
    order = [0] * (n + 1)
    included = [False] * (n + 1)

    for i in range(1, n + 1):
        if visited[i]:
            continue

        cur = i
        depth = 0

        while True:
            visited[cur] = True
            onStack[cur] = True
            order[cur] = depth
            depth += 1

            nxt = data[cur]

            if not visited[nxt]:
                cur = nxt
                continue

            if onStack[nxt]:
                # 사이클: nxt부터 다시 nxt로 돌아올 때까지
                node = nxt
                while True:
                    included[node] = True
                    node = data[node]
                    if node == nxt:
                        break
                break

            break

        # onStack 정리
        cur = i
        while onStack[cur]:
            onStack[cur] = False
            cur = data[cur]

    return sum(1 for i in range(1, n + 1) if not included[i])


T = int(input())
for _ in range(T):
    N = int(input())
    DATA = [0] + list(map(int, input().split()))
    print(solution(N, DATA))
