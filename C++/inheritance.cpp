#include<iostream>
#include<string>

using namespace std;

class Teacher {

    public:
        Teacher() {
            cout<<"In teacher class"<<endl;
        };
    string location = "New York";

};

class HistoryTeacher : public Teacher {
    public:

        HistoryTeacher() {
            cout<<"In history class"<<endl;
        };
        string location = "Newark";
        int id = 2123;
};


int main() {

    HistoryTeacher obj;
}