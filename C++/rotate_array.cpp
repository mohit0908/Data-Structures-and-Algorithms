#include<iostream>
using namespace std;

void rotatearray(int arr[], int n){
    int i;
    int temp = arr[0];

    for(i = 0; i< n-1; i++){
        arr[i] = arr[i+1];
    }
    arr[i] = temp;
}

void leftrotate(int arr[], int n, int d){
    for (int i = 0; i<d; i++){
         rotatearray(arr, n);
    }
}

void printArray(int arr[], int n){
    for (int i = 0; i< n; i++){
        cout<<arr[i]<<" ";
    }
}

int main(){
    int arr[] = {1,2,3,4,5,6};
    int n = sizeof(arr)/ sizeof(arr[0]);
    
    printArray(arr, n);
    leftrotate(arr, n, 1);
    printArray(arr, n);
}