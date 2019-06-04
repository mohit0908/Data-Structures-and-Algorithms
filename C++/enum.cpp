#include<iostream>
using namespace std;

enum direction {east, west, north, south};

int main(){
    direction dir;

    dir = north;

    cout<<"Direction:"<<dir<<endl;
    return 0;
}