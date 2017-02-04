# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_common_sub_seq(a,b):
    retlist = ""
    c=0
    prev = 0
    for i in range(len(a)):
        for j in range(prev,len(b)):
            if a[i] == b[j]:
                retlist+= " " + str(a[i])
                c+=1
                prev = j+1
                break
    return retlist,c

m,n = map(int,raw_input().strip().split())

a = map(int,raw_input().strip().split())
b = map(int,raw_input().strip().split())

f1,l1 = find_common_sub_seq(a,b)
f2,l2 = find_common_sub_seq(b,a)

if l1 >= l2:
    print f1.strip(" ")
else:
    print f2.strip(" ")

            