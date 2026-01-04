import sys
input = sys.stdin.readline
S = input().rstrip()
N = int(input().rstrip())
DATA = [input().rstrip() for _ in range(N)]

def solution(s, n, data):
    # 커서로 부터 왼쪽 / 오른쪽에 있는 문자열을 각각 스택으로 관리
    left = list(s)
    right = []
    for command in data: # 'L' 'D' 'B' 'P x'
        # 'L' 이면서 커서 왼쪽에 문자열이 존재하면: 
        if command == 'L' and left: 
            right.append(left.pop())
        # 'D' 이면서 커서 오른쪽에 문자열이 존재하면: 
        elif command == 'D' and right: 
            left.append(right.pop())
        # 'B' 이면서 커서 왼쪽에 문자열이 존재하면: 
        elif command == 'B' and left: 
            left.pop()
        # 'P'로 시작하면:
        elif command[0] == 'P': 
            left.append(command[2])
    return  ''.join(left + right[::-1])

print(solution(S, N, DATA))