import sys
input = sys.stdin.readline

N1 = int(input())
D1 = list(map(int, input().split()))
N2 = int(input())
D2 = list(map(int, input().split()))

def solution(n1, n2, d1, d2):
    # 크레인과 박스를 무게 기준 내림차순 정렬
    d1.sort(reverse=True) # 크레인
    d2.sort(reverse=True) # 박스

    # 가장 무거운 박스를 가장 강한 크레인이 못 들면 불가능
    if d2[0] > d1[0]:
        return -1

    visited = [False] * n2     # 각 박스가 옮겨졌는지 여부
    pos = [0] * n1             # 각 크레인이 현재 보고 있는 박스 인덱스
    moved = 0                  # 지금까지 옮긴 박스 개수
    time = 0                   # 걸린 시간(분)

    # 아직 옮기지 않은 박스가 남아 있는 동안 반복
    while moved < n2:
        # 1분 동안 모든 크레인이 각각 한 번씩 시도
        for i in range(n1):
            # i번째 크레인이 들 수 있는 박스를 찾을 때까지 이동
            while pos[i] < n2:
                # 아직 옮기지 않은 박스이고, 크레인이 들 수 있으면
                if not visited[pos[i]] and d1[i] >= d2[pos[i]]:
                    visited[pos[i]] = True   # 박스를 옮겼다고 표시
                    moved += 1              # 옮긴 박스 수 증가
                    pos[i] += 1             # 다음 박스부터 탐색
                    break                   # 이 크레인은 이번 분에 작업 완료
                # 현재 박스를 못 들면 다음 박스로 이동
                pos[i] += 1
        # 1분이 지났으므로 시간 증가
        time += 1

    return time

print(solution(N1, N2, D1, D2))
