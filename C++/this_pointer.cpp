#include<iostream>

using namespace std;

class Demo{
    private:
        int num;
        int ch;

    public:
        void setValues(int num, int ch){
            this->num = num;
            this->ch = ch;
        }
        void showValues(){
            cout<<num<<endl;
            cout<<ch<<endl;
        }
};

int main(){

    Demo obj;
    obj.setValues(10, 20);
    obj.showValues();
    return 0;
}