#include <stdio.h>

float converte_temperatura(float);

void main(){
    printf("%f\n",converte_temperatura(77.2));
}

float converte_temperatura(float f){
    float r = 0;

    r=(f-32)*(5.0/9.0);

    return r;
}