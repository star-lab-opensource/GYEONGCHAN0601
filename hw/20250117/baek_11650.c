#include <stdio.h>

int main(){
    int n ;
    scanf("%d", &n);

    int arr1[n][2];

    int tem_a;
    int tem_b;

    for(int i=0 ; i<n ; i++){
            int a, b;
            scanf("%d %d", &a, &b);
            arr1[i][0] = a;
            arr1[i][1] = b;

    }
    for(int j = 0; j<n-1; j++){
        for(int i=0; i<n-1-j; i++){
            if(arr1[i][0] == arr1[i+1][0]){
                if(arr1[i][1]>arr1[i+1][1]){
                    tem_a = arr1[i][0];
                    tem_b = arr1[i][1];

                    arr1[i][0] = arr1[i+1][0];
                    arr1[i][1] = arr1[i+1][1];

                    arr1[i+1][0] = tem_a;
                    arr1[i+1][1] = tem_b;
                }
            }

            else if(arr1[i][0]>arr1[i+1][0]){
                tem_a = arr1[i][0];
                tem_b = arr1[i][1];

                arr1[i][0] = arr1[i+1][0];
                arr1[i][1] = arr1[i+1][1];

                arr1[i+1][0] = tem_a;
                arr1[i+1][1] = tem_b;
        }
    }
    }


    for(int i=0 ; i<n ; i++){
            for(int j=0; j<2; j++){
                printf("%d ", arr1[i][j]);
            }
            printf("\n");
    }
}
