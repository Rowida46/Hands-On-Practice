#include<iostream>
using namespace std;
int main(){
int *x;
 x = new int ;
 *x = 90;
 cout<<*x<<endl;
cout<<x<<endl<<&x<<endl<<"----------------Delet------------"<<endl;
delete x;
x = new int ;
*x = 100;
cout<<x<<endl<<*x<<endl<<&x;

}

