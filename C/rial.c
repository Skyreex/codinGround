#include <stdio.h>
#include <math.h>
int main(void)
{
    int Rial;
    float amount;
    printf("amount in DH : ");
    scanf("%f",&amount);
    Rial = round(amount * 20);
    printf("%d Riyal",Rial);
    
    
}