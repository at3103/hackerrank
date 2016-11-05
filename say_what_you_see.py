# Complete the function below.

#Print how you would say these numbers. For ex: 123 --> We say it as one 1 one 2 one 3, hence, the output for that would be 111213.
#Another example 11111111 --> eight ones --> 81

def  say_what_you_see( input_strings):
    c = 1
    prev = -1
    olist = []
    ilist = ''
    
    for number in input_strings:
        c = 1
        ilist = ''
        print "number is " + number
        for j in xrange(len(number)):
            s = number[j]
            print s,j
            i = int(s)
            if j == 0:
                prev = int(number[j])
                c = 1
            elif i == prev:
                c += 1
                #if j == len(number) - 1:
                 #   ilist += str(c)
                  #  ilist += str(i)
            else:
                if j == len(number) - 1:
                    ilist += str(c)
                    ilist += str(prev)
                prev = i
                ilist += str(c)
                ilist += str(prev)
                c = 1
                continue
            if j == len(number) - 1:
                ilist += str(c)
                ilist += str(prev)
        olist.append(ilist)
        
    return olist
            

print say_what_you_see(['12','21'])