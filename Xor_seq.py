
import sys

def generate_A(prev,i,s,e):
	ret_ans = prev
	for a in range(long(i)+1,long(e+1)):
		print prev
		prev^=a		
		if a >= s:
			ret_ans^=prev
	return ret_ans,prev,a

# generate_A(0,0,0,20)
# exit()

prev = long(0)
i = long(0)
Q = int(raw_input().strip())
for a0 in xrange(Q):
	L,R = raw_input().strip().split(' ')
	L,R = [long(L),long(R)]
	#if L<=prev:
	if L<4:
		i = 0 #5 - 2 + 1 	
	else:
		i = L - ((L+1)%4) + 1  #5 - 2 + 1 
	b_zero = L + (4 - ((L+1)%4))  # 5 + 4 -2
	ret_ans = 0
	#for j in range(i,L):   # 4^5
	#	ret_ans^=j

	for j in range(i,b_zero):   # (4^5)^6
		ret_ans^=j
	i = R - ((R+1)%4) + 1		# 4 - 1
	#a_zero = R + (4 - ((L+1)%4))  # 5 + 4 -2
	#for j in range(i,L):   # 4^5
	#	ret_ans^=j
	#b_zero = L + (4 - ((L+1)%4))
	no_of_twos = i - b_zero -1
	ret_ans1 = ((no_of_twos%2)*2)
	for j in range(i,R+1):
		ret_ans1^=j

	ret_ans^=ret_ans1
	#prev = 0
	#ret_ans, prev, i = generate_A(0,i,L,R)
	# 	print prev
	# 	print i
	# else:
	# 	ret_ans, prev, i = generate_A(prev,i,L,R)
	print ret_ans