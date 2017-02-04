from collections import defaultdict,deque


def convert_dict(a,n):
	d = defaultdict(deque)
	for i in range(n):
		d[a[i]].append(i)
	return d

def find_element(a,n,m):
	d = convert_dict(a,n)

	for i in d.keys():
		first = d[i].pop()
		if d.get(m-i):
			return first,d[m-i].pop()
		else:
			d[i].appendleft(first)
	return -1


t = int(raw_input().strip())
for a0 in xrange(t):
	m = int(raw_input().strip())
	n = int(raw_input().strip())
	a = map(int, raw_input().strip().split(' '))
	l = find_element(a,n,m)
	if l == -1:
		print "Not Possible"
	else:
		print min(l) + 1, max(l) + 1


