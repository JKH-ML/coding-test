import sys
input = sys.stdin.readline
S = [x for x in input().rstrip()]

def solution(s):
    result = 0
    stack = ['(']
    for i in range(1, len(s)):
        if s[i]=='(':
            stack.append(s[i])
        elif s[i-1]=='(' and s[i]==')': # 레이저 발사
            stack.pop()
            result += len(stack)
        elif s[i-1]==')' and s[i]==')': # 막대기의 끝
            stack.pop()
            result += 1
    return result

print(solution(S))