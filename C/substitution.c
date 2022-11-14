#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int validate_key(string k);

int main(int argc, string argv[])
{
    if (argc != 2)                              // 2nd argument
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    int A = validate_key(argv[1]);
    if (A != 0)
    {
        return 1;
    }
    else if (A == 0)
    {
        string k = argv[1];
        string t = get_string("plaintext: ");
        printf("ciphertext: ");
        char c;
        int l = strlen(t);
        for (int i = 0; i < l; i++)
        {
            if (isupper(t[i]))
            {
                for (int j = 65; j < 91; j++)
                {
                    if (t[i] == j)
                    {
                        c = k[j - 65];
                        printf("%c", c);
                    }
                }
            }
            else if (islower(t[i]))
            {
                for (int j = 97; j < 123; j++)
                {
                    if (t[i] == j)
                    {
                        c = k[j - 97] + 32;
                        printf("%c", c);
                    }
                }
            }
            else
            {
                printf("%c", t[i]);
            }
        }
        printf("\n");
        return 0;
    }
}

int validate_key(string k)                          // Validating key
{
    int l = strlen(k);
    int R = 0;
    int A = 0;
    if (l == 26)                           // 26 letters
    {
        for (int i = 0; i < l; i++)
        {
            if (isdigit(k[i]))                  // No digits
            {
                printf("key must not contain digits.\n");
                A = 3;
                return 1;
            }
            if (isalpha(k[i]))                   // If the key is alphabetic
            {
                R++;
            }
            if (islower(k[i]))                  // lowercase
            {
                k[i] = k[i] - 32;               // From a to A
            }
        }
        for (int i = 0; i < l; i++)
        {
            for (int j = 0; j < l; j++)
            {
                if (i != j)
                {
                    if (k[i] == k[j])     // Repeated char
                    {
                        printf("key must not contain repeated characters.\n");
                        A = 4;
                        return 1;
                    }
                }
            }
        }
    }
    else if (l != 26)                   // +26 or -26 char
    {
        printf("Key must contain 26 characters.\n");
        A = 2;
        return 1;
    }
    return A;
}