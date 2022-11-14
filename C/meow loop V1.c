#include <stdio.h>
#include <stdbool.h>

int main()
{
    // While loop
    int i,n;
    printf("How many meow ? ");
    scanf("%d",&n);
    i=0;
    while(n>i){
    printf("Meow!\n");
    i++;
    }
    return 0;
}
/*
{
    // For loop
    int i,n;
    printf("How many meow ? ");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    printf("Meow!\n");
    return 0;
}
*/