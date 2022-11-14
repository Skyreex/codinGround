#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Height :");
    }
    while (h < 1 || h > 8);                 // Height Conditions

    for (int i = 0; i < h; i++)             // Nomber Of Row
    {
        for (int d = h - 1; d > i; d--)     // Spaces
        {
            printf(" ");
        }
        for (int j = -1; j < i; j++)        // left Hashes
        {
            printf("#");
        }
        printf("  ");                       // Double space
        for (int l = -1; l < i; l++)        // left Hashes
        {
            printf("#");
        }
        printf("\n");
    }
}