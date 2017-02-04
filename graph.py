from collections import defaultdict
# Enter your code here. Read input from STDIN. Print output to STDOUT


class Graph:
	def __init__(self, n, m):
		self.n = n
		self.m = m
		self.cost = defaultdict(list)

	def add_edge(self,a,b,c):
		self.cost[(a,b)].append(c)
		self.cost[(b,a)].append(c)
	
	def display(self):
		for k in self.cost.keys():
			for c in self.cost[k]:
				print "cost for " , k , " is ", c

				
		

n , m = map(int, raw_input().strip().split())
print n,m
G =	Graph(n,m)
for i in range(m):
	a,b,c = map(int, raw_input().strip().split())
	G.add_edge(a,b,c)
a,b = map(int, raw_input().strip().split())

G.display()