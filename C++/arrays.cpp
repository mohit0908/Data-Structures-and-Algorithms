#include <iostream>
#include <cmath>
using namespace std;
/* This method prints the square of each
 * of the elements of multidimensional array
 */
void square(int arr[2][3]){
   int temp;
   for(int i=0; i<2; i++){
      for(int j=0; j<3; j++){
        temp = arr[i][j];
        cout<<pow(temp, 2)<<endl;
      }
   }
}
int main(){
   int arr[2][3] = { 
       {1, 2, 3},
       {4, 5, 6}
   };
   square(arr);
   return 0;
}