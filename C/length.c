#include <stdio.h>
#include <cs50.h>

int string_length(string s);

int main(void)
{
    string name = get_string("Name : ");
    int length = string_length(name);      // string_length fct gets name which mean s == name and it returns i as length
    printf("%i\n", length);


}

int string_length(string s)
{
    int i = 0;
    while (s [i] != 0)      // This while loop can tell us the length of the string
    i++;
    return i;                               // it returns i
}