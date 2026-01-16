#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);

    int arr[n][2];
    int final_arr[n];

    for(int i=0; i<n; i++){
        int a,b;
        scanf("%d %d", &a, &b);
        arr[i][0] = a;
        arr[i][1] = b;
        final_arr[i] = 1;
    }

    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            if(arr[j][0] > arr[i][0] &&     arr[j][1] > arr[i][1]){
                final_arr[i]  ++;
            }
        }
    }
    for (int i = 0; i<n; i++) {
        printf("%d ", final_arr[i]);
    }

}
