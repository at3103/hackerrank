{ John Watson performs an operation called a right circular rotation on an array of integers, . After performing one right circular rotation operation, the array is transformed from  to .

Watson performs this operation  times. To test Sherlock's ability to identify the current element at a particular position in the rotated array, Watson asks  queries, where each query consists of a single integer, , for which you must print the element at index  in the rotated array (i.e., the value of ).

Input Format

The first line contains  space-separated integers, , , and , respectively. 
The second line contains  space-separated integers, where each integer  describes array element  (where ). 
Each of the  subsequent lines contains a single integer denoting .

Constraints

Output Format

For each query, print the value of the element at index  of the rotated array on a new line.

Sample Input

3 2 3
1 2 3
0
1
2
Sample Output

2
3
1
}

#!/bin/python

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))

k=k%n
temp = a[-k:]

temp += a[:n-k]

for a0 in xrange(q):
    m = int(raw_input().strip())
    print temp[m]

