def recursive_fcn(i):
	if i == 10:
		return
	print(i, '-th fcn calls', i+1, '-th fcn.')
	recursive_fcn(i+1)
	print(i, '-th fcn terminated.')

# recursive_fcn(1)


def factorial(n):
	if n<=1:
		return 1
	return n * factorial(n-1)

# print(factorial(5))

def recursive_GCD(a, b):
	if a%b == 0:
		return b
	else:
		return recursive_GCD(b, a%b)

print(recursive_GCD(192, 162))
print(recursive_GCD(162, 192))