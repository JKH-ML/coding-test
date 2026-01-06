import sys
input = sys.stdin.readline

def solution(data):  
    n, stack, max_area, heights = data[0], [], 0, data[1:]
    heights.append(0)
    for i in range(n + 1):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area

while True:
    data = list(map(int, input().split()))
    if data[0] == 0: break
    print(solution(data))