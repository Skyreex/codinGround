#include <stdio.h>
#include <math.h>
int main(void)
{
    int pennies;
    float amount;
    printf("amount in $ : ");
    scanf("%f",&amount);
    pennies = round(amount * 100); //why round() Cuuuuuz 4.20 ->419 pennies
    printf("%d pennies",pennies);
    
    
}