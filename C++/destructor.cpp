#include<iostream>
using namespace std;

class Demo{

    public:

        Demo(){
            cout<<"Constructor called"<<endl;
        }

        ~Demo(){

            cout<<"Destructor called"<<endl;
        }

        void display(){
            cout<<"Display function called"<<endl;
        }
};

int main(){

    Demo obj;
    obj.display();
    return 0;
};