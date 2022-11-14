#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    float l, w, s, L, S, index; // Var declaration
    string text = get_string("Text: ");
    l = count_letters(text);
    w = count_words(text);
    s = count_sentences(text);
    L = l * 100 / w;                             // L is the average number of letters per 100 words in the text
    S = s * 100 / w;                             // S is the average number of sentences per 100 words in the text
    index = (0.0588 * L) - (0.296 * S) - 15.8;   // Coleman-Liau index

    // Grade

    if (index >= 1 && index <= 15)
    {
        printf("Grade %.0f\n", round(index));
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade 16+\n");
    }
}

int count_letters(string text) // Letters count
{
    int l = strlen(text);
    int letters = 0;
    for (int i = 0; i < l; i++)
    {
        if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122)) // from A-Z & a-z
        {
            letters = letters + 1 ;
        }
    }
    return letters;
}

int count_words(string text) // Words count
{
    int l = strlen(text);
    int words = 1;
    for (int i = 0; i < l; i++)
    {
        if (text[i] == 32)                      // The ASCII number of space is 32
        {
            words = words + 1 ;
        }
    }
    return words;
}

int count_sentences(string text)                // Sentences count
{
    int l = strlen(text);
    int sentences = 0;
    for (int i = 0; i < l; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)    // ASCII 33 = '!' / 46 = '.' / 63 = '?'
        {
            sentences = sentences + 1 ;
        }
    }
    return sentences;
}
