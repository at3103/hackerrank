from collections import deque

def is_matched(expression):
	brac = deque()
	match_brac = {'(':')','{':'}','[':']'}
	for i in expression:
		if i == '(' or i == '{' or i =='[':
			brac.append(i)
		else:
			if brac:
				if match_brac[brac.pop()] != i:
					return False
			else:
				return False
	return brac == deque()


t = int(raw_input().strip())
for a0 in xrange(t):
	expression = raw_input().strip()
	if is_matched(expression) == True:
		print "YES"
	else:
		print "NO"


