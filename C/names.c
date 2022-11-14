#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string names[] = {"Akram", "Bill", "Harry", "Mark", "Charle", "Jermain", "Kendrick"};
    for (int i = 0 ; i < 7; i++)
    {
        if (!(strcmp(names[i],"Akram"))) // (strcmp(names[i],"Akram") == 0 meaning false // !(0)=> 1
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}