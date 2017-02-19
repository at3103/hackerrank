"""
Given N integers, count the number of pairs of integers whose difference is .

Input Format

The first line contains N and K.
The second line contains N  numbers of the set. All the N numbers are unique.


Each integer will be greater than  and at least  smaller than .
Output Format

An integer that tells the number of pairs of integers whose difference is .
"""
from collections import Counter
#!/usr/bin/py
# Head ends here
def pairs(a,k):
    """
    a contains array of numbers and k is the value of difference
    """
    answer = 0
    given_input_dictionary = Counter(a)
    for number in a:
        if given_input_dictionary.get(number - k):
            answer += 1
    return answer
# Tail starts here
if __name__ == '__main__':
    a = map(int, raw_input().strip().split(" "))
    _a_size = a[0]
    _k = a[1]
    b = map(int, raw_input().strip().split(" "))
    print pairs(b, _k)
