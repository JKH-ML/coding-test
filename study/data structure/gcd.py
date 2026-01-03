# gcd_sub
def gcd_sub(a,b):
    while(a!=0 and b!=0):
        if a > b: 
            a = a - b
        else: 
            b = b - a
    return a + b


# gcd_mod
def gcd_mod(a,b):
    while(a!=0 and b!=0):
        if a > b: 
            a %= b
        else: 
            b %= a
    return a + b

# gcd_rec
def gcd_rec(a,b):
    if a > b: 
            a %= b
    else: 
            b %= a
            
    if a == 0 or b == 0:
        return a+b
    else:
        return gcd_rec(a,b)
   
a, b = 192, 162
print(gcd_sub(a,b), gcd_mod(a,b), gcd_rec(a,b))