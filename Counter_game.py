# Enter your code here. Read input from STDIN. Print output to STDOUT

def check_power_two(n):
    return bin(n).count('1') == 1

def find_closest_power(n):
    b = bin(n)[2:]
    b = b[0] + b[1:].replace('1','0')
    return int(b,base=2)

def find_winner(n):
    if n == 1:
        return "Richard"
    c = 0
    while n>1:
        c+=1
        if check_power_two(n):
            n/=n
        else:
            n-=find_closest_power(n)
    print c
    if c%2:
        return "Richard"
    else:
        return "Louise"
        

print find_winner(6)

# T =  int(raw_input().strip())

# for i in range(T):
#     n = int(raw_input().strip())
#     print find_winner(n)
    
#     