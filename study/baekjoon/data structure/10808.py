import sys
input = sys.stdin.readline
S = input().rstrip()

def solution(s):
    ascii_dict = {i: 0 for i in range(ord('a'), ord('z') + 1)}
    for i in s:
        ascii_dict[ord(i)] += 1
    return ' '.join([str(x) for x in ascii_dict.values()])

print(solution(S))