#include <cs50.h>
#include <stdio.h>


int main(void)
{
    int h;
    do
    {
        h = get_int("Height :");
    }
    while (h < 1 || h > 8);  //Height condition

    for (int i = 0; i < h; i++)   //nomber of row
    {
        for (int d = h - 1; d > i; d--)   //nomber of spaces
        {
            printf(" ");
        }
        for (int j = -1; j < i; j++)      //nomber of hashes and column
        {
            printf("#");
        }
        printf("\n");
    }
}