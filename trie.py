from collections import defaultdict

class trie(object):
	"""docstring for trie"""
	def __init__(self, arg):
		super(trie, self).__init__()
		self.value = arg
		self.dict = defaultdict()
		self.words = 0

	def add(self, new_letter):
		new_entry = trie(new_letter)
		new_entry.words += 1
		self.dict[new_letter] = new_entry
		return new_entry
	
	def traverse(self, letter, add):
		ret_node  = self.dict.get(letter)
		self.words += add
		return ret_node

def operations(op, contact, T):
	add = 0
	if op == 'add':
		add = 1
	i = 0
	temp = T
	while temp and i < len(contact):
		prev = temp
		letter = contact[i]
		temp = prev.traverse(letter, add)
		i += 1

	if temp:
		if temp.value == contact[-1]:
			return temp.words
	if add:
		i -= 1
		while i < len(contact):
			letter = contact[i]
			prev = prev.add(letter)
			i += 1

	return 0

T = trie('*')
with open('input.txt','r') as file:
	n = int(file[0].strip())	
	for line in file[1:]:
		op, contact = line.strip().split(' ')
		ret = operations(op, contact, T)
		if op == 'find':
			print ret
'''
n = int(raw_input().strip())
for a0 in xrange(n):
	op, contact = raw_input().strip().split(' ')
	ret = operations(op, contact, T)
	if op == 'find':
		print ret

'''







