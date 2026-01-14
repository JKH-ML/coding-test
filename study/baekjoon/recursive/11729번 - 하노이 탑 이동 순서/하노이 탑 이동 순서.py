n = int(input())
print(2**n - 1)
def f(n, start, end):
    if n == 1:
        print(f'{start} {end}')
        return
    else:
        middle = 6 - start - end
        f(n-1, start, middle)
        f(1, start, end)
        f(n-1, middle, end)
        return  
    
f(n, 1, 3)

