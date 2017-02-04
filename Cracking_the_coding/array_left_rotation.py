from collections import deque

def array_left_rotation(a, n, k):
	a = deque(a)
	k %= n
	for i in range(k):
		temp = a.popleft()
		a.append(temp)
	return list(a)
			

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))