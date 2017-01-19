# Enter your code here. Read input from STDIN. Print output to STDOUT



    int n,i,j,c=0,prev=0,sq,f;
    R =[]

    n = int(raw_input().strip())
    
    for x in xrange(1,n+1):
        R += int(raw_input().strip())

    prev = 

    


    sq=1;
    f=1;
    if(n>0)
    {
        prev=1;
        c=1;
    }
    for(i=1;i<n;i++)
        {
            if(a[i]>a[i-1])
                {
                    c+=prev+1;
                    prev++;
                    sq++;
            }
            else if(a[i]==a[i-1])
                {
                    c+=1;
                    prev=1;
                    f=0;
                    sq=1;
            }
            else if(a[i]<a[i-1])
                {
                    if(prev==1 && f==0)
                        {
                            c+=1;
                            
                    }
                    
                    else if(prev==1 && f==1)
                        {
                            c+=1 + sq;
                            sq++;
                    }
                    else sq = 0;
                    prev=1;
                    c+=1;
                    f=1;
            }
    }
    cout<<c;
    return 0;
}


