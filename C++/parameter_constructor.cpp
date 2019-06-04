#include<iostream>
using namespace std;
class demo{

    public:
    demo(int a, int b){
        cout<<a+b<<endl;
    }
};

int main(){

    demo obj(10, 20);
}