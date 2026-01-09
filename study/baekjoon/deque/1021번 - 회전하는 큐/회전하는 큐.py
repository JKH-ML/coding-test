import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().rstrip().split(' '))
DATA = list(map(int, input().rstrip().split(' ')))

def solution(n, k, data):
    result = 0
    q = deque([x+1 for x in range(n)])
    for del_num in data:
        # k개 지우면서 result += 연산횟수
        # del_num 은 현재 q에서 몇번째 index인지 찾기.
        n = len(q)
        idx = q.index(del_num)
        # 왼쪽이 빠른지 오른쪽이 빠른지 찾기. 빠른길 선택
        result += min(n - idx, idx)
        if idx < n - idx:
            for j in range(idx):
                q.append(q.popleft())
        else:
            for j in range(n - idx):
                q.appendleft(q.pop())
        # popleft.
        q.popleft()
    return result

print(solution(N, K, DATA))
