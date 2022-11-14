#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("input : ");
    printf("Output : ");
 //   for (int i = 0; i < strlen(s); i++)               That's not efficient we could do better
    for (int i = 0, n = strlen(s); i < n; i++)          // That's called marginal improving
    {
        printf("%c",s[i]);
    }
    printf("\n");
}
