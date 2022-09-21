#include <stdio.h>

int VerificaNum(int);

void main(){
    printf("%d\n",VerificaNum(6));
}

int VerificaNum(int n){
    int r=0,s=0;

    for (int i = 1; i < n; i++)
    {
        if (n%i == 0)
        {
            s+=i;
        }
        
    }

    r = (s==n);
    
    return r;
}
