from collections import defaultdict,deque
import copy

def find_friends(a):
	retset = set()
	for i in range(len(a)):
		if a[i] == 'Y':
			retset.add(i)
	return retset

def find_friend_circle(friend_dict, friends):
	
	#friends = copy.deepcopy(friend_dict.keys())
	visited = defaultdict()
	to_remove = set()
	current_friend_queue = deque()
	number_of_circles = 0
	
	while friends:
		number_of_circles += 1
		current_friend_queue.append(friends[0])
		to_remove.add(friends[0])
		while current_friend_queue:
			temp = current_friend_queue.popleft()
			if visited.get(temp):
				continue
			visited[temp] = 1
			current_friend_queue.extend(friend_dict[temp])
			to_remove.update(friend_dict[temp])
		friends = list(set(friends) - to_remove)

	return number_of_circles



# Enter your code here. Read input from STDIN. Print output to STDOUT

friend_dict = defaultdict(set)
n = int(raw_input().strip())

for i in range(n):
	row = raw_input().strip()
	friend_dict[i].update(find_friends(row))
print find_friend_circle(friend_dict, friend_dict.keys())