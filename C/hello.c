#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("what's your name ? ");
    printf("Hello ,%s!\n",name);
}

// You can compile the code using $ clang -o hello hello.c -lcs50 (if cs50.h is included)
// if only stdio.h is included you can compile using $ clang hello hello.c
