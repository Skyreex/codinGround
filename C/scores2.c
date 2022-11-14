#include <stdio.h>
#include <cs50.h>
// Array
int main(void)
{
    int j = get_int("How many subjects : ");
    int score[j];
    for (int i=0;i<j;i++)
    {
   //     for(int J=1;J<j+1;J++)
        score[i] = get_int("score ");
     //   break ;
    }
    printf("the average is : %.2f \n",(score[j-1] )/(float)j);

}