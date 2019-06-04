#include<iostream>
using namespace std;

struct student{
    int age;
    char name[30];
};

void printInfo(student);

int main(){
    student s;
    cout<<"Enter student name";
    cin.getline(s.name, 30);
    cout<<"Enter student age:";
    cin>>s.age;


    printInfo(s);
}

void printInfo(student s){
    cout<<"Student name"<<s.name<<endl;
    cout<<"Student age"<<s.age<<endl;
}