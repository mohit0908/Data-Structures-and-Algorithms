#include<iostream>
using namespace std;

class Demo {
    private:
    int num;
    char ch;

    public:
        int getNum(){
            return num;
        }
        char getChar(){
            return ch;
        }
        void setNum(int x) {
            this->num = x;
        }
        void setChar(char c) {
            this->ch = c;
        }
};

int main() {

    Demo obj;
    int x;
    char c;
    cout<<"Enter integer:";
    cin>>x;
    cout<<"Enter char:";
    cin>>c;

    obj.setChar(c);
    obj.setNum(x);
    cout<<"Integer entered:"<<obj.getNum<<endl;
    cout<<"Char entered:"<<obj.getChar<<endl;
    
    
    }