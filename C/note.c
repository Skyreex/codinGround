#include <stdio.h>

int main()
{
    int i;
    float T[6] ,S,avg;
    for(i=0;i<6;i++){
        printf("Module %d :",i+1);
        scanf("%f",&T[i]);
    }
    S=0;
    for(i=0;i<6;i++){
        S= S + T[i];
        
    }
    avg=S/6;
    printf("la moyenne est %.2f",avg);
    return 0;
}
