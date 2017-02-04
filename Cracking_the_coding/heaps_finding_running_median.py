#!/bin/python

import sys

def find_pos(a,x):
	start = 0
	l = len(a) - 1
	end = l

	while start <= end:
		mid = (start + end)/2
		if a[mid] == x:
			return mid + 1
		elif a[mid] < x and a[mid+1] > x:
			return mid + 1
		elif a[mid] > x and a[mid-1] <= x:
			return mid
		elif a[mid] < x:
			start = mid + 1
		else:
			end = mid - 1
	return -1

def find_median(a,n):
	pos = n/2
	if n%2:
		return float(a[pos])
	else:
		return float(float(a[pos] + a[pos-1])/2.0)


n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
	a_t = int(raw_input().strip())
	a.append(a_t)
	if a_i > 0 and a[-1] < a[-2]:
		pos = find_pos(a,a_t)
		temp = a.pop()
		a.insert(pos,temp)
	print "{:.1f}".format(find_median(a,a_i+1))

