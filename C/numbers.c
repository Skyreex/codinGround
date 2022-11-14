#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int numbers[] = {1, 3, 4, 7, 6, 9, 0};
    for (int i = 0; i < 7; i++)
    {
        if (numbers[i] == 0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}