#include <cs50.h>
#include <stdio.h>

long cc_num(void);
long cc_validation1(long number);
long cc_validation2(int A6, long number);

int main(void)
{
    long number = cc_num();
    int A6 = cc_validation1(number);
    cc_validation2(A6, number);
}


long cc_num(void)
{
    long num;
    do
    {
        num = get_long("Number : ");                    // Get the card number
    }
    while (num > 57e16);                                // Condition for the card
    return num;
}

long cc_validation1(long number)
{
    int A1, A2, A3, A4, A5;
    A2 = 0;
    A4 = 0;
    long i, j;
    for (i = 100; i < 1E18; i = i * 100)  // Starting with the number’s second-to-last digit,
    {
        A1 = number % i / (i / 10);
        A1 = A1 * 2;                      // Multiply every other digit by 2,
        if (A1 > 8)
        {
            A1 = A1 % 10 + 1;
        }
        A2 = A1 + A2;
    }
    for (j = 10; j < 1E18; j = j * 100)
    {
        A3 = number % j / (j / 10);
        A4 = A3 + A4;                       // The sum of the digits that weren’t multiplied by 2
    }
    A5 = A4 + A2;                           // The sum of all parts
    return A5;
}
long cc_validation2(int A6, long number)
{
    A6 = A6 % 10;
    if (A6 == 0)                                // Meaning the last digit is 0
    {                            
        if (number > 3999999999999999 && number < 5000000000000000)       // VISA
        {
            printf("VISA\n");
        }
        else if (number > 3999999999999 && number < 50000000000000)       // VISA
        {
            printf("VISA\n");
        }
        else if (number > 5099999999999999 && number < 5600000000000000)  // MASTERCARD
        {
            printf("MASTERCARD\n");
        }
        else if (number > 369999999999999 && number < 380000000000000)    // AMEX
        {
            printf("AMEX\n");
        }
        else if (number > 339999999999999 && number < 350000000000000)    // AMEX
        {
            printf("AMEX\n");
        }
        else
        {
            printf("INVALID\n");                                          // INVALID
        }
    }
    else
    {
        printf("INVALID\n");                                             // INVALID
    }
    return 1;
}