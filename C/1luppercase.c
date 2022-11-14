#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("name : ");
    printf("Name : ");
    if(s[0] >= 'a' && s[0] <= 'z')
    {
    printf("%c", s[0] - 32);
    }
    else
    {
    printf("%c",s[0]);
    }
    for (int i = 1, n = strlen(s); i < n; i++)
    printf("%c",s[i]);
    printf("\n");
}
/* ASCII
a-z --- 97 - 122
A-Z --- 65 - 90

 32 between a and A
*/