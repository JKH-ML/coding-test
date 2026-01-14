A, B, C = map(int, input().split())

# O(N) 은 시간초과 -> O(logN) 으로 구현하려면 B를 2로 나눠가며 해결
# B를 2로 나누기 위해 B가 홀수, 짝수인 경우를 관찰
def sol(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a % c

    if b % 2 == 0:
        return sol_even(a, b, c)
    else:
        return sol_odd(a, b, c)

def sol_even(a, b, c):
    half = sol(a, b // 2, c)
    return (half * half) % c

def sol_odd(a, b, c):
    return (sol(a, b - 1, c) * a) % c

print(sol(A, B, C))
