
def find_index(opt,x):
    start = 0
    end = len(opt) -1 
    while(1):
        mid = (start + end)/2
        if opt[mid] == x:
            break
        if opt[mid] < x and opt[mid+1] > x:
            return mid
        elif opt[mid] > x:
            end = mid -1
        else:
            start = mid +1
    return -1


def find_longest_subseq(a,n):
    opt = []
    if a.count(s[0]) == n:
        return 1
    for i in range(0,n):
        if not opt:
            opt.append(a[i])
        if a[i] > opt[-1]:
            opt.append(a[i])
        elif a[i] < opt[0]:
            opt[0] = a[i]
        else:
            ind = find_index(opt,a[i])
            if ind != -1:
                opt[ind+1] = a[i]
    return len(opt)



# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
s=[]
opt=[]
for i in range(n):
    s.append(int(raw_input().strip()))

print find_longest_subseq(s,n)



# s = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# print find_longest_subseq(s,16)
# s = [2,7,4,3,8]
# print find_longest_subseq(s,5)


