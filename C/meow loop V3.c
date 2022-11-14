#include <stdio.h>

void meow(int n); 

int main()
{
    printf("How many meow ? ");
    meow(69);
    return 0;
}

void meow(int n)
{
    int i;
    scanf("%d",&n);
    for(i=0 ;i<n ;i++)
    printf("Meow!\n");
}
