#include <stdio.h>
#include <string.h>
int main(){
    char number[100000];

    while(1){
        scanf("%s", number);

        int len = strlen(number);
        int real_pal = 1;

        if(strlen(number) == 1 && number[0] == '0'){
            break;
        }

        for(int i =0; i<len; i++){
            if(number[i] != number[len-1-i]){
                real_pal = 0;
                break;
            }
        }

        if(real_pal){
            printf("yes\n");
        }
        else{
            printf("no\n");
        }
    }

}
