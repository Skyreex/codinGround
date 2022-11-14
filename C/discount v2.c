#include <stdio.h>

float discount(float price , float discount0);
int main()
{
    float Regular_Price,Discount;
    printf("What's the regular price ? ");
    scanf("%f",&Regular_Price);
    printf("What's the discount ? ");
    scanf("%f",&Discount);
    float NewPrice = discount(Regular_Price,Discount);
    float discounted = Regular_Price - NewPrice;
    printf("The old price is : %.2f $\n",Regular_Price);
    printf("The new price is : %.2f $\n",NewPrice);
    printf("The discounted amount : %.2f $",discounted);
    return 0;
}

float discount(float price , float discount0)
{
    return   price * (1 - discount0/100);
}


