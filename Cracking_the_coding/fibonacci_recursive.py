from collections import defaultdict

fib = defaultdict()
fib[0] = 0
fib[1] = 1

def fibonacci(n):
	global fib
	if not fib.get(n):
		fib[n] = fibonacci(n-1) + fibonacci(n-2) 
		#return fib[n]
	#else:
		
	return fib[n]
	
#n = int(raw_input())
n = 3
print(fibonacci(n))

