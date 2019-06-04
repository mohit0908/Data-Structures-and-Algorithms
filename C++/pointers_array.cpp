#include<iostream>

using namespace std;

int main(){


    int arr[] = {1,2,3,4,5};
    int *p;
    p = arr;

    for (int i = 1; i<=10;i++){
        cout<<"Array value:"<<*p<<endl;
        p++;
    }

    return 0;
}