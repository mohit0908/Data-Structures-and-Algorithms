#include<iostream>

using namespace std;

class constructorDemo{
    public:
    int num; char ch;

    constructorDemo(){
        num = 100;
        ch = 'A';
    }
};

int main(){


    constructorDemo obj;

    cout<<"Num value:"<<obj.num<<endl;
    cout<<"Character:"<<obj.ch<<endl;
};