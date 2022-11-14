#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct
{
    string name;
    string number;
}
person;

int main(void)
{

    person people[2];

    people[0].name = "Cole";
    people[0].number = "+212-45-4554";

    people[1].name = "Lamar";
    people[1].number = "+212-45-4555";

    for (int i = 0 ; i < 2; i++)
    {
        if (strcmp(people[i].name, "Cole") == 0)
        {
            printf("%s : %s\n",people[i].name,people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}