#include <stdio.h>
int main(void)
{
    int r,c;
    do{
    printf("Nb of row : ");
    scanf("%d",&r);
    printf("Nb of column : ");
    scanf("%d",&c);
    }
 //   start:
    while(r<1 && c<1);
        // for each row
        for(int i=0;i<r;i++)
        {
        // for each column
            for(int j=0;j<c;j++)
            {
                //print a brick
            printf("#");
             }
             //move to next row
          printf("\n");
    }
    
}


