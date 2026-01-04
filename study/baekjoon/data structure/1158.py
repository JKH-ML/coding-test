"""
문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 
양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

출력
예제와 같이 요세푸스 순열을 출력한다.

예제 입력 1 
7 3

예제 출력 1 
<3, 6, 2, 7, 5, 1, 4>
"""

import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

def solution(n, k):
    # 아이디어: 순환하면서 cnt == k 이면 popleft
    alive = deque([x+1 for x in range(n)])
    dead = []
    corps = 0
    cnt = 1
    while (corps != n) :
        if cnt == k:
            dead.append(str(alive.popleft()))
            corps += 1
            cnt = 1
        else:
            alive.append(alive.popleft())
            cnt += 1
    return '<' + ', '.join(dead) + '>' # return f"<{', '.join(dead)}>"

print(solution(N, K))




# 로테이트 사용
# import sys
# from collections import deque

# input = sys.stdin.readline
# N, K = map(int, input().split())

# def solution(n, k):
#     alive = deque([x + 1 for x in range(n)])
#     dead = []
    
#     while alive:
#         # k-1번 회전시켜 k번째 사람을 맨 앞으로 이동
#         alive.rotate(-(k - 1))
#         # k번째 사람 제거 및 기록
#         dead.append(str(alive.popleft()))
        
#     return f"<{', '.join(dead)}>"

# print(solution(N, K))



# 인덱스를 계산해서 해결
# def josephus_problem(n, k):
#     answer = []

#     next_index = k-1
#     people = list(range(1, n+1))

#     while people:
#         cur = people.pop(next_index)
#         answer.append(cur)

#         if len(people) != 0:
#             next_index = (next_index + (k-1)) % len(people)

#     print("<", ", ".join(map(str, answer)), ">", sep='')

# n, k = map(int, input().split())
# josephus_problem(n, k)