#include<iostream>
using namespace std;


class Animal {
    public:
    virtual void member_func(){
        cout<<"This is a Animal class function"<<endl;
    }
};

class Camel: public Animal {
    public:

    void member_func(){
        cout<<"This is Camel class function"<<endl;
    }
};

int main() {
    Animal *obj;
    obj = new Camel();
    obj->member_func();
}