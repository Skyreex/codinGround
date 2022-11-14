#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void)
{
    int h = get_int("Height : ");
    draw(h);
}

void draw(int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = -1; j < i ; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}