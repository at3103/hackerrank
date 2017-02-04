# Complete the function below.

def check_palindrome(s):
	return list(s) == list(reversed(s))

def  count_palindromes( S):
    #c = len(S)
    c=0
    
    for i in range(len(S)):
        for j in range(i,len(S)):
            if check_palindrome(S[i:j+1]):   
                c+=1
    
    return c
    
    


