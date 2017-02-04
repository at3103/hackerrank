def find_sub_seq(l,n):
	indices = (len(l),len(l))
	min_diff = max(l)
	s = 0
	prev_sum = 0

	for i in range(len(l)):
		prev_sum += l[i]
		s = prev_sum
		for j in range(i+1):
			temp_sum_diff = abs(s - n)
			if temp_sum_diff < min_diff:
				min_diff = temp_sum_diff
				indices = (j,i)
			elif temp_sum_diff == min_diff:
				if indices[0] > j:
					indices = (j,i)
				elif indices[0] == j and indices[1] > i:
				 	indices = (j,i)
			if min_diff == 0:
				return tuple(indices)			
			s-=l[j]
	return indices


print find_sub_seq([3,4,5,6,7],14)