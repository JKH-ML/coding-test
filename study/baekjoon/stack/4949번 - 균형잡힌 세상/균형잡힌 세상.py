import sys
input = sys.stdin.readline

def solution(s):
    stack = []
    for i in s:
        if i =='(' or i =='[':
            stack.append(i)
        if i == ')': 
            if not stack or stack[-1]=='[':
                return 'no'
            stack.pop()
        if i == ']': 
            if not stack or stack[-1]=='(':
                return 'no'
            stack.pop()
    
    if stack: return 'no'
    else: return 'yes'

while True:
    s = list(input().rstrip())
    if s == ['.']: break
    else: print(solution(s))

