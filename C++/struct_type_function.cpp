#include<iostream>
#include<string>

using namespace std;

struct student{
    int age;
    char name[30];
};

student setInfo();
void displayInfo(student);

int main(){
    student s;
    cout<<"Enter student info"<<endl;
    s = setInfo();
    cout<<"Displaying info:"<<endl;
    displayInfo(s);

    };
student setInfo(){
    student s;
    cout<<"Enter name:";
    cin.getline(s.name, 30);
    cout<<"Enter age:";
    cin>>s.age;
    return s;
};

void displayInfo(student s){
    cout<<"Person name:"<<s.name<<endl;
    cout<<"Person age:"<<s.age<<endl;
}