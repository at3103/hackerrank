
def find_longest_subseq(s,n,opt):
    #opt=[]
    #opt.append(1)
    max_len = 1
    for i in range(1,n):
        c = 1
        for j in range(i-1,-1,-1):
            if j+1 < c:
                break
            temp = opt[j]
            if s[j] < s[i]:
                if temp + 1 > c:
                    c = temp + 1
        opt[i] = c
        if c > max_len:
            max_len = c
    
    return max_len


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input().strip())
s=[]
opt=[]
for i in range(n):
    s.append(int(raw_input().strip()))
    opt.append(1)

print find_longest_subseq(s,n,opt)

