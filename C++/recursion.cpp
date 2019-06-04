#include<iostream>

using namespace std;


int recursion(int);


int main(){

    int x;
    cout<<"Enter number for recursion:";
    cin>>x;
    cout<<"Recursion:"<<recursion(x)<<endl;

}


int recursion(int x){

    if (x == 1) 
        return 1;
    else 
        return x * recursion(x-1);

}