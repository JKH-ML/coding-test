import sys
input = sys.stdin.readline
S = [x for x in input().rstrip()]


# 관찰 결과 = 이전 등장한 괄호가 중요하다. -> 케이스 분류 4x4 가지.

# ( ( / [ [ -> 가능. 임시값 val 에 *=
# ( [ / [ ( -> 가능. 임시값 val 에 *=

# ( ) / [ ] -> 가능. 임시값이 완성되면서 더해지는 항이 된다. result에 +=

# ( ] / [ ) -> 불가능. 이 케이스를 예외처리하기 위해 stack이 필요.
# 여는 괄호는 stack.append, 닫는 괄호는 stack.pop

# ) ) / ] ] / ) ] / ] ) -> 가능. just pop - pop
# ) ( / ) [ / ] ( / ] [ -> 가능. just pop - pop

# 예외처리
# 1. 괄호가 홀수개 인 경우 : 없어도 되는데 있으면 일부 경우에 성능이 좋을수도.
# 2. ) / ] : stack이 비었는데 pop 하는경우
# 3. s 순회가 끝났는데 stack 에 내용물이 있는 경우
# 4. ( ] / [ ) : pop 하려고 보니까 stack[-1] 과 짝이 안 맞는 경우.

def solution(s):
    n = len(s)
    stack = []
    answer = 0
    val = 1 
    # val은 임시값. 2 또는 3이 곱해지다가 닫는 괄호가 나오면 result에 더해진다.
    # 더해지고 나면 닫는 괄호 pop 하고, 2 또는 3으로 다시 나눠진다.
    
    # 예외처리1
    if n % 2 == 1: return 0
        
    for i in range(n):
        
        if s[i] == "(":
            # 여는 괄호
            stack.append("(")
            val *= 2
            
        elif s[i] == "[":
            # 여는 괄호
            stack.append("[")
            val *= 3
            
        elif s[i] == ")":
            
            # 예외처리 2,4
            if not stack or stack[-1] == "[":
                return 0
            
            if s[i-1] == "(":
                answer += val
            
            # 닫는 괄호
            stack.pop()
            val //= 2
            
        elif s[i] == "]":
            
            # 예외처리 2,4
            if not stack or stack[-1] == "(":
                return 0
            
            if s[i-1] == "[":
                answer += val
                
            # 닫는 괄호
            stack.pop()
            val //= 3

    # 예외처리 3
    if stack: return 0
    else: return answer

print(solution(S))