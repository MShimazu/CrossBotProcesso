#include <stdio.h>
#include <math.h>

float CalcDist(float[],float[]);

void main(){
    float p1[] = {1,2};
    float p2[] = {5,6};

    printf("%f\n",CalcDist(p1,p2));
}

float CalcDist(float n1[],float n2[]){
    float r = 0;

    r += pow((n1[0]-n2[0]),2);
    r += pow((n1[1]-n2[1]),2);
    
    r = sqrt(r);
    return r;
}