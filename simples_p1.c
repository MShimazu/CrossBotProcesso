#include <stdio.h>

void main(){

    float lista[10];
    int x,y;

    printf("digitar 10 numeros\n");
    for (int i = 0; i < 10; i++)
    {
        scanf("%f",&lista[i]);
    }
    
    printf("digite x:");
    scanf("%d",&x);
    printf("digite y:");
    scanf("%d",&y);

    printf("Soma = %f\n",(lista[x]+lista[y]));
}
