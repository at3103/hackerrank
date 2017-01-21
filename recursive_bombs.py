def check(max_it, min_it):
	ret = 0
	rem1 = (max_it+1)%min_it
	rem2 = (max_it-1)%min_it
	if rem2 == 0:
		ret = min_it - 1 + ((max_it-1)/min_it)
	elif rem1 == 0:
		ret = min_it - 2 + ((max_it+1)/min_it)
	return ret

def answer(M, F):
	# your code here
	m = int(M)
	f = int(F)
	ret = 0
	max_it = max(m,f)
	min_it = min(m,f)
	diff = max_it - min_it
	if m == 0 or f == 0:
		return str("impossible")
	if m + f == 2:
		return str(0)
	if diff == 0:
		ret = 0
	elif diff >= min_it:
		ret = check(max_it,min_it)
		if ret == 0:
			min_it,diff = diff,min_it
		else:
			return str(ret)
	if diff < min_it:
		ct = 0
		while diff < min_it:
			max_it-=min_it
			if max_it < min_it:
				max_it,min_it = min_it,max_it
			ct+=1
			diff = max_it - min_it

		ret = check(max_it,min_it)
		if ret != 0:
			ret+=ct
	
	if ret == 0:
		return str("impossible")
	else:
		return str(ret)

	
#ret = check(min_it,max_it-min_it)
print answer(30,43)
c = answer(2,3)
print answer(13,7)
print c