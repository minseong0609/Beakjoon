#include <stdio.h>

int main() {
  int arr[1000000]={0,};
  int n;
  scanf("%d", &n);
  for(int i=0 ; i<n ; i++){
    scanf("%d", &arr[i]);
  }
  int min = 1000000;
  int max = -1000000;

  for(int j=0; j < n; j++){
    if(min > arr[j]){
      min = arr[j];
    }
    if(max < arr[j]){
      max = arr[j];
    }
  }
  printf("%d %d",min,max);
  
  //모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
  return 0;
}
