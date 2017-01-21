#!/bin/python

# Complete the function below.


def  maxXor( l,  r):
    maxxor = 0
    for i in range(l,r+1):
        for j in range(i,r+1):
            tempxor = i ^ j
            if tempxor > maxxor:
                maxxor = tempxor
    return maxxor

            

    

_l = int(raw_input());


_r = int(raw_input());

res = maxXor(_l, _r);
print(res)


