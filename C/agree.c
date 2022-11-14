#include <stdio.h>
#include <stdbool.h>

int main()
{
    char X;
    printf("Do you agree ?\n");
    scanf("%c",&X);
    if (X == 'y' || X == 'Y')
    printf("Agreed !");
    else if(X == 'n' || X == 'N')
    printf("Not agreed !");
    return 0;
}
