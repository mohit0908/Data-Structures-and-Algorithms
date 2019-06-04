#include<iostream>

using namespace std;

int main(){

    char str[50] = "String of ice and fire";
    char book[50];
    cout<<"Enter book name:";
    cin.get(book, 20);
    cout<<"Entered book name:"<<book<<endl;

    cout<<str<<endl;
}