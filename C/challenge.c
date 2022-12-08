#include <stdio.h>

int main(void){
    int val = 30;
    for (int z = 1;z<30;z++){
        if (z == 4 || z == 9 || z == 15 || z == 23){
            z++;
            continue;

        }
        for (int i = 0;i<30-z;i++){
            printf(" ");
        }
        val--;
        printf("/");
        for (int j = 1;j<z*2;j++){
            if ( z >= 25 && z <= 30 ) {
                if (z == 27){
                    if (j == z - 2){
                        printf("|||$|");
                        j+=5;
                    }
                }
                else{
                    if (j == z - 2){
                        printf("|||||");
                        j+=5;
                    }
                }
            }
            printf("*");
        }

        printf("\\\n");

    }
    for (int i=0;i<60;i++)
            printf("-");

}
