#include<iostream>
#include<cstring>
using namespace std;

struct student{
    char name[11];
    int age;
};


int main(){

    student s1, s2;
    s1.age = 10;
    string str = "James Bond";
    strcpy(s2.name, str.c_str());

    cout<<s1.age<<endl;
    cout<<s2.name<<endl;
}