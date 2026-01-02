"""
문제
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. 
AAAA와 BB

이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 
민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 
이때, '.'는 폴리오미노로 덮으면 안 된다.

폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 보드판이 주어진다. 
보드판의 크기는 최대 50이다.

출력
첫째 줄에 사전순으로 가장 앞서는 답을 출력한다. 
만약 덮을 수 없으면 -1을 출력한다.

예제 입력 1 
XXXXXX
예제 출력 1 
AAAABB
예제 입력 2 
XX.XX
예제 출력 2 
BB.BB
예제 입력 3 
XXXX....XXX.....XX
예제 출력 3 
-1
예제 입력 4 
X
예제 출력 4 
-1
예제 입력 5 
XX.XXXXXXXXXX..XXXXXXXX...XXXXXX
예제 출력 5 
BB.AAAAAAAABB..AAAAAAAA...AAAABB
"""

def sol(s):
    # 아이디어
    # s -> words(문자인지 점인지)
    # -> 갯수세기L, BB AAAA로 커버
    # -> result 로 합쳐서 return
    
    buffer = ''
    dot = 0
    words = []
    for i in s:
        if i=='.':
            dot += 1
            if buffer:
                words.append(buffer)
                buffer = ''
        else:
            if dot > 0:
                words.append('.' * dot)
                dot = 0
            buffer += i
    if buffer:
        words.append(buffer)
        buffer = ''
    if dot > 0:
        words.append('.' * dot)
        dot = 0
        
    result = ''
    for word in words:
        if word.startswith('X'):
            L = len(word)
            if L % 2 == 1:
                return -1
            k = L // 4 
            r = L % 4 # r = 0 or 2
            word = 'AAAA' * k +'BB' * (r//2)
            result += word
        else:
            result += word
    return result
    
a = input()
print(sol(a))

# 배운 것
# s = 'XX.XXXXXXXXXX..XXXXXXXX...XXXXXX'
# parts = s.split('.')
# print(parts)
# parts = '.'.join(parts)
# print(parts)
# print(s)

# 간단한 솔루션
# import sys

# # 입력 받기
# board = sys.stdin.readline().rstrip()

# board = board.replace('XXXX', 'AAAA')

# board = board.replace('XX', 'BB')

# if 'X' in board:
#     print(-1)
# else:
#     print(board)