#include <stdio.h>
#include <stdlib.h>

int main()
{
    // var
    char name[100];
    int age;
    // i/o
    // name
    puts("What's your name ?");
    scanf("%s", name);
    printf("Hi ,%s!\n", name);
    // age

age:
    puts("How old are you ?");
    scanf("%i", &age);
    if (age >= 0)
        switch (age)
        {
        case 0:
            printf("How much warmth is there?");
            break;
        case 1 ... 3:
            printf("How did u even type");
            break;
        case 4 ... 10:
            printf("You're so young");
            break;
        case 11 ... 17:
            printf("You're a bit teenager");
            break;
        case 18:
            printf("You seem pretty LEGAL");
            break;
        case 19 ... 29:
            printf("How does it feel like to be mature");
            break;
        case 30 ... 49:
            printf("Damn bro you're getting old");
            break;
        case 50 ... 69:
            printf("Damn bro you're so old");
            break;
        case 70 ... 99:
            printf("Damn bro you're SO SO SO OLD");
            break;
        case 100:
            printf("Badr Bennoun");
            break;
        case 666:
            printf("a3odo billah");
            break;
        case 777:
            printf("SEVEN SEVEN SEVEN");
            break;
        default:
            printf("Are u even alive? LOL");
        }
    else
    {
        printf("Error\n");
        goto age;
    }
    return 0;
}
