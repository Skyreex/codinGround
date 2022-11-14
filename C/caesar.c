#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

bool only_digits(string s);

int main(int argc, string argv[])               // argc = number of command line argument / argv = vector of C strings
{
    if (argc != 2)                              //  No argument or 2 arguments or more
    {
        printf("Usage: ./caesar key\n");
        return 1;                                   // Close the program
    }
    int R = only_digits(argv[1]);
    if (R == 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    int k = atoi(argv[1]);                              // k is the key
    string t = get_string("plaintext:  ");
    printf("ciphertext: ");
    char c;
    int l = strlen(t);
    for (int i = 0; i < l; i++)
    {
        if (isupper(t[i]))                          // Uppercase
        {
            t[i] = t[i] - 65;                       // A = 0 , B = 1 ... / in order to use the formula
            c = (t[i] + k) % 26;                    // The formula
            c = c + 65;                             // A = 65 , B = 66
            printf("%c", c);
        }
        else if (islower(t[i]))                     // Lowercase
        {
            t[i] = t[i] - 97;                       // a = 0 , b = 1 ... / in order to use the formula
            c = (t[i] + k) % 26;                    // The formula
            c = c + 97;                             // a = 97 , b = 98 ...
            printf("%c", c);
        }
        else
        {
            printf("%c", t[i]);                     // exception for space and punctuation
        }
    }
    printf("\n");
    return 0;
}

bool only_digits(string s) // Bool expression checks if the string s is full digits
{
    int R = 0;                                // Initialization of R
    int l = strlen(s);                        // digit count
    for (int i = 0; i < l; i++)
    {
        if (isdigit(s[i]))
        {
            R++;                                // Incerementation
        }
    }
    if (R == l)                         // Full digits
    {
        return true;
    }
    else                                // Not full digits
    {
        return false;
    }
}
