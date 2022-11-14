#include <stdio.h>

void meow(void); 

int main()
{
    int n,i;
    printf("How many meow ? ");
    scanf("%d",&n);
    for(i=n ;i>0 ;i--)
    meow();
    
    return 0;
}

void meow(void)
{
    printf("Meow!\n");
}
