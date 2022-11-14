#include <stdio.h>
#include <cs50.h>

int get_amount(void);
int calculate_200dh (int amount);
int calculate_100dh (int amount);
int calculate_50dh (int amount);
int calculate_20dh (int amount);
int calculate_10dh (int amount);
int calculate_5dh (int amount);
int calculate_2dh (int amount);
int calculate_1dh (int amount);

int main (void)
{
    int amount = get_amount();
    // The amount given by the customer

    int _200dh = calculate_200dh(amount);
    amount = amount - _200dh * 200;
    // Calculate the number of 200DH to give the customer

    int _100dh = calculate_100dh(amount);
    amount = amount - _100dh * 100;
    // Calculate the number of 100DH to give the customer

    int _50dh = calculate_50dh(amount);
    amount = amount - _50dh * 50;
    // Calculate the number of 50DH to give the customer

    int _20dh = calculate_20dh(amount);
    amount = amount - _20dh * 20;
    // Calculate the number of 20DH to give the customer

    int _10dh = calculate_10dh(amount);
    amount = amount - _10dh * 10;
    // Calculate the number of 10DH to give the customer

    int _5dh = calculate_5dh(amount);
    amount = amount - _5dh * 5;
    // Calculate the number of 5DH to give the customer

    int _2dh = calculate_2dh(amount);
    amount = amount - _2dh * 2;
    // Calculate the number of 2DH to give the customer

    int _1dh = calculate_1dh(amount);
    amount = amount - _1dh * 1;
    // Calculate the number of 1DH to give the customer

    int total = _200dh + _100dh + _50dh + _20dh + _10dh + _5dh + _2dh + _1dh;
    // The total

    printf("200DH : %d\n100DH : %d\n50DH : %d\n20DH : %d\n10DH : %d\n5DH : %d\n2DH : %d\n1DH : %d\nTotal : %d\n",_200dh,_100dh,_50dh,_20dh,_10dh,_5dh,_2dh,_1dh,total);
}

int get_amount(void)
{
    int amount;
    do
    {
        amount = get_int("Amount : ");
    }
    while (amount < 0);
    return amount;
}

int calculate_200dh (int amount)
{
    return amount / 200;
}

int calculate_100dh (int amount)
{
    return amount / 100;
}

int calculate_50dh (int amount)
{
    return amount / 50;
}

int calculate_20dh (int amount)
{
    return amount / 20;
}

int calculate_10dh (int amount)
{
    return amount / 10;
}

int calculate_5dh (int amount)
{
    return amount / 5;
}

int calculate_2dh (int amount)
{
    return amount / 2;
}

int calculate_1dh (int amount)
{
    return amount;
}
/*
int calculate_50c (int amount)
{
    return amount / .5;
}

int calculate_20c (int amount)
{
    return amount / .2;
}

int calculate_10c (int amount)
{
    return amount / .1;
}
*/