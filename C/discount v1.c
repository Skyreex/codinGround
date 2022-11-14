#include <stdio.h>

float discount(float discount1);
int main()
{
    float Regular_Price,discount0,discount2,NewPrice,discounted;
    printf("What's the regular price ? ");
    scanf("%f",&Regular_Price);
    printf("What's the discount ? ");
    scanf("%f",&discount0);
    discount2 = discount(discount0);
    NewPrice = Regular_Price*discount2;
    discounted = Regular_Price - NewPrice;
    printf("The old price is : %.2f $\n",Regular_Price);
    printf("The new price is : %.2f $\n",NewPrice);
    printf("The discounted amount : %.2f $",discounted);
    return 0;
}

float discount(float discount1)
{
    return   1 - discount1/100 ;
}


