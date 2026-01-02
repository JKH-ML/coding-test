import sys
input = sys.stdin.readline
N, K = map(int, input().split())
data = []
for _ in range(N):
    data.append(int(input()))

def solution(n, k, array):
    # 아이디어: 화폐가 비싼 순서대로 남은돈을 나눠서 몫은 result, 나머지를 다음 
    # 화폐로 넘긴다. 남은 돈이 0이면 즉시 종료하고 return result
    # 알고리즘: 그리디
    # 자료구조: 리스트
    # 시간복잡도: O(N)
    result = 0
    array.reverse()
    for i in range(n):
        if k == 0:
            return result
        result += k // array[i]
        k = k % array[i]
    return result

print(solution(N, K, data))
