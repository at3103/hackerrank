#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int find_longest_sub(int s[], int n)
{   
    int max_len = 1;
    int max_s = s[0];
    int opt[n];
    opt[0]=1;
    int c = 1;

    for(int i = 1; i <n; i++)
    {
        c = 1;
        //if (s[i] <= max_s)
        //    continue;
        //max_s = s[i];
        for(int j = i-1;j>=0;j--)
        {
            if(j+1 < c)
                break;
            if (s[j] < s[i])
                if (opt[j] + 1 > c)
                    c = opt[j] + 1;    
        }
        opt[i] = c;
        if (c > max_len)
            max_len = c;
    }
    return max_len;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin>>n;
    int a[n];
    
    for(int i = 0; i <n; i++)
    {
     cin>>a[i];   
    }
    cout<<find_longest_sub(a,n);
    return 0;
}


