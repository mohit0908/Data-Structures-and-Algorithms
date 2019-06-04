#include <iostream>
using namespace std;

int main() {
//code
int testNum;
cin >> testNum;
for(int i = 0; i < testNum; ++i){

int arrNum, findNum;
cin >> arrNum >> findNum;

int findIndex = -1;
int arrData[arrNum];
for (int j = 0; j < arrNum; ++j) {

cin >> arrData[j];
if(findIndex == -1 && arrData[j] == findNum) {
findIndex = j;
}
}

cout << findIndex << "\n";

}

return 0;
}