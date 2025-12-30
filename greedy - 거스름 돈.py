"""
예시문제: 거스름 돈
거스름 돈 n원을 500원, 100원, 50원, 10원짜리 동전으로 거슬러 줄 때
동전의 총 갯수가 최소가 되도록 하는 함수를 작성하고,
함수의 출력으로 각 동전의 갯수의 합을 출력하라.
"""

def solution(n):
    result = []
    coins = [500, 100, 50, 10]
    for coin in coins:
        if n >= coin:
            count = n // coin
            result.append(count)
            n -= coin * count
    if n == 0:
        return int(sum(result))
    else:
        return "error"
    
print(solution(1250))
print(solution(277450))


    